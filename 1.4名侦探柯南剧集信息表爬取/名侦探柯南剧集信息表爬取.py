from  typing  import List
import collections
import sys
import string
# #fibonacci serier斐波拉契
# a,b = 0,1
# while b < 10:
#     print (b, end='\t')
#     # a, b = b, a+b #先更新左边的a，右边的a是之前的a
#     m = a+b #前两项相加
#     a = b   #a赋值为前一项值
#     b = m   #更新b == 输出m
#     #3 5 \b=5 a=3 \b=3+5 a=5
#     #ab更新b，a变'刚才'的b

# #3-100的质数
# for n in range(3,100):
#     for i in range(3,n):
#         if n%i == 0:
#             #n不是质数
#             break #break不会触发本层else 不需要flag
#     else:
#         print(n, '是质数')
# else:
#     print('n 3-100 结束')

# #格式化 美化列表 
# try:
#     a = [66, 333, 333, 1, 1234]
#     b = a.copy()
#     mat = '{:8d} |{:4d}'
#     print('%-8s' % '元素值','%-4s' % '剩余个数')
#     for i in range(len(b)):
#         # print(mat.format(b.pop(), len(b))
#         print(mat.format(b.pop(), len(b)))
# except BaseException as e:
#     print(e)
# #4种（格式化）输出
# print('pi的值',math.pi,'*\t*')     #,x, |x左右自带空格
# print('pi的值%f\t*' % math.pi)     # % 旧式字符串格式化
# print('pi的值{}\t*'.format(math.pi)) #’‘.format（）使用这种
# print(f'pi的值{math.pi}')             #f'{xx}'

##3x4 转 4x3 矩阵转置
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ] 
##1 数组方法
# for row in matrix: #输出原矩阵
#     for j in range(4):
#         print('%d' % row[j],end='\t')
#     print()
# print('-'*20)
# #创建B 
# arrb=[[None]* len(matrix)  for row in range(len(matrix[0]))] 
# for i in range(4):      #行
#     for j in range(3):  #列
#         arrb[i][j] = matrix[j][i]
#         print(arrb[i][j],end='\t')
#     print()
# #2 列表解析嵌套方法
#     #4行列表，使用外层[]组成二维列表/解析
# # arrb = [ [row[i] for row in matrix] for i in range(4)]
# for i in range(4): #  i是matrix的列
#     arrb = [row[i] for row in matrix] #遍历matrix每行i列的元素，组成list
#     print(arrb) 

#leetcode
# #有序列表删除重复项-双指针
#     #p经过的就是输出列表，q会遍历到列表尾部
#     #遇到不相同的数字就加入到p列表中，即p+1 = q
# nums = [0,0,1,1,1,2,2,3,3,4]
# class Solution:
#     def removeDuplicates(self, nums) :
#         #nums type:List[int]
#         #rtype: int
#         p = 0 
#         q = 1
#         for q in range(len(nums)):
#             if(nums[p] == nums[q]):
#                 pass
#             if(nums[p] != nums[q]):
#                 nums[p+1] = nums[q]
#                 p += 1
#         return p+1
        
# x = Solution().removeDuplicates(nums)
# print(nums[:x+1])

# #买卖股票的最佳时机 - 贪心算法
#     #低买高卖，列表中从前之后，差最大。买昨天的股票今天卖出
#     #本质：只要今天i涨了昨天i-1才会买，一维
# price = [7, 1, 5, 3, 6, 4]
# res = 0
# for i in range(1,len(price)):
#     diff = price[i] - price[i-1]
#     if (diff > 0):
#         res += diff
# print(res)
# #买卖股票的最佳时机 - 动态规划
#     #a[i][j] i是天数，j是0现金/1股票 无法执行？？
#       #https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
# a = [[]]
# a[0][0] = 0 
# a[0][1] = -price[0]

# for  i in range(1, len(price) - 1):
#     a[i][0] = max(a[i-1][0], a[i-1][1] + price[i])
#     a[i][1] = max(a[i-1][1], a[i-1][0] - price[i])
# print(a[5][0])

##旋转数组-切片
#     #给定K，元素移动
# nums = [1,2,3,4,5,6,7]
# #k可变，非负数
# k = 3
# k = k % len(nums)
# if (k >= 0):
#     nums = nums[-k:len(nums)]  + nums[0:len(nums)-k]
# print(nums)
# ##旋转数组-反转3
# def list_swap(i, j): 
#     while(i<j):
#         nums[i],nums[j] = nums[j],nums[i]
#         i+=1
#         j-=1

# n = len(nums)
# #整个数组反转
# list_swap(0, n-1)

# list_swap(0, k-1)
# list_swap(k, n-1)


#给定一个整数数组，判断是否存在重复元素。
#如果任意一值在数组中出现至少两次，函数返回 true,反之为false
    #两次for遍历 超时
# flag = False
# nums = [1,2,3,1]
# len = len(nums)
# for i in range(len):
#     for j in range(i+1, len):
#         if nums[i] == nums[j]:
#             # print('{0} == {1}'.format(nums[i],nums[j]), end='\t')
#             flag = True
#             return flag
# if (flag == False):
#     return flag
#     #先排序预处理再判断
# nums.sort()
# for i in range(len(nums)-1):
#     if (nums[i] == nums[i+1]):
#         return True
# return False
    
# #只出现一次的数字 其他出现两次
# #(位运算)具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#     #remove  不使用额外空间，但运行时间久
# a = [2,2,6,1,6]
# i = 0
# while True:
#     c = a[i]
#     a.remove(c)
#     if(c in a):
#         a.remove(c)
#     #移除了两次c
#     else:
#         print(c)
#         break
#         #集合*2-List = 不重复的元素，使用了额外空间
# sum(set(a))*2-sum(a)

##两个数组的交集 II
   #方法1 自己做的，使用字典
#     def Listcount(list1):
#         dict1 = {}
#     for i in list1:
#         dict1.update({i:list1.count(i)})
#     return dict1
# templist = []
# templist2 = []
# nums1dict = Listcount(nums1)
# nums2dict = Listcount(nums2)
# for i in nums1dict.keys():
#     if i in nums2dict.keys():
#         templist.append(i)
# #遍历两个字典，找相同的keys-templist 并且要values少的
# for i in templist:
#     #相同keys 少的values == extend([keys]*values)
#     lessvalues = (nums1dict[i] if nums1dict[i] <= nums2dict[i] else nums2dict[i]) 
#     templist2.extend([i] * lessvalues)
# print(templist2)
    # # 方法2 哈希表两个数组的交集 
# nums1 = [2,9,9,7,5,9]
# nums2 = [1,2,2,1,4,9,9]
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         if len(nums2) <= len(nums1):
#             return self.intersect(nums2,nums1)
        
#         #使nums1长度最小
#         try:
#             #intersection用于存放交集，且最小值
#             intersection = list()
#             #dicttemp是一个计数器-hashmap
#             #{9: 3, 2: 1, 7: 1, 5: 1} 9 2 7 5
#             dicttemp = collections.Counter(nums1)
#             for i in nums2:
#                 if dicttemp.get(i, 0) > 0:
#                     intersection.append(i)
#                     dicttemp[i] -= 1
#             return intersection
#         except Exception as identifier:
#             print('这是错误',identifier)
# Solution().intersect(nums1,nums2)
    ## 方法3 python 集合&运算
        # num1 = collections.Counter(nums1)
        # num2 = collections.Counter(nums2)
        # num = num1 & num2
        # print(num1,'\n',num2)
#     ##有序 交集
# nums1.sort()
# nums2.sort()
# print(nums1)
# print(nums2)
# intersection = list()
# index1 = index2 = 0
# while index1 < len(nums1) and index2 < len(nums2):
#     if nums1[index1] < nums2[index2]:
#         #让小的追上大的
#         index1 += 1
#     elif nums1[index1] > nums2[index2]:
#         index2 += 1
#     #相等
#     else:
#         intersection.append(nums1[index1])
#         index1 += 1
#         index2 += 1
# print(intersection)

# # #输入非负数，数字+1
# digits = [1,9,9]  
# # #不进位，有进位，有进位-多一位
# newlst = []
# while digits and (digits[-1] == 9):
#     digits.pop()
#     newlst.append(0)
# if digits == []:
#     #digits = [] 说明是全999
#     return [1] + newlst
# else:
#     digits[-1] += 1
#     return digits + newlst

##所有 0 移动到数组的末尾，同时保持非零元素的相对顺序
# class Solution:
#     def moveZeroes(self, nums: List[int]):
#         try:
#             j = 0
#             for i in range(len(nums)) :
#                 if nums[i] != 0:
#                     nums[j] = nums[i]
#                     j += 1
#             # 非0元素统计完了，剩下的都是0了
#             # 所以第二次遍历把末尾的元素都赋为0即可
#             for i in range(j,len(nums)):
#                 nums[i] = 0
#         except Exception as a:
#             print(a)
        # # try:
        # #     count = 0
        # #     for i in nums:
        # #         nums.remove(0)
        # #         count += 1
        # # except Exception as a:
        # #     pass
        # # finally:
        # #       nums.extend([0]*count)  
# nums = [0,1,0,3,12]
# Solution().moveZeroes(nums)
# print(nums)

# ##两数之和 不使用暴力破解
#     #给定一个整数数组 nums 和一个目标值 target，
#     #请你在该数组中找出和为目标值的那 两个 整数，
#     #返回他们的数组下标，假设每种输入只会对应一个答案。
#     #但是，数组中同一个元素不能使用两遍
# class Solution:
#     def twoSum(self, nums: List[int], target: int) :
#         if len(nums) < 2:
#            return 0
#         hashmap = {}
#         for index , num in enumerate(nums):
#             itemp = hashmap.get(target - num) 
#             if (itemp is not None) and (index is not itemp):
#                 #找到了
#                 print(hashmap)
#                 return [itemp, index]
#             hashmap[num] =  index
#         #target是某一位num的两倍 防止！
# nums = [3,3]
# target = 6
# a = Solution().twoSum(nums, target)
# print(a)

# ## 旋转图像 原地顺时针旋转 90 度
#     #旋转二维数组 直接修改输入的矩阵
# class Solution:
#     def rotate(self, matrix: List[List[int]]):
        
# matrix=[
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [13,14,15,16]
# ]
# Solution().rotate(matrix)
# for i in matrix:
#     print(i)

# ##反转字符串
#     #不要给另外的数组分配额外的空间，你必须原地修改输入数组、
#     # 使用 O(1) 的额外空间解决这一问题
# s = ["h","e","l","l","o"]
# class Solution:
#     def reverseString(self, s: List[str]) :
#         if len(s) <= 1:
#             return 0
#         i,j = 0, len(s)-1
#         while i < len(s)/2:
#             s[i], s[j] = s[j], s[i]
#             i += 1
#             j -= 1

# Solution().reverseString(s)
# print(s)

##整数反转
    #给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
    # -123 -321 范围为 [−2^31,  2^31 − 1] 溢出那么就返回 0
# x = -123
# class Solution:
#     def reverse(self, x: int) :
#         temp,res = abs(x),0
#         while temp > 0:
#             res = res*10 + temp%10
#             if res < -(1<<31) or res > (1<<31)-1 :
#                 return 0
#             temp //= 10
#         return res if x > 0 else -res
# d = Solution().reverse(x)
# print(d)

# ##字符串中的第一个唯一字符
#     #s = "loveleetcode"  返回 2
# s = "loveleetcode"
# class Solution:
#     def firstUniqChar(self, s: str):
#         sc = collections.Counter(s)
#         for key, value in enumerate(s):
#             if sc[value] == 1:
#                 return key
#         return -1

# a = Solution().firstUniqChar(s)
# print(a)

# ##有效的字母异位词
#     #只包含小写字母,进阶:
#     #如果输入字符串包含 unicode 字符怎么办
# s = "anagram"
# t = "nagaram"
# class Solution:
#     def isAnagram(self, s: str, t: str) :
#         # #判断字符数是否相同
#         # if len(s) != len(t):
#         #     return False

#         # cs = collections.Counter(s)
#         # ct = collections.Counter(t)
#         # if cs == ct:
#         #     return True
#         # else:
#         #     return False

# ##验证回文串
#     #只考虑字母和数字字符，可以忽略字母的大小写.
#     #空字符定义为有效 True
# s = "A man, a plan, a canal: Panama"
# class Solution:
#     def isPalindrome(self, s: str):
#         t = ""
#         for i in s.lower():
#             if i.isalpha() or i.isdigit():
#                 t += i
#         i = 0
#         j = len(t) - 1 
#         while i < j:
#             if t[i] != t[j]:
#                 return False
#             i += 1
#             j -= 1
#         # print(t)        
#         return True

# print(Solution().isPalindrome(s))

# ##字符串转换整数 (atoi)
#     #第一个非空字符为正或者负号,尽可能多的连续数字字符组合有符号数
#     #第一个非空字符是数字，尽可能多的连续数字字符组合成整数
#     #第一个非空格字符不是一个有效整数字符不能进行有效的转换时，请返回 0
#     #数字 "-91283472332" 超过 32 位有符号整数范围。 因此返回 INT_MIN (−231)
# s = "+1"
# class Solution:
#     def myAtoi(self, s: str) :
#         #去掉手尾空字符
#         t = s.strip()
#         #如果第一个字符是空、不是数字、不是正负符号，返回0
#         if( not t) or not(t[0].isdigit() or t[0] == '-' or  t[0] == '+') :
#             return 0
#         #定义边界
#         INT_MAX=2**31-1
#         INT_MIN=-2**31
#         if t[0] == '-':
#             flag = -1
#         elif t[0] == '+':
#             flag = 0
#         else:
#             flag = 1
#         d = 0
#         #弹出整数d
#         for i in (t if flag > 0 else t[1:]): #t[1:] "1"
#             if not i.isdigit():
#                 print(i)
#                 break
#             d = d*10 + int(i)
#         #整数d变成符号数
#         if flag < 0:
#             d *= -1
#         #有符号数范围内
#         if d > INT_MIN and d < INT_MAX :
#             return d
#         #32位以外
#         return INT_MIN if d < 0 else INT_MAX
# # print(Solution().myAtoi(s))
# print((-1<<31)-1)

# ##实现strStr()
# #定一个 haystack 字符串和一个 needle 字符串， 
# #在 haystack 字符串中找出 needle 字符串出现的第一个位置 
# # (从0开始)。如果不存在，则返回  -1
# haystack = "hello"
# needle = "ll7"
# class Solution:
#     def strStr(self, haystack: str, needle: str) :
#         if not needle:
#             return 0
#         if len(needle) > len(haystack):
#             return -1
#         k = haystack.find(needle)
#         return k
# Solution().strStr(haystack, needle)

##外观数列
'''
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1 
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串
'''
# n >1 <30
k = 3
class Solution:# 迭代 从外到内 最后跳出return
    def countAndSay(self, n: int) :
        print(n)
        n -= 1
        if n < 0:
            return 0
        return self.countAndSay(n)
        
Solution().countAndSay(k)