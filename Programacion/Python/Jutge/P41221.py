import sys

numbers=list(map(int, sys.stdin.read().split()))
if len(numbers)==3:
    print(sum(numbers))