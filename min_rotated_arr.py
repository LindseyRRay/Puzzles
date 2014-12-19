# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# You may assume no duplicate exists in the array.
from random import randint

class Solution:
    # @param num, a list of integer
    # @return an integer
    @staticmethod
    def findMin(num):
        if not num:
            return None
        else:
            for index, element in enumerate(num):
                if index == 0:
                    min_el = element
                elif index > 0:
                    if element < num[index-1]:
                        min_el = element
            return min_el

    @staticmethod
    def rec_findmin(num):
        if len(num) ==1 or num[0] < num[-1]:
            return num[0]
        return Solution.rec_min(num, 0, len(num)-1)

    @staticmethod
    def rec_min(num, a, b):
        if a+1 == b:
            return min(num[a], num[b])
        if num[a] > num[int((a+b)/2)]:
            return Solution.rec_min(num, a, int((a+b)/2))
        else:
            return Solution.rec_min(num, int((a+b)/2), b)



    @staticmethod
    def rotate_list(num):
        pivot = randint(0,len(num)-1)
        print("Pivot is %s"%pivot)
        return num[pivot:]+num[:pivot]



if __name__ == '__main__':

    print(Solution.findMin([]))
    l1 = [randint(0,100) for x in range(5)]
    l1.sort()
    print("original list")
    [print(element) for element in l1]
    l1 = Solution.rotate_list(l1)
    print("rotated list") 
    [print(element) for element in l1]
    print("Answer")
    print(Solution.findMin(l1))
    print("Starting rec")
    print(Solution.rec_findmin(l1))
    



    