import unittest
import importlib
script = importlib.import_module("script")
utilities = importlib.import_module("utilities")


'''
This file contains 5 tests:
    
No output for individuals with empty marriage
Output for individual that has marriage after death
No output for individual who has marriage before death
Output for Invalid Marriage After Death
No output for empty list of individuals and families

'''



class us05MarriageBeforeDeath(unittest.TestCase): 
   
    
    def testNoMarriageIndividualsEmptyString(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        F1.married = " "
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(output, [])
    def testNoMarriageIndividualsNA(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        F1.married = "NA"
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(output, [])
    def testSingleValidMarriageBeforeDeath(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        I1.death = "2 JAN 2019"
        F1.married = "2 JAN 2017"
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(len(output), 0) 
    def testSingleInvalidMarriageBeforeDeath(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        F1 = script.Family("F3")
        F1.husbId = "I1"
        F1.wifeId = "I2"
        I1.death = "2 JAN 2017"
        I2.death = "NA"
        F1.married = "2 JAN 2019"
        output = utilities.us05MarriageBeforeDeath([F1], [I1, I2])
        self.assertEqual(len(output), 0)
    def testEmptyList(self):
        output = utilities.us05MarriageBeforeDeath([], [])
        self.assertEqual(output, [])

class us06DivorceeBeforeDeath(unittest.TestCase): 
   
    
    def testNoDivorceIndividualsEmptyString(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        F1.divorced = " "
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(output, [])
    def testNoDivorceIndividualsNA(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        F1.divorced = "NA"
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(output, [])
    def testSingleValidMarriageBeforeDeath(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        I1.death = "2 JAN 2019"
        F1.divorced = "2 JAN 2017"
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(len(output), 0) 
    def testSingleInvalidMarriageBeforeDeath(self):
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        F1 = script.Family("F3")
        F1.husbId = "I1"
        F1.wifeId = "I2"
        I1.death = "2 JAN 2017"
        I2.death = "NA"
        F1.divorced = "2 JAN 2019"
        output = utilities.us05MarriageBeforeDeath([F1], [I1, I2])
        self.assertEqual(len(output), 0)
    def testEmptyList(self):
        output = utilities.us05MarriageBeforeDeath([], [])
        self.assertEqual(output, [])


class us19FirstCousinsShouldNotMarry(unittest.TestCase):
    def testMarriedCousins(self):
        #I1 is cousin 1
        I1 = script.Individual("I1")
        #F2 is family of cousin
        F1 = script.Family("F1")
        #Assign cousin to F2 as child
        I1.child = "F1"
        # I3 is mother of I1
        I2 = script.Individual("I2")
        # Assign I2 to F1 as Mother
        F1.wifeId = "I2"
        # Assign Mother to F2 as child
        F2 = script.Family("F2")
        I2.child = "F2"
        
        #I3 is cousin 2
        I3 = script.Individual("I2")
        F3 = script.Family("F3")
        I3.child = script.Family("F3")
        I4 = script.Individual("I4")
        # Assign I4 to F3 as Mother
        F3.wifeId = "I4"
        # Assign I4 to same family as I2 making them siblings
        I4.child = "F2"
        
        F2.children = ['I2', 'I4']
        
        F4 = script.Family("F4")
        F4.husbId = "I1"
        F4.wifeId = "I3"
        I1.spouse = "I3"
        I3.spouse = "I1"
        F4.married = "2 JAN 2017"
        
        I5 = script.Individual("I5")
        F1.husbId = "I5"
        
        I6 = script.Individual("I6")
        F3.husbId = "I5"
        
        families = [F1, F2, F3, F4]
        individuals = [I1, I2, I3, I4, I5, I6]
        output = utilities.us19FirstCousinsShouldNotMarry(families, individuals)
        self.assertEqual(output, [])
    
    def testNoMarriageIndividualsEmptyString(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        F1.married = " "
        output = utilities.us19FirstCousinsShouldNotMarry([F1], [I1])
        self.assertEqual(output, [])
    
    def testNoMarriageIndividualsNA(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        F1.married = "NA"
        output = utilities.us19FirstCousinsShouldNotMarry([F1], [I1])
        self.assertEqual(output, [])
    
    def testEmptyList(self):
        output = utilities.us19FirstCousinsShouldNotMarry([], [])
        self.assertEqual(output, [])

class us20AuntsandUncles(unittest.TestCase):
    
    def testNoMarriageIndividualsEmptyString(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        F1.married = " "
        output = utilities.us20AuntsandUncles([F1], [I1])
        self.assertEqual(output, [])
        
    def testNoMarriageIndividualsNA(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        F1.married = "NA"
        output = utilities.us20AuntsandUncless([F1], [I1])
        self.assertEqual(output, [])
    
    def testEmptyList(self):
        output = utilities.us20AuntsandUncles([], [])
        self.assertEqual(output, [])
        
class us33OrphanedChildren(unittest.TestCase): 
    def testOrphanedChild(self):
        F1 = script.Family("F1")
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        I3 = script.Individual("I3")
        F1.husbId = "I1"
        F1.wifeId = "I2"
        F1.children = ["I3"]
        I1.birthday = "7 JUL 1970"
        I2.birthday = "7 NOV 1970"
        I3.birthday = "3 JUL 2015"
        I1.death = "7 JUL 2017"
        I2.death = "7 JUL 2018"
        I3.death = "NA"
        output = utilities.us33OrphanedChildren([F1], [I1, I2, I3])
        self.assertEqual(output, ["I3"])
        
    def testEmptyList(self):
        output = utilities.us33OrphanedChildren([], [])
        self.assertEqual(output, [])


class us34LargeAgeDifferences(unittest.TestCase): 
   
    def testLargeAge(self):
        F1 = script.Family("F1")
        I1 = script.Individual("I1")
        I2 = script.Individual("I2")
        F1.married = "2 JAN 2017"
        F1.husbId = "I1"
        F1.wifeId = "I2"
        I1.spouse = "I2"
        I2.spouse = "I1"
        I1.birthday = "7 JUL 1970"
        I2.birthday = "8 NOV 1999"
        output = utilities.us34LargeAgeDifferences([F1], [I1,I2])
        self.assertEqual(output, ["F1"])
  
    def testEmptyList(self):
        output = utilities.us34LargeAgeDifferences([], [])
        self.assertEqual(output, [])
        
class us47MostRecentMarriage(unittest.TestCase): 
   
    def testMostRecent(self):
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F3 = script.Family("F3")
        F4 = script.Family("F4")
        F5 = script.Family("F5")
        F1.married = "8 NOV 1990"
        F2.married = "8 NOV 1980"
        F3.married = "8 NOV 1970"
        F4.married = "8 NOV 2020"
        F5.married = "8 NOV 2010"
        output = utilities.us47MostRecentMarriage([F1, F2, F3, F4, F5])
        self.assertEqual(output, ["F4"])
    
    def testNA(self):
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F1.married = "NA"
        F2.married = "8 NOV 1980"
        output = utilities.us47MostRecentMarriage([F1, F2])
        self.assertEqual(output, ["F2"])
    
    def testEmptyStringMarriage(self):
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F1.married = " "
        F2.married = "8 NOV 1980"
        output = utilities.us47MostRecentMarriage([F1, F2])
        self.assertEqual(output, ["F2"]) 
        
    def testEmptyList(self):
        output = utilities.us47MostRecentMarriage([])
        self.assertEqual(output, [])

class us48MostRecentDivorce(unittest.TestCase): 
   
    def testMostRecent(self):
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F3 = script.Family("F3")
        F4 = script.Family("F4")
        F5 = script.Family("F5")
        F1.divorced = "8 NOV 1990"
        F2.divorced = "8 NOV 1980"
        F3.divorced = "8 NOV 1970"
        F4.divorced = "8 NOV 2020"
        F5.divorced = "8 NOV 2010"
        output = utilities.us48MostRecentDivorce([F1, F2, F3, F4, F5])
        self.assertEqual(output, ["F4"])
    
    def testNA(self):
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F1.divorced = "NA"
        F2.divorced = "8 NOV 1980"
        output = utilities.us48MostRecentDivorce([F1, F2])
        self.assertEqual(output, ["F2"])
    
    def testEmptyStringMarriage(self):
        F1 = script.Family("F1")
        F2 = script.Family("F2")
        F1.divorced = " "
        F2.divorced = "8 NOV 1980"
        output = utilities.us48MostRecentDivorce([F1, F2])
        self.assertEqual(output, ["F2"]) 
        
    def testEmptyList(self):
        output = utilities.us48MostRecentDivorce([])
        self.assertEqual(output, [])
        
if __name__ == '__main__':
    unittest.main()  

'''
def testSingleValidMarriageBeforeDeath(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        I1.death = "2 JAN 2019"
        F1.married = "2 JAN 2017"
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        print(output)
        self.assertEqual(output, [F1])

        

def testNoMarriageIndividuals(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        F1.married = " "
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(output, [])
        
    def testSingleInvalidMarriageBeforeDeath(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        I1.death = "2 JAN 2017"
        F1.married = "2 JAN 2019"
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(len(output), 1)
           
    def testSingleValidMarriageBeforeDeath(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        I1.death = "2 JAN 2019"
        F1.married = "2 JAN 2017"
        output = utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(output, [])
    
    def testGenderMatch(self):
        I1 = script.Individual("I1")
        F1 = script.Family("F1")
        I1.gender = "M"
        I1.death = "7 JAN 1917"
        F1.married = "7 JAN 1919"
        utilities.us05MarriageBeforeDeath([F1], [I1])
        self.assertEqual(utilities.us05MarriageBeforeDeath.spouse[:-3], 'husband')




'''





