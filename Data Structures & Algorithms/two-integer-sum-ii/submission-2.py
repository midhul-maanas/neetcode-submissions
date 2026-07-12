class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers)-1
        numbers.sort()
        print(f"Sorted: {numbers}")
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                print(f"Checking {numbers[i]}:{numbers[j]}")
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        return [0,0]