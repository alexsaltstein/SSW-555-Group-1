import unittest
import importlib
utils = importlib.import_module("utilities")
script = importlib.import_module("script")

class testUS09(unittest.TestCase):

    def testBirthBeforeMotherDeath(self):
        '''Test catch for birth before mother's death'''
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I1.death = "7 AUG 1970"
        I1.alive = False
        I3.birthday = "8 AUG 1970"
        F1 = script.Family("F1")
        F1.husbId = "I2"
        F1.wifeId = "I1"
        F1.children = ["I3"]
        listOfFamilies = [F1]
        listOfIndividuals = [I1, I2, I3]
        output = utils.us09BirthBeforeDeathOfParents(listOfFamilies, listOfIndividuals)
        self.assertEqual(output, ["I3"])

    def testBirthBeforeFatherDeath(self):
        '''Test catch for birth before father's death'''
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I2.death = "9 JAN 1970"
        I2.alive = False
        I3.birthday = "10 OCT 1970"
        F1 = script.Family("F1")
        F1.husbId = "I2"
        F1.wifeId = "I1"
        F1.children = ["I3"]
        listOfFamilies = [F1]
        listOfIndividuals = [I1, I2, I3]
        output = utils.us09BirthBeforeDeathOfParents(listOfFamilies, listOfIndividuals)
        self.assertEqual(output, ["I3"])

    def testBirthBeforeBothParentDeaths(self):
        '''Test catch for birth before mother's death'''
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I2.death = "9 JAN 1970"
        I2.alive = False
        I1.death = "9 OCT 1970"
        I2.alive = False
        I3.birthday = "10 OCT 1970"
        F1 = script.Family("F1")
        F1.husbId = "I2"
        F1.wifeId = "I1"
        F1.children = ["I3"]
        listOfFamilies = [F1]
        listOfIndividuals = [I1, I2, I3]
        output = utils.us09BirthBeforeDeathOfParents(listOfFamilies, listOfIndividuals)
        self.assertEqual(output, ["I3"])

    def testMultipleFamiliesWithBirthBeforeDeathOfParents(self):
        '''Test catch for birth before father's death'''
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I4 = script.Individual("I4")
        I5 = script.Individual("I5")
        I6 = script.Individual("I6")

        I2.death = "9 JAN 1970"
        I2.alive = False
        I3.birthday = "10 OCT 1970"
        F1 = script.Family("F1")
        F1.husbId = "I2"
        F1.wifeId = "I1"
        F1.children = ["I3"]

        I5.death = "9 OCT 1970"
        I5.alive = False
        I6.birthday = "10 OCT 1970"
        F2 = script.Family("F2")
        F2.husbId = "I4"
        F2.wifeId = "I5"
        F2.children = ["I6"]

        listOfFamilies = [F1, F2]
        listOfIndividuals = [I1, I2, I3, I4, I5, I6]
        output = utils.us09BirthBeforeDeathOfParents(listOfFamilies, listOfIndividuals)
        self.assertEqual(output, ["I3", "I6"])

    def testNoBirthBeforeDeathOfParents(self):
        '''Test catch for birth before father's death'''
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I4 = script.Individual("I4")
        I5 = script.Individual("I5")
        I6 = script.Individual("I6")

        I2.death = "11 JAN 1970"
        I2.alive = False
        I3.birthday = "10 OCT 1970"
        F1 = script.Family("F1")
        F1.husbId = "I2"
        F1.wifeId = "I1"
        F1.children = ["I3"]

        I5.death = "11 OCT 1970"
        I5.alive = False
        I6.birthday = "10 OCT 1970"
        F2 = script.Family("F2")
        F2.husbId = "I4"
        F2.wifeId = "I5"
        F2.children = ["I6"]

        listOfFamilies = [F1, F2]
        listOfIndividuals = [I1, I2, I3, I4, I5, I6]
        output = utils.us09BirthBeforeDeathOfParents(listOfFamilies, listOfIndividuals)
        self.assertEqual(output, [])

class testUS10(unittest.TestCase):
    def test01(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")

        I1.birthday = "10 AUG 1979"
        I2.birthday = "11 AUG 1974"

        F1 = script.Family("F1")
        F1.husbId = "I1"
        F1.wifeId = "I2"
        F1.married = "9 AUG 1992"   #1993 doesnt work, but anything before that year does. Is this preferred behavior?

        listOfFamilies = [F1]
        listOfIndividuals = [I1, I2]
        output = utils.us10MarriageAfter14(listOfFamilies, listOfIndividuals)
        self.assertEqual(output, ["I1"])

if __name__ == '__main__':
    unittest.main()