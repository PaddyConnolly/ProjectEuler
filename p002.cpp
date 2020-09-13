#include <iostream>

using namespace std;

int main() {

    int sum = 0;

    for (int prev = 1, curr = 2; curr <= 4'000'000;) {
        if (curr % 2 == 0) {
            sum += curr;
        }

        curr += prev;
        prev = curr - prev;
    }

    cout << sum << endl;


}