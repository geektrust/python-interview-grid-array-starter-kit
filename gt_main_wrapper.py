import sys
from solution import Solution


def main():
    """
    *****************************************************************************
    DO NOT EDIT THIS CODE.
    *****************************************************************************

    This code is used to bootstrap your solution to be checked for correctness by
    our system.

    This is the main entry point for the program. It will parse the input for you.
    You don't need to change this.
    """
    if len(sys.argv) < 2:
        raise ValueError("No command line arguments passed")

    input_str = sys.argv[1]
    rows = input_str.split("|")
    grid = [list(map(int, row.split(","))) for row in rows]

    solution = Solution()
    output = solution.handle(grid)
    print(output)


if __name__ == "__main__":
    main()
