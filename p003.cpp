#include <iostream>

#define ll long long

using namespace std;

ll lpf (ll n); 

int main() {

   cout << lpf(600851475143) << endl;

} 

ll lpf(ll n) {
    ll ans = 0;
    for (ll i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            ans = i;
            while (n % i == 0) {
                n /= i;
            }
        }
    
    }

    if (n > 1) {
        ans = n;
    }

    return ans; 

}   