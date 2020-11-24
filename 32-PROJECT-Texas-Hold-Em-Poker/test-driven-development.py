import unittest

# def product(a, b):
#    return a * b 

# class TestProduct(unittest.TestCase):
#     def test_multiple_two_numbers_together(self):
#         self.assertEqual(
#             product(3, 5),
        #     15
        # )

    

class CardTest(unittest.TestCase):
    def test_setup(self):
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()