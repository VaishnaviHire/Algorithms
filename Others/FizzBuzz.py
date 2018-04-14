#attribution: www.leetcode.com
# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the
#  multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
      
        for i in range(n):
            if divmod(i + 1,3)[1] == 0 and divmod(i + 1,5)[1] == 0:
                result.append("FizzBuzz")
            elif divmod(i + 1,3)[1] == 0:
                result.append("Fizz")
            elif divmod(i + 1,5)[1] == 0:
                result.append("Buzz")
            else:
                result.append(str(i + 1))
        
        return result