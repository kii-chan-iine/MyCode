'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

不理解！！！
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next



# 定义一个链表节点
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 这里为大家补充了创建链表的函数
def create_list(nums):
    last = None
    for num in reversed(nums):
        list_node = ListNode(num)
        list_node.next = last
        last = list_node
    return last


list1=[2,3,4]
list2=[5,6,4]

l1 = create_list(list1)
l2=create_list(list2)



s=Solution()
ss=s.addTwoNumbers(l1,l2)


# 打印
def printNode(node):
    while node:
        print ( ' value: ', node.val, ' next: ', node.next)
        node = node.next

printNode(ss)
#%%

# 　　# 翻转
#     def reverse(self,nodelist):
#         list = []
#         while nodelist:
#             list.append(nodelist.val)
#             nodelist = nodelist.next
#         result = Node()
#         result_handle =Node_handle()
#         for i in list:
#             result = result_handle.add(i)
#         return result