import unittest
import importlib
script = importlib.import_module("script")
utilities = importlib.import_module("utilities")

class us07AgeOver150(unittest.TestCase):

    '''
    five tests:
    No output for individuals with birthdays less than 150 years ago
    Output for individual that has birthday more than 150 years ago
    Output for multiple individuals that have birthday more than 150 years
    No output for empty list of individuals
    no output for list of individuals with no ages specified
    '''
    def testIndiUnder150(self):
        I1 = script.Individual("I1")
        I1.age = 45
        output = utilities.us07AgeOver150([I1])
        self.assertEqual(output, [])

    def testIndiOver150(self):
        I1 = script.Individual("I1")
        I1.age = 160
        output = utilities.us07AgeOver150([I1])
        self.assertEqual(len(output), 1)

    def testMultipleIndiOver150(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I1.age = 165
        I2.age = 189
        output = utilities.us07AgeOver150([I1, I2])
        self.assertEqual(len(output), 2)

    def testEmptyList(self):
        output = utilities.us07AgeOver150([])
        self.assertEqual(output, [])

    def testIndiNoAge(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        output = utilities.us07AgeOver150([I1, I2])
        self.assertEqual(output, [])
   

if __name__ == '__main__':
    unittest.main()