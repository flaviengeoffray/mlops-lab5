#include <stdio.h>

float simple_tree(float *features, int n_features) {
    if (features[0] <= 78.002831) {
        return -194619.561109506;
    } else {
        if (features[0] <= 158.476189) {
            if (features[0] <= 153.471748) {
                return 250010.8604221458;
            } else {
                return -264704.42010859;
            }
        } else {
            if (features[2] <= 0.500000) {
                return 252134.46650306377;
            } else {
                return 300020.3322925896;
            }
        }
    }
}

int main() {
    float features[3] = {200.000000, 2.000000, 1.000000};
    float pred = simple_tree(features, 3);
    printf("Prediction: %f\n", pred);
    return 0;
}
