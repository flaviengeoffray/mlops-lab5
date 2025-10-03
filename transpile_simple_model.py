import joblib
import numpy as np
import subprocess
import os

def transpile_model():

    model = joblib.load('regression.joblib')
    
    coefficients = model.coef_
    intercept = model.intercept_
    n_features = len(coefficients)

    c_code = f"""#include <stdio.h>

float prediction(float *features, int n_features) {{
    float result = {intercept:.6f};
"""
    for i, coef in enumerate(coefficients):
        c_code += f"    result += features[{i}] * {coef:.6f};\n"
    
    c_code += """    return result;
}

int main() {
"""
    example_data = [200, 2, 1] # size = 200, nb_rooms = 2, garden = 1
    c_code += f"    float features[{n_features}] = {{"
    c_code += ", ".join([f"{val:.6f}" for val in example_data])
    c_code += "};\n"
    
    c_code += f"""    
    float pred = prediction(features, {n_features});
    printf("Prediction: %f\\n", pred);
    
    return 0;
}}"""
    
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

if __name__ == "__main__":
    transpile_model()
