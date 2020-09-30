import unittest
import importlib
script = importlib.import_module("script")
utilities = importlib.import_module("utilities")

class us14MultipleBirthsTest(unittest.TestCase):

    '''
    five tests:
    1. Family with no child is legal
    2. Family with one child is legal
    3. Family with Four children is legal
    4. Family with five children is not legal
    5. Illegal family should be correctly reported
    '''
    def testEmptyFamily(self):
        F1 = script.Family("F1")
        output = utilities.us14MultipleBirths([F1])
        self.assertEqual(output, [])

    def testOneChild(self):
        F1 = script.Family("F1")
        F1.children.append(1)
        output = utilities.us14MultipleBirths([F1])
        self.assertEqual(output, [])

    def testFourChildren(self):
        F1 = script.Family("F1")
        F1.children.append(1)
        F1.children.append(2)
        F1.children.append(3)
        F1.children.append(4)
        output = utilities.us14MultipleBirths([F1])
        self.assertEqual(output, [])

    def testFiveChildrenNotLegal(self):
        F1 = script.Family("F1")
        F1.children.append(1)
        F1.children.append(2)
        F1.children.append(3)
        F1.children.append(4)
        F1.children.append(5)
        output = utilities.us14MultipleBirths([F1])
        self.assertEqual(len(output), 1)

    def testIllegalFamilyCorrectlyReported(self):
        F1 = script.Family("F1")
        F1.children.append(1)
        F1.children.append(2)
        F1.children.append(3)
        F1.children.append(4)
        F1.children.append(5)
        output = utilities.us14MultipleBirths([F1])
        self.assertEqual(output, ["F1"])

if __name__ == '__main__':
    unittest.main()
