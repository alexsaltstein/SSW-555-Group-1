import unittest
import importlib
script = importlib.import_module("script")
utilities = importlib.import_module("utilities")

class us03DeathBeforeBirthTests(unittest.TestCase):

    '''
    five tests:
    No output for inidividuals with no deaths
    Output for individual that has death before born
    Output for multiple individuals that have death before born
    No output for individuals that have death
    no output for an empty individuals list
    '''
    def testNoDeathsIndividuals(self):
        I1 = script.Individual("I1")
        output = utilities.us03DeathBeforeBirth([I1])
        self.assertEqual(output, [])

    def testSingleInvalidDeath(self):
        output = utilities.us03DeathBeforeBirth(script.individuals)
        self.assertEqual(len(output), 1)

    def testMultipleInvalidDeaths(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I1.death = "2 JAN 2017"
        I2.death = "2 JAN 2019"
        I1.birthday = "2 FEB 2020"
        I2.birthday = "2 OCT 2021"
        output = utilities.us03DeathBeforeBirth([I1, I2])
        self.assertEqual(len(output), 2)

    def testValidIndividualDeaths(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I1.death = "2 JAN 2017"
        I2.death = "2 JAN 2019"
        I1.birthday = "2 FEB 1927"
        I2.birthday = "2 OCT 1978"
        output = utilities.us03DeathBeforeBirth([I1, I2])
        self.assertEqual(output, [])

    def testEmptyList(self):
        output = utilities.us03DeathBeforeBirth([])
        self.assertEqual(output, [])
    

if __name__ == '__main__':
    unittest.main()
