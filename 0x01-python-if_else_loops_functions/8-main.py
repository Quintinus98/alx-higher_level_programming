#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")

add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")
