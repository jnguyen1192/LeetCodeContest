class Solution:
    
    def findMinFibonacciNumbers(self, k: int) -> int:
        #return the minimum number of Fibonacci numbers whose sum is equal to k
        F1 = 1
        F2 = 1
        #Fn = Fn-1 + Fn-2 , for n > 2.
        fib_numbers = []
        fib_numbers.append(F1)
        fib_numbers.append(F2)
        for i in range(10**9):
            if fib_numbers[i] + fib_numbers[i+1] > 10**9:
                break
            fib_numbers.append(fib_numbers[i] + fib_numbers[i+1])
        # get k max less
        index_max = 0
        for index, fib_number in enumerate(fib_numbers):
            index_max = index
            if fib_number > k:
                break
        sum_ = 0
        nb_sum = 0
        for fib_number in fib_numbers[index_max::-1]:
            if sum_ + fib_number <= k:
                sum_ += fib_number
                nb_sum += 1
                
        return nb_sum