#!/usr/bin/python3
"""Defining the nQueens Module to solve the N Queens puzzle
The challenge is of placing N non-attacking queens on an N×N chessboard
"""


class nQueens:
    """Class nQueens problem solver
    Args:
        n (int): number of queens and size of chessboard (N×N)

    Attributes:
        n (int, private): number of queens and size of chessboard (N×N)
        state (list, private): state of the board to test for solutions.
            Has a size of n.
        solutions (list, public): list of solutions/states for the puzzle.
            Satisfies conditions:
                Every queen must not share a row, column,
                or diagonal with any other queen.

    Methods:
        n (Public): property setter and getter.
        state (Public): property setter and getter.
        check_solution (staticmethod): tests if state, row and columns meet
            the solution criteria where:
                Every queen must not share a row, column, or
                diagonal with any other queen.

        solve_n_queens (Public): Instance method for solving the problem
            Methods:
                backtrack (static method): recursive algorithm that implements
                backtracking to check the solution and eliminate non solutions
        print_solution (Public): Instance method that prints the solutions

    """
    def __init__(self, n):
        """class private instance method: constructor.
        """
        self.n = n
        self.state = self.n
        self.solutions = []
        self.solve_n_queens()

    @property
    def n(self):
        """n property getter."""
        return self.__n

    @n.setter
    def n(self, value):
        """n property setter."""
        if not value.isdigit():
            print("N must be a number")
            exit(1)
        elif int(value) < 4:
            print("N must be at least 4")
            exit(1)
        self.__n = int(value)

    @property
    def state(self):
        """state property getter."""
        return self.__state

    @state.setter
    def state(self, n):
        """state property setter."""
        self.__state = [0] * n

    @staticmethod
    def check_solution(state, row, col):
        """static method that tests if state, row and columns meet
            the solution criteria where:
                Every queen must not share a row, column, or
                diagonal with any other queen.
        """
        for i in range(row):
            if state[i] == col or \
               state[i] - i == col - row or \
               state[i] + i == col + row:
                return False
        return True

    def solve_n_queens(self):
        """solve_n_queens (Public): Instance method for solving the problem"""

        @staticmethod
        def backtrack(row):
            """static method that recursively implements backtracking algorithm
                    to check the solution and eliminate non solutions"""

            if row == self.n:
                self.solutions.append(self.state[:])
                return
            for col in range(self.n):
                if self.check_solution(self.state, row, col):
                    self.state[row] = col
                    backtrack(row + 1)
                    self.state[row] = 0
        self.solutions = []
        self.state = self.n
        backtrack(0)

    def print_solution(self):
        """Instance method that prints the solutions if found"""
        if not self.solutions:
            return
        res = self.solutions.copy()
        x = []
        for s, sol in enumerate(res):
            x.append([])
            for r, _ in enumerate(sol):
                x[s].append([r, _])
            # print(x[s])
        for _ in x:
            print(_)
        # return str(x)


if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        value = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if value < 4:
        print("N must be at least 4")
        exit(1)

    nQueens(argv[1]).print_solution()
