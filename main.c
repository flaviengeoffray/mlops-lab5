#include <stdio.h>

float linear_regression_prediction(float* features, float* thetas, int n_parameters) {
    float prediction = thetas[0]; // Intercept term
    for (int i = 0; i < n_parameters; i++) {
        prediction += features[i] * thetas[i + 1];
    }
    return prediction;
}

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
    return 1.0 / (1.0 + exp_approx(-x, 10));
}

float logistic_regression(float* features, float* thetas, int n_parameters) {
    float prediction = thetas[0]; // Intercept term
    for (int i = 0; i <= n_parameters; i++) {
        prediction += features[i] * thetas[i + 1];
    }
    return sigmoid(prediction);
}

int main() {

    // --- Ex 1 ---
    // float X[] = {1.0, 1.0, 1.0};
    // float thetas[] = {0.0, 1.0, 1.0, 1.0};
    // int n_parameters = 3;

    // float prediction = linear_regression_prediction(X, thetas, n_parameters);
    // printf("Prediction: %f\n", prediction);
    // return 0;


    // --- Ex 2 ---
    // float x = 1.0;
    // int n_terms = 5;
    // float result = exp_approx(x, n_terms);
    // printf("Approximation of e^%f using %d terms: %f\n", x, n_terms, result);
    // return 0;


    // --- Ex 3 ---
    float x = 0.0;
    float result = sigmoid(x);
    printf("Sigmoid(%f) = %f\n", x, result);
    return 0;
}
