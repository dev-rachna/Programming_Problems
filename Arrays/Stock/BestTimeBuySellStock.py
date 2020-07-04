# -*- coding: utf-8 -*-

'''
leetcode 121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

'''

def maxProfit(prices):
    valley=float('inf')
    maxi=0
    for i in range(0,len(prices)):
        if prices[i]<valley:
            valley=prices[i]
        maxi=max(prices[i]-valley,maxi)
    return maxi
            