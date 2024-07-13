#include <iostream>
#include "cmath"
using namespace std;

int main() {
    double x = 5;
    double z = 0.01;

    double sum = 0;
    double term = 1;
    for (int n = 1; n < 5; n++) { // fabs(term) > z
        term = (pow(x, 2 * n - 1)) / (2 * n - 1);
        sum += term;
        cout << sum << endl;
    }

    double answer = sum * 2;
    double answer2 = log((1 + x) / (1 - x));

    cout << "Точная сумма = " << answer2 << endl;
    cout << "Разница = " << fabs(answer2) - fabs(sum) << endl;
    cout << answer << endl;

    return 0;
}



