import unittest
import importlib
script = importlib.import_module("script")
utilities = importlib.import_module("utilities")

class us11NoBigamy(unittest.TestCase):

    '''
    five tests:
    Output for cases of bigamy with no deaths or divorces
    Output for death of spouse of person engaged in bigamy
    Output for multiple cases of bigamy
    No output for valid second marriages
    no output for empty input
    '''
    def testNoDeathOrDivorce(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F1.husbId = "I1"
        F1.wifeId = "I2"
        F2.husbId = "I1"
        F2.wifeId = "I3"
        F1.married = "1 NOV 1985"
        F2.married = "2 NOV 2015"
        output = utilities.us11NoBigamy([F1,F2], [I1, I2, I3])
        self.assertEqual(output, ['I1', 'I3', 'I2', 'F2', 'F1'])

    def testDeathDuringBigamy(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F1.husbId = "I1"
        F1.wifeId = "I2"
        F2.husbId = "I1"
        F2.wifeId = "I3"
        F1.married = "1 NOV 1985"
        F2.married = "2 NOV 2005"
        I2.death = "2 JAN 2010"
        output = utilities.us11NoBigamy([F1,F2], [I1, I2, I3])
        self.assertEqual(output, ['I1', 'I3', 'I2', 'F2', 'F1'])

    def testMultipleErrors(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")
        I4 = script.Individual("I4")
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F3 = script.Family("F3")
        F1.husbId = "I2"
        F1.wifeId = "I1"
        F2.husbId = "I3"
        F2.wifeId = "I1"
        F3.husbId = "I2"
        F3.wifeId = "I4"
        F1.married = "1 NOV 1985"
        F2.married = "2 NOV 2015"
        F3.married = "3 APR 1990"
        output = utilities.us11NoBigamy([F1, F2, F3], [I1, I2, I3, I4])
        self.assertEqual(output, ['I1', 'I3', 'I2', 'F2', 'F1', 'I2', 'I4', 'I1', 'F3', 'F1'])

    def testOneDeath(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F1.husbId = "I1"
        F1.wifeId = "I2"
        F2.husbId = "I1"
        F2.wifeId = "I3"
        F1.married = "1 NOV 1985"
        F2.married = "2 NOV 2015"
        I2.death = "2 JAN 2010"
        output = utilities.us11NoBigamy([F1,F2], [I1, I2, I3])
        self.assertEqual(output, [])

    def testEmptyList(self):
        output = utilities.us11NoBigamy([], [])
        self.assertEqual(output, [])

    # def testParentsNotTooOld(self):
    #     I1 = script.Individual("I1")
    #     I2 = script.Individual("I2")
    #     I3 = script.Individual("I3")
    #     I4 = script.Individual("I4")
    #     I5 = script.Individual("I5")
    #     F1 = script.Family("F1")
    #     F2 = script.Family("F2")
    #     F1.husbId = "I1"
    #     F1.wifeId = "I2"
    #     F1.children = ["I4"]
    #     F2.husbId = "I1"
    #     F2.wifeId = "I3"
    #     F2.children = ["I4", "I5"]
    #     I1.birthday = "1 NOV 1985"
    #     I2.birthday = "2 NOV 2005"
    #     I3.birthday = "1 NOV 1945"
    #     I4.birthday = "2 NOV 2015"
    #     I5.birthday = "1 NOV 2019"
    #     output = utilities.us12ParentsNotTooOld([F1, F2], [I1, I2, I3, I4, I5])
    #     self.assertEqual(output, ['I3', 'I4', 'F2', 'I3', 'I5', 'F2'])


if __name__ == '__main__':
    unittest.main()
