from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        fpath1 = './files/testfile1.txt'
        fpath2 = './files/testfile2.txt'
        fpath3 = './files/testfile3.txt'
        solution(fpath1, fpath2, fpath3)

        with open(fpath3, 'r') as f:
            lines = f.readlines()

        self.assertEqual(lines[0], 'A for Apple.\n')
        self.assertEqual(lines[1], 'B for Ball.\n')