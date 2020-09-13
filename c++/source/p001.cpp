#include <iostream>

using namespace std;

int main() {

    int ans; 
    for (int i = 3; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            ans += i;
        }
    }

    cout << ans << endl;
    
}