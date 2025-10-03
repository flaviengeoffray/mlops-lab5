#include <stdio.h>

float prediction(float *features, int n_features) {
    float result = -8152.937710;
    result += features[0] * 717.258370;
    result += features[1] * 36824.195974;
    result += features[2] * 101571.840022;
    return result;
}

int main() {
    float features[3] = {200.000000, 2.000000, 1.000000};
    
    float pred = prediction(features, 3);
    printf("Prediction: %f\n", pred);
    
    return 0;
}