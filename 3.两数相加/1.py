# 解法模板 超时
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         #1. 两表为空的情况下
#         if l1 == None:
#             return l2
#         if l2 == None:
#             return l1
#         # 创建一个空表 储存结果
#         result = ListNode(0)
#         p = result
#         # 进位
#         carry = 0
#         #2. 两个表位数相同
#         while l1 and l2:
#             # 取余
#             p.next=ListNode((l1.val+l2.val+carry)%10)
#             # 取整
#             carry = (l1.val+l2.val+carry)//10
#             l1 = l1.next
#             l2 = l2.next
#             p = p.next
#         #3. 两表长度不同
#         if l1:
#             while l1:
#                 p.next=ListNode((l1.val+carry)%10)
#                 carry = ((l1.val+carry)//10)
#                 l1.next
#                 p = p.next
#         if l2:
#             while l2:
#                 p.next=ListNode((l2.val+carry)%10)
#                 carry = ((l2.val+carry)//10)
#                 l2.next
#                 p = p.next

#         #4. 最后还有进位
#         if carry == 1:
#             p.next=ListNode(1)

#         return result.next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 结果存储
        result = ListNode(0)
        # 指针
        p = result
        # 进位
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            p.next = ListNode((carry + x + y) % 10)
            carry = (carry + x + y) // 10
            p = p.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        if (carry > 0):
            p.next = ListNode(1)
        return result.next