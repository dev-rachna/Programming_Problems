# -*- coding: utf-8 -*-

'''
leetcode 122. Best Time to Buy and Sell Stock II
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
'''

def maxProfit(prices):
    
    res=0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            res+=prices[i]-prices[i-1]
    return res

print(maxProfit([7,6,4,3,1]))