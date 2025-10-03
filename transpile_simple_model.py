import joblib
import subprocess

def transpile_linear_model():

    model = joblib.load('regression.joblib')
    
    coefficients = model.coef_
    intercept = model.intercept_
    n_features = len(coefficients)

    c_code = """#include <stdio.h>

    float prediction(float *features, float *thetas, int n_parameters) {
        float pred = thetas[0]; // Intercept term
        for (int i = 0; i < n_parameters; i++) {
            pred += features[i] * thetas[i + 1];
        }
        return pred;
    }
    """

    c_code += """
    int main() {
    """
    example_data = [200, 2, 1] # size = 200, nb_rooms = 2, garden = 1
    c_code += f"    float features[{n_features}] = {{"
    c_code += ", ".join([f"{val:.6f}" for val in example_data])
    c_code += "};\n"

    c_code += f"    float thetas[{n_features + 1}] = {{{intercept:.6f}"
    c_code += ", " + ", ".join([f"{coef:.6f}" for coef in coefficients])
    c_code += "};\n"
    
    c_code += f"    float pred = prediction(features, thetas, {n_features});\n"
    c_code += "    printf(\"Prediction: %f\\n\", pred);\n"
    c_code += "    \n"
    c_code += "    return 0;\n"
    c_code += "}\n"

    filename = "linear_model.c"
    with open(filename, 'w') as f:
        f.write(c_code)
    
    print(f"Code C généré dans {filename}")
    
    compile_cmd = f"gcc -o linear_model {filename} -lm"
    print(f"Commande de compilation: {compile_cmd}")
    
    try:
        subprocess.run(compile_cmd.split(), check=True)
        print("Compilation réussie! Exécutable: ./linear_model")
    except subprocess.CalledProcessError:
        print("Erreur lors de la compilation")


def transpile_logistic_model():
    model = joblib.load('regression.joblib')
    
    coefficients = model.coef_
    intercept = model.intercept_
    n_features = len(coefficients)

    c_code = """#include <stdio.h>

    #include <math.h>

    float exp_approx(float x, int n_term) {
        float sum = 1.0; // First term of the series

        float xkm1 = 1.0; // x^k-1
        float km1_fact = 1.0; // (k-1)!

        for (int n = 1; n <= n_term; n++) {
            float xk = xkm1 * x; // Compute x^k
            float k_fact = km1_fact * n; // Compute k!
            sum += xk / k_fact; // Add the k-th term to the sum

            xkm1 = xk; // Update x^k-1 for next iteration
            km1_fact = k_fact; // Update (k-1)! for next iteration
        }
        return sum;
    }

    float sigmoid(float x) {
        return 1.0f / (1.0f + expf(-x));
    }

    float logistic_regression(float* features, float* thetas, int n_parameters) {
        float prediction = thetas[0]; // Intercept term
        for (int i = 0; i < n_parameters; i++) {
            prediction += features[i] * thetas[i + 1];
        }
        return sigmoid(prediction);
    }
    """

    c_code += """int main() {
"""
    example_data = [200, 2, 1] # size = 200, nb_rooms = 2, garden = 1
    c_code += f"    float features[{n_features}] = {{"
    c_code += ", ".join([f"{val:.6f}" for val in example_data])
    c_code += "};\n"

    c_code += f"    float thetas[{n_features + 1}] = {{{intercept:.6f}"
    c_code += ", " + ", ".join([f"{coef:.6f}" for coef in coefficients])
    c_code += "};\n"

    c_code += f"    float pred = logistic_regression(features, thetas, {n_features});\n"
    c_code += "    printf(\"Prediction: %f\\n\", pred);\n"

    c_code += """    return 0;
}"""

    filename = "logistic_model.c"
    with open(filename, 'w') as f:
        f.write(c_code)

    print(f"Code C généré dans {filename}")

    compile_cmd = f"gcc -o logistic_model {filename} -lm"
    print(f"Commande de compilation: {compile_cmd}")

    try:
        subprocess.run(compile_cmd.split(), check=True)
        print("Compilation réussie! Exécutable: ./logistic_model")
    except subprocess.CalledProcessError:
        print("Erreur lors de la compilation")

def transpile_tree_model():

    model = joblib.load('tree_model.joblib')
    tree = model.tree_

    # Fonction récursive pour générer le code C
    def recurse(node, depth=1):
        indent = "    " * depth
        if tree.feature[node] == -2:  # feuille
            value = tree.value[node][0][0]
            return f"{indent}return {value};\n"
        else:
            feat = tree.feature[node]
            thresh = tree.threshold[node]
            code = f"{indent}if (features[{feat}] <= {thresh:.6f}) {{\n"
            code += recurse(tree.children_left[node], depth + 1)
            code += f"{indent}}} else {{\n"
            code += recurse(tree.children_right[node], depth + 1)
            code += f"{indent}}}\n"
            return code

    c_code = "#include <stdio.h>\n\n"
    c_code += "float simple_tree(float *features, int n_features) {\n"
    c_code += recurse(0)
    c_code += "}\n\n"

    n_features = tree.n_features
    example_data = [200, 2, 1]  # size = 200, nb_rooms = 2, garden = 1
    c_code += "int main() {\n"
    c_code += f"    float features[{n_features}] = {{"
    c_code += ", ".join([f"{v:.6f}" for v in example_data])
    c_code += "};\n"
    c_code += f"    float pred = simple_tree(features, {n_features});\n"
    c_code += "    printf(\"Prediction: %f\\n\", pred);\n"
    c_code += "    return 0;\n"
    c_code += "}\n"

    filename = "tree_model.c"
    with open(filename, 'w') as f:
        f.write(c_code)
    print(f"Code C généré dans {filename}")

    compile_cmd = f"gcc -o tree_model {filename}"
    print(f"Commande de compilation: {compile_cmd}")
    try:
        subprocess.run(compile_cmd.split(), check=True)
        print("Compilation réussie! Exécutable: ./tree_model")
    except subprocess.CalledProcessError:
        print("Erreur lors de la compilation")



if __name__ == "__main__":
    transpile_linear_model()
    transpile_logistic_model()
    transpile_tree_model()
