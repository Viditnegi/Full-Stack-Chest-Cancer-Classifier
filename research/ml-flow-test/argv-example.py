import sys


alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

print(alpha)
print(l1_ratio)


# python .\ml-flow-test\argv-example.py 0.9 0.3
#  prints 0.9 0.3

# python .\ml-flow-test\argv-example.py 
#  prints 0.5 0.5