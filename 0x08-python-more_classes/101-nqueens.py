#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.
"""


def queen_exists(y, answers, n):
    """Does queen exist in y?"""
    for i in range(n):
        if y == answers[i][1]:
            return True
    return False


def reject_solution(x, y, answers, n):
    """Accept or reject solution"""
    if (queen_exists(y, answers, n)):
        return False

    for i in range(x):
        if abs(answers[i][1] - y) == abs(i - x):
            return False
    return True


def clear_answer(x, answers, n):
    """Clears all answers"""
    for i in range(x, n):
        answers[i][1] = None


def n_queens(x, answers, n):
    """Find solution through recursive backtracking"""
    for y in range(n):
        clear_answer(x, answers, n)
        if reject_solution(x, y, answers, n):
            answers[x][1] = y
            if (x == n - 1):  # agree to the solution
                print(answers)
            else:
                n_queens(x + 1, answers, n)  # skip to next x value to continue


def main():
    """Main function - code starts here"""
    answers = []

    if (len(sys.argv) != 2):
        print("Usage: n_queens N")
        exit(1)
    if (sys.argv[1].isdigit() is False):
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if (n < 4):
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        answers.append([i, None])

    n_queens(0, answers, n)


if __name__ == "__main__":
    import sys
    main()
