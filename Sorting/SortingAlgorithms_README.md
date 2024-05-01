
# Sorting Algorithms Overview

This document provides a brief overview of several common sorting algorithms, highlighting their characteristics and the algorithmic paradigm they often share.

## Algorithms Covered

### Selection Sort
- **Selection Sort** is an in-place comparison sorting algorithm. It repeatedly selects the smallest element from the unsorted segment and moves it to the end of the sorted segment.

### Insertion Sort
- **Insertion Sort** builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

### Merge Sort
- **Merge Sort** is a divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

### Quicksort
- **Quicksort** is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quicksort that pick pivot in different ways.

## Common Algorithmic Paradigm: Divide-and-Conquer
Both merge sort and quicksort employ a common algorithmic paradigm based on recursion. This paradigm, known as **divide-and-conquer**, breaks a problem into subproblems that are similar to the original problem, recursively solves the subproblems, and finally combines the solutions to the subproblems to solve the original problem.

This approach is particularly powerful in cases where the problem can be naturally divided into independent subproblems and is a cornerstone of many efficient algorithms beyond just sorting.

