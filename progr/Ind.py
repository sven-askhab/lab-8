#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = tuple(map(int, input().split()))

    for i, value in enumerate(A[:-2]):
        if A[i + 1] > A[i] and A[i + 1] > A[i + 2]:
            print("Номера элементов первой тройки:", i + 1, i + 2, i + 3)
            break
    else:
        print("Такой тройки не найдено.")