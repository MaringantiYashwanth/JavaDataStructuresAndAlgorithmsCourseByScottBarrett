var maxSequence = function(arr) {
	var min = 0, ans = 0, sum = 0;
	for (let i = 0; i < arr.length; i++) {
		sum += arr[i];
		min = Math.min(sum, min);
		ans = Math.max(ans, sum - min);
	}
	return ans;
}

var maxSequence = function (arr) {
	let maxSoFar = -Infinity;
	let maxEndingHere = 0;
	/*
	* Kadane's algorithm
	* 1. initialize the maxSoFar variable to small possible to track the maximum element so far
	* 2. initialize the maxEndingHere to track the maximum possible value
	* 3. iterate through an array
	* 4. update the maxEndingHere by adding the current element
	* 5. if maxEndingHere is greater than  the maxSoFar then update the maxSoFar
	* 6. with the maxEndingHere value
	* 7. if maxEndingHere is less than zero then reset it's value to 0
	* 8. Finally return the maxSoFar
	*/
	for (let e of arr) {
		maxEndingHere = e;
		if (maxEndingHere > maxSoFar) {
			maxSoFar = maxEndingHere;
		}
		if (maxEndingHere < 0) {
			maxEndingHere = 0;
		}
	}
	return maxSoFar;
}