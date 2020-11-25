import unittest
import importlib
utils = importlib.import_module("utilities")
script = importlib.import_module("script")
'''
class testUS09(unittest.TestCase):

    def testBirthBeforeMotherDeath(self):
        #Test catch for birth before mother's death
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
        #Test catch for birth before father's death
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
        #Test catch for birth before mother's death
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
        #Test catch for birth before father's death
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
        #Test catch for birth before father's death 
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

class testUS23(unittest.TestCase):
    def testDuplicateBirthday(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")

        I1.birthday = "10 AUG 1979"
        I1.name = "Brandon"
        I2.birthday = "10 AUG 1979"
        I2.name = "Mike"

        listOfIndividuals = [I1, I2]
        output = utils.us23UniqueNameAndBirthDate(listOfIndividuals)
        self.assertEqual(output, ["10 AUG 1979"])


    def testDuplicateName(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")

        I1.birthday = "10 AUG 1978"
        I1.name = "Brandon"
        I2.birthday = "10 AUG 1979"
        I2.name = "Brandon"

        listOfIndividuals = [I1, I2]
        output = utils.us23UniqueNameAndBirthDate(listOfIndividuals)
        self.assertEqual(output, ["Brandon"])

    def testMultipleDuplicateBirthdays(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I1.birthday = "10 AUG 1979"
        I1.name = "Brandon"
        I2.birthday = "10 AUG 1979"
        I2.name = "Mike"
        I3.birthday = "10 AUG 1979"
        I3.name = "Jeremy"

        listOfIndividuals = [I1, I2, I3]
        output = utils.us23UniqueNameAndBirthDate(listOfIndividuals)
        self.assertEqual(output, ["10 AUG 1979", "10 AUG 1979"])
    def testMultipleDuplicateNames(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I1.birthday = "10 AUG 1977"
        I1.name = "Brandon"
        I2.birthday = "10 AUG 1978"
        I2.name = "Brandon"
        I3.birthday = "10 AUG 1979"
        I3.name = "Brandon"

        listOfIndividuals = [I1, I2, I3]
        output = utils.us23UniqueNameAndBirthDate(listOfIndividuals)
        self.assertEqual(output, ["Brandon", "Brandon"])
    def testDuplicateBirthdayAndName(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I1.birthday = "10 AUG 1979"
        I1.name = "Jake"
        I2.birthday = "10 AUG 1979"
        I2.name = "Brandon"
        I3.birthday = "10 AUG 1978"
        I3.name = "Brandon"

        listOfIndividuals = [I1, I2, I3]
        output = utils.us23UniqueNameAndBirthDate(listOfIndividuals)
        self.assertEqual(output, ["10 AUG 1979", "Brandon"])
    def testNoDupes(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")

        I1.birthday = "10 AUG 1978"
        I1.name = "Brandon"
        I2.birthday = "10 AUG 1979"
        I2.name = "Mike"

        listOfIndividuals = [I1, I2]
        output = utils.us23UniqueNameAndBirthDate(listOfIndividuals)
        self.assertEqual(output, [])'''
'''class testUS24(unittest.TestCase):
    def testDuplicateSpouseNamePairs(self):
        F1 = script.Family("F1")
        F2 = script.Family("F2")

        F1.husbName = "James"
        F1.wifeName = "Amanda"
        F1.married = "10 AUG 1979"

        F2.husbName = "James"
        F2.wifeName = "Amanda"
        F2.married = "9 AUG 1979"

        families = [F1, F2]
        output = utils.us24UniqueFamiliesBySpouses(families)
        self.assertEqual(output, [("James", "Amanda")])

    def testDuplicateMarriageDates(self):
        F1 = script.Family("F1")
        F2 = script.Family("F2")

        F1.husbName = "Jay"
        F1.wifeName = "Ariana"
        F1.married = "10 AUG 1979"

        F2.husbName = "James"
        F2.wifeName = "Amanda"
        F2.married = "10 AUG 1979"

        families = [F1, F2]
        output = utils.us24UniqueFamiliesBySpouses(families)
        self.assertEqual(output, ["10 AUG 1979"])

    def testDuplicateSpouseNamesAndMarriageDates(self):
        F1 = script.Family("F1")
        F2 = script.Family("F2")

        F1.husbName = "James"
        F1.wifeName = "Amanda"
        F1.married = "10 AUG 1979"

        F2.husbName = "James"
        F2.wifeName = "Amanda"
        F2.married = "10 AUG 1979"

        families = [F1, F2]
        output = utils.us24UniqueFamiliesBySpouses(families)
        self.assertEqual(output, [("James", "Amanda"), "10 AUG 1979"])'''

'''class testUS37(unittest.TestCase):
    def testDeadHusband(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I1.name = "James"
        I1.death = "4 OCT 2020"
        I1.alive = False

        I2.name = "Amanda"

        I3.name = "Brad"

        F1 = script.Family("F1")

        F1.husbName = "James"
        F1.husbId = "I1"
        F1.wifeName = "Amanda"
        F1.wifeId = "I2"
        F1.married = "10 AUG 1979"
        F1.children = [I3]
        families = [F1]
        individuals = [I1, I2, I3]
        output = utils.us37ListRecentSurvivors(individuals, families)
        self.assertEqual(output, [["Amanda", ["Brad"]]])

    def testDeadWife(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I1.name = "James"

        I2.name = "Amanda"
        I2.death = "1 NOV 2020"
        I2.alive = False

        I3.name = "Brad"

        F1 = script.Family("F1")

        F1.husbName = "James"
        F1.husbId = "I1"
        F1.wifeName = "Amanda"
        F1.wifeId = "I2"
        F1.married = "10 AUG 1979"
        F1.children = [I3]
        families = [F1]
        individuals = [I1, I2, I3]
        output = utils.us37ListRecentSurvivors(individuals, families)
        self.assertEqual(output, [["James", ["Brad"]]])

    def testMultipleSpouses(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")
        I4 = script.Individual("I4")

        I4.name = "Lauren"

        I1.name = "James"

        I2.name = "Amanda"
        I2.death = "1 NOV 2020"
        I2.alive = False

        I3.name = "Brad"

        F1 = script.Family("F1")

        F1.husbName = "James"
        F1.husbId = "I1"
        F1.wifeName = "Amanda"
        F1.wifeId = "I2"
        F1.married = "10 AUG 1979"
        F1.children = [I3]

        F2 = script.Family("F1")

        F2.husbName = "Lauren"
        F2.husbId = "I4"
        F2.wifeName = "Amanda"
        F2.wifeId = "I2"
        F2.married = "10 AUG 1969"
        F2.divorced = "10 AUG 1975"

        families = [F1, F2]
        individuals = [I1, I2, I3, I4]


        output = utils.us37ListRecentSurvivors(individuals, families)
        self.assertEqual(output, [["James", ["Brad"]], ['Lauren', []]])

    def testMultipleChildren(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")
        I4 = script.Individual("I4")

        I4.name = "Jon"

        I1.name = "James"

        I2.name = "Amanda"
        I2.death = "1 NOV 2020"
        I2.alive = False

        I3.name = "Brad"

        F1 = script.Family("F1")

        F1.husbName = "James"
        F1.husbId = "I1"
        F1.wifeName = "Amanda"
        F1.wifeId = "I2"
        F1.married = "10 AUG 1979"
        F1.children = [I3, I4]
        families = [F1]
        individuals = [I1, I2, I3, I4]
        output = utils.us37ListRecentSurvivors(individuals, families)
        self.assertEqual(output, [["James", ["Brad", "Jon"]]])

    def testMultipleChildrenWithDifferentSpouses(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")
        I4 = script.Individual("I4")
        I5 = script.Individual("I5")

        I5.name = "Jon"

        I4.name = "Lauren"

        I1.name = "James"

        I2.name = "Amanda"
        I2.death = "1 NOV 2020"
        I2.alive = False

        I3.name = "Brad"

        F1 = script.Family("F1")

        F1.husbName = "James"
        F1.husbId = "I1"
        F1.wifeName = "Amanda"
        F1.wifeId = "I2"
        F1.married = "10 AUG 1979"
        F1.children = [I3]

        F2 = script.Family("F1")

        F2.husbName = "Lauren"
        F2.husbId = "I4"
        F2.wifeName = "Amanda"
        F2.wifeId = "I2"
        F2.married = "10 AUG 1969"
        F2.divorced = "10 AUG 1975"
        F2.children = [I5]

        families = [F1, F2]
        individuals = [I1, I2, I3, I4, I5]


        output = utils.us37ListRecentSurvivors(individuals, families)
        self.assertEqual(output, [["James", ["Brad"]], ['Lauren', ["Jon"]]])'''
'''class testUS38(unittest.TestCase):
    def testUpcomingBirthday(self):
        I1 = script.Individual("I1")


        I1.birthday = "6 DEC 2020"
        I1.name = "James"

        individuals = [I1]
        output = utils.us38ListUpcomingBirthdays(individuals)
        self.assertEqual(output, ["James"])

    def testUpcomingBirthdays(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")

        I1.birthday = "6 DEC 2020"
        I1.name = "James"

        I2.birthday = "6 NOV 2020"
        I2.name = "Amanda"

        I3.birthday = "3 DEC 2020"
        I3.name = "Taylor"

        individuals = [I1, I2, I3]
        output = utils.us38ListUpcomingBirthdays(individuals)
        self.assertEqual(output, ["James", "Amanda", "Taylor"])
class testUS51And52(unittest.TestCase):
    def testMaleChild(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")

        I1.gender = "M"
        I1.name = "James"

        F1.children = [I1]
        individuals = [I1]
        families = [F1]
        output = utils.us51FamilyHasMaleChild(families, individuals)
        self.assertEqual(output, ["F1"])

    def testMultipleMaleChild(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        F1 = script.Family("F1")

        I1.gender = "M"
        I1.name = "James"
        I2.gender = "M"
        I2.name = "Arthur"

        F1.children = [I1, I2]
        individuals = [I1, I2]
        families = [F1]
        output = utils.us51FamilyHasMaleChild(families, individuals)
        self.assertEqual(output, ["F1"])

    def testMultipleFamiliesMaleChild(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        F1 = script.Family("F1")
        F2 = script.Family("F2")

        I1.gender = "M"
        I1.name = "James"
        I2.gender = "M"
        I2.name = "Arthur"

        F1.children = [I1]
        F2.children = [I2]
        individuals = [I1, I2]
        families = [F1, F2]
        output = utils.us51FamilyHasMaleChild(families, individuals)
        self.assertEqual(output, ["F1", "F2"])

    def testUS53(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")
        I4 = script.Individual("I4")
        I5 = script.Individual("I5")
        I6 = script.Individual("I6")
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F3 = script.Family("F3")
        F1.husbId = "I1"
        F1.wifeId = "I2"
        F2.husbId = "I3"
        F2.wifeId = "I4"
        F3.husbId = "I5"
        F3.wifeId = "I6"
        F1.married = "21 NOV 1985"
        F2.married = "8 NOV 2015"
        F1.divorced = "21 NOV 1994"
        F2.divorced = "8 NOV 2026"
        F3.married = "8 DEC 2015"
        F3.divorced = "8 DEC 2024"
        I1.name = "bobby"
        I2.name = "barbie"
        I3.name = "barney"
        I4.name = "bonnie"
        I5.name = "bartelby"
        I6.name = "bethany"
        output = utils.us52DivorcedInTenYears([F1, F2, F3], [I1, I2, I3, I4, I5, I6])
        self.assertEqual(output, [['I1', 'I2', 'F1'], ['I5', 'I6', 'F3']])'''

if __name__ == '__main__':
    unittest.main()