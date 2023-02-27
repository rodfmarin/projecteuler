"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
    """
    Get the sum of all the multiples of 3 or 5 under n
    """
    multiples = []
    for i, n in enumerate(range(2, 1000)):
        if n % 3 == 0 or n % 5 == 0:
            multiples.append(n)

    print(multiples)
    print(sum(multiples))


if __name__ == "__main__":
    main()
