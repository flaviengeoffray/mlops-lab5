#include <stdio.h>

    float prediction(float *features, float *thetas, int n_parameters) {
        float pred = thetas[0]; // Intercept term
        for (int i = 0; i < n_parameters; i++) {
            pred += features[i] * thetas[i + 1];
        }
        return pred;
    }
    
    int main() {
        float features[3] = {200.000000, 2.000000, 1.000000};
    float thetas[4] = {-8152.937710, 717.258370, 36824.195974, 101571.840022};
    float pred = prediction(features, thetas, 3);
    printf("Prediction: %f\n", pred);
    
    return 0;
}
