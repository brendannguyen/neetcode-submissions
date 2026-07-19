class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # simulate multiplication on paper
        # O(m*n)
        # space: O(m+n)

        if "0" in [num1, num2]:
            return "0"
        
        result = [0] * (len(num1)+len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i])*int(num2[j]) # multiply digits

                result[i+j] += digit # add product
                result[i+j+1] += (result[i+j]  // 10) # carry
                result[i+j] = result[i+j]%10 # keep ones digit only

        result, beg = result[::-1], 0
        
        # remove leading zeros
        while beg < len(result) and result[beg] == 0:
            beg += 1
        
        # convert num result to array of strings
        result = map(str, result[beg:])
        return "".join(result)

