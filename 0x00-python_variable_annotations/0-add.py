#!/usr/bin/env python3
"""Module that contains a single function that adds two integers."""
def add(a: float, b: float) -> float:
	""" Add two integers together."""
	sum = a+b
	return sum

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

