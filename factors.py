#!/usr/bin/python3
import sys
import math

def factorize(n):
    for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return i, n
    return n, 1


def main(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factor1, factor2 = factorize(number)
            print(f"{number}={factor1}*{factor2}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
