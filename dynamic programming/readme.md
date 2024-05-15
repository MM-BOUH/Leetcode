# Dynamic Programming Exercises

Dynamic programming (DP) is a powerful technique used in computer science to solve problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant computations. DP is particularly useful for optimization problems where you need to find the best solution among many possible solutions.

This repository contains a set of dynamic programming exercises from LeetCode to help you prepare for coding interviews. The problems range from simple to medium difficulty and cover various aspects of DP.

## Table of Contents
1. [Understanding Dynamic Programming](#understanding-dynamic-programming)
2. [Exercises](#exercises)

## Understanding Dynamic Programming

### What is Dynamic Programming?

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable when the problem can be divided into overlapping subproblems which can be solved independently. DP is generally used to optimize recursive algorithms by storing intermediate results in a table (memoization) or by building a solution iteratively (tabulation).

### Key Concepts

1. **Optimal Substructure:**  
   The optimal solution to the problem can be constructed from optimal solutions to its subproblems.

2. **Overlapping Subproblems:**  
   The problem can be broken down into subproblems which are reused multiple times.

### Types of Dynamic Programming Approaches

1. **Memoization (Top-Down):**  
   - Involves solving the problem recursively and storing the results of subproblems in a table to avoid redundant computations.
   - Useful when the problem can naturally be divided into subproblems and there are many overlapping subproblems.

2. **Tabulation (Bottom-Up):**  
   - Involves solving the problem iteratively by building up a table from the base cases to the final solution.
   - Useful when the problem can be solved by iteratively combining solutions to smaller subproblems.

### Example Problem: House Robber

Let's consider the "House Robber" problem:

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

**Solution using Dynamic Programming:**

1. **Define the state:**  
   Let `dp[i]` be the maximum amount of money you can rob from the first `i` houses.

2. **State transition:**  
   To determine the maximum amount of money you can rob from the first `i` houses, you have two options:
   - Do not rob the `i-th` house, so the total amount is `dp[i-1]`.
   - Rob the `i-th` house, so the total amount is `nums[i] + dp[i-2]` (since you cannot rob two adjacent houses).

   Therefore, the recurrence relation is:
   \[
   dp[i] = \max(dp[i-1], nums[i] + dp[i-2])
   \]

3. **Base cases:**
   - `dp[0] = nums[0]` (Only one house to rob)
   - `dp[1] = \max(nums[0], nums[1])` (Choose the maximum of robbing the first or the second house)

By applying this approach, you can solve the problem efficiently.

## Exercises

Here are some dynamic programming exercises to practice:

1. [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
2. [House Robber](https://leetcode.com/problems/house-robber/)
3. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
4. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
5. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
6. [Unique Paths](https://leetcode.com/problems/unique-paths/)

These problems will help you build a solid understanding of dynamic programming concepts. Good luck with your preparation!
