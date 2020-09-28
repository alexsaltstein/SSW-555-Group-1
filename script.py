from prettytable import PrettyTable
from datetime import datetime
import importlib
utils = importlib.import_module("utilities")
"""
Author: Alex Saltstein, Daniel Collins, James Surless, Miriam Podkolzin, Kenny Mason, Brandon Patton

Description: This python script reads the specified GEDCOM file that you want to read then outputs in a
  pretty format the individuals and the families
    "--> <input line>" then
    "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
      <level> is the level of the input line, e.g. 0, 1, 2
      <tag> is the tag associated with the line, e.g. 'INDI', 'FAM', 'DATE', ...
      <valid?> has the value 'Y' if the tag is one of the supported tags or 'N' otherwise.  The set of all valid tags for our project is specified in the Project Overview document.
      <arguments> is the rest of the line beyond the level and tag.
"""
class Individual:
  def __init__(self, iD):
    self.iD = iD
    self.name = ""
    self.gender = ""
    self.birthday = ""
    self.age = ""
    self.alive = True
    self.death = "NA"
    self.child = "NA"
    self.spouse = "NA"

  def toList(self):
    return [self.iD,self.name,self.gender,self.birthday,self.age,self.alive,self.death,self.child if len(self.child) != 0 else "NA",self.spouse]

class Family:
  def __init__(self, iD):
    self.iD = iD
    self.married = ""
    self.divorced = "NA"
    self.husbId = ""
    self.husbName = ""
    self.wifeId = ""
    self.wifeName = ""
    self.children = []

  def addChild(self,child):
    self.children.append(child)
    
  def toList(self):
    return [self.iD,self.married,self.divorced,self.husbId,self.husbName,self.wifeId,self.wifeName,self.children if len(self.children) != 0 else "NA"]
    
def printIndividuals(individuals):
  table = PrettyTable()
  table.field_names = ["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]
  for i in individuals:
    table.add_row(i.toList())
  print("Individuals")
  print(table)
  
def printFamily(families):
  table = PrettyTable()
  table.field_names = ["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"]
  for f in families:
    table.add_row(f.toList())
  print("Families")
  print(table)

#beginning of script
validTags = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

f = open("my-family.ged", "r")

individuals = []
families = []

def findat(f):
  isInd = False
  found = False
  findingBirt = False
  findingDeat = False
  findingMarr = False
  findingDiv = False
  currI = 0
  for i,line in enumerate(f):
    line = line.replace("\n","")
    linelist = line.split(" ")
    i = linelist[1]
    if i[0] == "@":
      if i[1] == "F":
        families.append(Family(i[1:-1]))
        isInd = False
      if i[1] == "I":
        individuals.append(Individual(i[1:-1]))
        isInd = True
      found = True
    elif found:
#      print("isInd: ", isInd)
#      print(linelist)
      tag = linelist[1]
      if isInd:
        #do individual parse
        try:
          if tag == "NAME":
            individuals[len(individuals)-1].name = " ".join(linelist[2:])
          if tag == "SEX":
            individuals[len(individuals)-1].gender = linelist[2]
          if findingBirt:
            birthday = " ".join(linelist[2:])
            datetime_object = datetime.strptime(birthday, '%d %b %Y')
            individuals[len(individuals)-1].birthday = birthday
            individuals[len(individuals)-1].age = str((datetime.now() - datetime_object)/365).split(" ")[0]
            findingBirt = False
          if findingDeat:
            individuals[len(individuals)-1].death = " ".join(linelist[2:])
            datetime_object_birt = datetime.strptime(individuals[len(individuals)-1].birthday, '%d %b %Y')
            datetime_object_deat = datetime.strptime(individuals[len(individuals)-1].death, '%d %b %Y')
            individuals[len(individuals)-1].age = str((datetime_object_deat - datetime_object_birt)/365).split(" ")[0]
            individuals[len(individuals)-1].alive = False
            findingDeat = False
          if tag == "BIRT":
            findingBirt = True
          if tag == "DEAT":
            findingDeat = True
          if tag == "FAMC":
            individuals[len(individuals)-1].child = linelist[2].strip("@")
          if tag == "FAMS":
            individuals[len(individuals)-1].spouse = linelist[2].strip("@")
        except:
          #do nothing cause not valid tag
          pass
      else:
        #do fam parse
        try:
          if findingMarr:
            families[len(families)-1].married = " ".join(linelist[2:])
            findingMarr = False
          if tag == "MARR":
            findingMarr = True
          if findingDiv:
            families[len(families)-1].divorced = " ".join(linelist[2:])
            findingDiv = False
          if tag == "DIV":
            findingDiv = True
          if tag == "HUSB":
            hid = linelist[2].strip("@")
            families[len(families)-1].husbId = hid
            for ind in individuals:
              if ind.iD == hid:
                families[len(families)-1].husbName = ind.name
          if tag == "WIFE":
            wid = linelist[2].strip("@")
            families[len(families)-1].wifeId = wid
            for ind in individuals:
              if ind.iD == wid:
                families[len(families)-1].wifeName = ind.name
          if tag == "CHIL":
            families[len(families)-1].addChild(linelist[2].strip("@"))
        except:
          #do nothing cause not valid tag
          pass
      
#every week we just integrate specific functions for sprint formatting is specified in sprintChecklist.pdf
def printErrors():
  utils.us03DeathBeforeBirth(individuals)
  utils.us04MarriageBeforeDivorce(families)
  utils.us07AgeOver150(individuals)
  utils.us08BirthBeforeMarriage(families, individuals)

findat(f)
printIndividuals(individuals)
printFamily(families)
printErrors()
