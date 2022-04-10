#include <stdint.h>
#include <iostream>
#include <string>

using namespace std;

int sumDivisibleBy3or5(void) {
	int sum = 0;
	for (int i = 0; i < 1000; i++) {
		if (!(i % 3) || !(i % 5)) {
			sum += i;
		}
	}
	return sum;
}

int main(void) {
	cout << sumDivisibleBy3or5();
	return 0;
}
