## Maximum Subarray (Leetcode: 53)

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

```
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

```

## Solution

### Method 1: Storing Sum

- i =0, j= 0, maxSum = -inf
- sum[i] = sum[i-1] + arr[i]
- sum(i, j) = sum[j] - sum[i]
- maxSum can be calculated by determining for every i, j pair in the array max(sum(i,j), arr[j])

<b>Time Complexity = O(n^2)<br>
Space Complexity = O(n)</b>

### Methode 2: Kadane`s Algorithm

- Create two variables which store `current_sum` and `max_sum`
- `current_sum` depicts the sum of numbers till current index
- `max_sum` depicts the maximum of all current sums
- hence, calculate both value of both variables for each index

<b>Time Complexity = O(n)<br>
Space Complexity = O(1)</b>