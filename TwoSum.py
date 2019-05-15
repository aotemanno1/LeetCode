class Solution:
    def twoSum(self, nums, target):
        result = [0, 0]
        for index1 in range(len(nums)-1):
            for index2 in range(index1+1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    result[0] = index1
                    result[1] = index2
        print(result)


def main():
    nums = [2, 7, 11, 15]
    target = 17
    test = Solution()
    test.twoSum(nums, target)


if __name__ == '__main__': main()
