import unittest


def run_all_unit_tests():
    """Runs all unit tests in the "tests" directory and all its subdirectories

    Requirements:
    - Test Files Name must match "test*.py"
    - Test Case Classes Must Extend unittest.TestCase
    - All Test Functions Name must match "test_*"
    """
    testsuite = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=1).run(testsuite)


if __name__ == '__main__':
    run_all_unit_tests()
