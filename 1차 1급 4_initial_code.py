#You may use import as below.
#import math

def solution(num):
    num += 1
    nums = str(num).replace("0", "1")
    print(nums)

#The following is code to output testcase.
num = 9949999
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")