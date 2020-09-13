#include <iostream>
#include <math.h>

using namespace std;

bool is_prime(int x);

int main() {

    int n = 2'000'000;
    int i = 2;
    long long int ans = 0;

    for (int p = 1; p <= n; p++) {
        if (is_prime(p)) {
            ans += p;
        }
    }

    cout << ans << endl;

}

bool is_prime(int x) {
    if (x <= 1) {
        return false;
    } else if (x <= 3) {
        return true;
    } else if (x % 2 == 0) {
        return false;
    } else {
        for (int i=3; i <= int(sqrt(x)); i+=2) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }
}
