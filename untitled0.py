# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:27:59 2020

@author: BANANICE
"""

#coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:return
        #取出链表中的数字存入数组
        arr1,arr2=[],[]       
        while l1:
            arr1.append(l1.val)    
            l1 = l1.next
        while l2:
            arr2.append(l2.val)    
            l2 = l2.next 
        #倒序
        arr1.reverse()
        arr2.reverse()
        #print (arr1,arr2)
        #组成数字
        num1,num2 = 0,0
        for i in arr1:
            num1 = num1*10+i
        for i in arr2:
            num2 = num2*10+i        
        print (num1,num2)
        #相加
        num_total = num1+num2
        print (num_total)
        #从低位到高位写入链表，初始化链表的根节点为0，如果相加的和为0，直接返回
        l_res = ListNode(0)
        cursor = l_res
        if num_total == 0: return l_res
        while num_total:
            temp = num_total%10
            print (temp)
            cursor.next = ListNode(temp)
            cursor = cursor.next
            num_total = int(num_total/10)
            #print (num_total)
        return l_res.next
            
        
if __name__=='__main__':
    #创建l1和l2两个链表，注意，排序好的就需要arr1和arr2中数字从小到大
    arr1 = [0,8,6,5,6,8,3,5,7]
    arr2 = [6,7,8,0,8,5,8,9,7]
    l1 = ListNode(arr1[0])
    p1 = l1
    l2 = ListNode(arr2[0])
    p2 = l2
    for i in arr1[1:]:
        p1.next = ListNode(i)
        p1 = p1.next
    for i in arr2[1:]:
        p2.next = ListNode(i)
        p2 = p2.next    
    s=Solution()
    #两个链表相加
    q=s.addTwoNumbers(l1,l2)