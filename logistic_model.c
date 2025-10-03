#include <stdio.h>

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
    int main() {
    float features[3] = {200.000000, 2.000000, 1.000000};
    float thetas[4] = {-8152.937710, 717.258370, 36824.195974, 101571.840022};
    float pred = logistic_regression(features, thetas, 3);
    printf("Prediction: %f\n", pred);
    return 0;
}