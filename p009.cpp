#include <iostream>

using namespace std;

int main() {

    for (int m = 0; m < 30; m++) {
        for (int n = 0; n < 30; n++) {
            int a[3] = {m*m + n*n, 2*m*n, m*m - n*n};
            int sum = 0;

            for(int i = 0; i < 3; i++) {
                sum += a[i];
            }

            if (sum == 1000) {

                int prod = 1;

                for(int i = 0; i < 3; i++) {
                    prod *= a[i];
                }

                cout << prod << endl;


            }

        }
    }


}



    

