class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_value = 5000000
        res = 0
        valid_value = True
        for start_value in range(1, 1000000):
            sum_ = start_value
            valid_value = True
            current_min_value = 5000000
            current_res = 0
            for j in nums:
                sum_ = sum_ + j
                if sum_ < 1:
                    valid_value = False
                    break
                if sum_ < current_min_value:
                    current_min_value = sum_
                    current_res = start_value
            if valid_value and current_min_value < min_value:
                min_value = current_min_value
                res = current_res
                return res
                #print(min_value, res)
        #print("End")
        return res
        
                