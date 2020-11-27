# miriam podkolzin HW 04

import unittest
import importlib
script = importlib.import_module("script")
utilities = importlib.import_module("utilities")

class us02BirthBeforeMarriage(unittest.TestCase):
    
    '''
    five tests:
    No output for inidividuals with no marriage before birth
    Output for individual that has marriage before born
    Output for multiple individuals that have marriages before born
    no output for an empty individuals list
    '''

    def testNoMarraigeIndividual(self):
        I1 = script.Individual("I1")
        I1.birthday = "1 NOV 1990"
        F1 = script.Family("F1")
        F1.marriage = " "
        output = utilities.us02BirthBeforeMarriage([I1], [F1])
        self.assertEqual(output, [])

    def testSingleInvalid(self):
        I1 = script.Individual("I1")
        I1.birthday = "1 NOV 1997"
        F1 = script.Family("F1")
        F1.marriage = "9 JAN 1985"
        output = utilities.us02BirthBeforeMarriage([I1], [F1])
        self.assertEqual(len(output), 0)

    def testMultipleInvalidMarriageBeforeBirth(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F1.marriage = "1 NOV 1985"
        F2. marriage = "2 NOV 2015"
        I1.birthday = "2 FEB 2020"
        I2.birthday = "2 OCT 2020"
        output = utilities.us02BirthBeforeMarriage([I1, I2], [F1,F2])
        self.assertEqual(output, [])

    def testValidIndividualMarriages(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F1.marriage = "1 NOV 1985"
        F2. marriage = "2 NOV 2015"
        I1.birthday = "2 FEB 1927"
        I2.birthday = "2 OCT 1978"
        output = utilities.us02BirthBeforeMarriage([I1, I2], [F1,F2])
        self.assertEqual(output, [])

    def testEmptyList(self):
        output = utilities.us02BirthBeforeMarriage([],[])
        self.assertEqual(output, [])
    
    def testOldestFamilyMembers(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        I1.age = "31"
        I2.age = "25"
        output = utilities.us43oldestFamilyMembers([I1, I2], [F1,F2])
        self.assertEqual(output,[])
    
    def testYoungestFamilyMembers(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        I1.age = "31"
        I2.age = "25"
        output = utilities.us43YoungestFamilyMembers([I1, I2], [F1,F2])
        self.assertEqual(output,[])

if __name__ == '__main__':
    unittest.main()
