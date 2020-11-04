from  typing  import List
import collections
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

## 旋转图像 原地顺时针旋转 90 度
    #旋转二维数组 直接修改输入的矩阵
class Solution:
    def rotate(self, matrix: List[List[int]]):
        
matrix=[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
]

Solution().rotate(matrix)
for i in matrix:
    print(i)







    
