const sumDivisibleOf3and5 = () => {
	let sum = 0;

	for (let i = 0; i < 1000; i++) {
		if (!(i % 3) || !(i % 5)) {
			sum += i;
		}
	}

	return sum;
}

console.log(sumDivisibleOf3and5());
