# This is the utilities script for how we are going to implement stories for each sprint
from datetime import datetime
from datetime import date
from datetime import timedelta
import dateutil.relativedelta
from collections import Counter

'''
    This function loops through individuals and makes sure that
    births and deaths occur before the current date. Then loops through
    families to make sure marriage/divorces occur before the current
    date. If there is an error, outputs information about error and
    list of id's with errors
'''


def us01DatesBeforeCurrentDate(individuals, families):
    KEY_WORD = "ERROR: US01: "
    output = []
    now = datetime.now()
    for x in individuals:
        if int((now - datetime.strptime(x.birthday, '%d %b %Y')).days) <= 0:
            print(KEY_WORD + x.iD + ": Born " + x.birthday + " after today " + str(now))
            output.append(x.iD)
        if x.death != "NA" and int((now - datetime.strptime(x.death, '%d %b %Y')).days) <= 0:
            print(KEY_WORD + x.iD + ": Died " + x.death + " after today " + str(now))
            output.append(x.iD)
    for y in families:
        if int((now - datetime.strptime(y.married, '%d %b %Y')).days) <= 0:
            print(KEY_WORD + x.iD + ": Married " + y.married + " after today " + str(now))
            output.append(y.iD)
        if y.divorced != "NA" and int((now - datetime.strptime(y.divorced, '%d %b %Y')).days) <= 0:
            print(KEY_WORD + y.iD + ": Divorced " + y.divorced + " after today " + str(now))
            output.append(y.iD)
    return output


'''
    This function loops through individuals and families to make sure that
    birth occurs before the marriage of an individual. If there is an error,
    outputs information about error and list of id's with errors
'''


def us02BirthBeforeMarriage(individuals, families):
    KEY_WORD = "ERROR: US02: "
    output = []
    for fam in families:
        for indi in individuals:
            if (indi.iD in fam.iD and (datetime.strptime(fam.married, '%d %b %Y') - datetime.strptime(indi.birthday,
                                                                                                      '%d %b %Y')).days <= 0):
                print(KEY_WORD + fam.iD + ": Married " + fam.married + " after birth " + indi.birthday)
                output.append(fam.iD)
    return output


'''
    This function loops through individuals and makes sure that
    birth occurs before death and if there is an error outputs
    that there is a death before birth error returns list of id's with errors
'''


def us03DeathBeforeBirth(individuals):
    KEY_WORD = "ERROR: INDIVIDUALS: US04: "
    output = []
    for indi in individuals:
        isDeathBeforeBirth = indi.death != "NA" and (
                    datetime.strptime(indi.death, '%d %b %Y') - datetime.strptime(indi.birthday, '%d %b %Y')).days <= 0
        if isDeathBeforeBirth:
            print(KEY_WORD + indi.iD + ": Died " + indi.death + " before born " + indi.birthday)
            output.append(indi.iD)
    return output


'''
    This function loops through families and makes sure that
    marriage occurs before divorce and if there is an error outputs
    that there is a divorce before marriage error returns list of id's with errors
'''


def us04MarriageBeforeDivorce(families):
    KEY_WORD = "ERROR: FAMILY: US04: "
    output = []
    for fam in families:
        isDivorceBeforeMarriage = fam.divorced != "NA" and (
                    datetime.strptime(fam.divorced, '%d %b %Y') - datetime.strptime(fam.married, '%d %b %Y')).days <= 0
        if isDivorceBeforeMarriage:
            print(KEY_WORD + fam.iD + ": Divorced " + fam.divorced + " before married " + fam.married)
            output.append(fam.iD)
    return output


'''
    This function loops through individuals in each
    family and ensures that any marriages occur
    before the death of a spouse. If there are any
    erros, this function will print out an error
    statement. The error statement includes
    information regarding the id of the family for
    the invalid marriage, the invalid marriage date,
    the id of the individual who died before the
    marriage date, and the individual's death date.
'''


def us05MarriageBeforeDeath(families, individuals):
    KEY_WORD = "ERROR: FAMILY: US06"
    output = []
    for fam in families:
        husband = fam.husbId
        wife = fam.wifeId
        h = next(h for h in individuals if h.iD == husband)
        w = next(w for w in individuals if w.iD == wife)
        if fam.married == "NA":
            continue
        else:
            if h.death == "NA":
                h_diff = 1
            else:
                h_diff = datetime.strptime(h.death, '%d %b %Y') - datetime.strptime(fam.married, '%d %b %Y')
                h_diff = h_diff.days
            if w.death == "NA":
                w_diff = 1
            else:
                w_diff = datetime.strptime(w.death, '%d %b %Y') - datetime.strptime(fam.married, '%d %b %Y')
                w_diff = w_diff.days
            if h_diff <= 0:
                print(
                    KEY_WORD + ' ' + fam.iD + ":" + " Married " + fam.married + " after husband's " + '(' + h.iD + ')' + " death on " + h.death)
                output.append(fam.iD)
            elif w_diff <= 0:
                print(
                    KEY_WORD + ' ' + fam.iD + ":" + " Married " + fam.married + " after wife's " + '(' + w.iD + ')' + " death on " + w.death)
                output.append(fam.iD)
    return output


'''
    This function loops through individuals in each
    family to ensure that all divorces occur before
    the death of either spouse. If there are any
    erros, this function will print out an error
    statement. The error statement includes
    information regarding the id of the family for
    the invalid divorce, the invalid divorce date,
    the id of the individual who died before the
    divorce date, and the individual's death date.
'''


def us06DivorceBeforeDeath(families, individuals):
    KEY_WORD = "ERROR: FAMILY: US06"
    output = []
    for fam in families:
        husband = fam.husbId
        wife = fam.wifeId
        h = next(h for h in individuals if h.iD == husband)
        w = next(w for w in individuals if w.iD == wife)
        if fam.divorced == "NA":
            continue
        else:
            if h.death == "NA":
                h_diff = 1
            else:
                h_diff = datetime.strptime(h.death, '%d %b %Y') - datetime.strptime(fam.divorced, '%d %b %Y')
                h_diff = h_diff.days
            if w.death == "NA":
                w_diff = 1
            else:
                w_diff = datetime.strptime(w.death, '%d %b %Y') - datetime.strptime(fam.divorced, '%d %b %Y')
                w_diff = w_diff.days
            if h_diff <= 0:
                print(
                    KEY_WORD + ' ' + fam.iD + ":" + " Divorced " + fam.divorced + " after husband's " + '(' + h.iD + ')' + " death on " + h.death)
                output.append(fam.iD)
            elif w_diff <= 0:
                print(
                    KEY_WORD + ' ' + fam.iD + ":" + " Divorced " + fam.divorced + " after wife's " + '(' + w.iD + ')' + " death on " + w.death)
                output.append(fam.iD)
    return output


'''
    This function loops through individuals and makes sure that
    individuals ages are less than 150 years of age. (i.age < 150)
    If there is an error, outputs information about error and list of id's
    with errors
'''


def us07AgeOver150(individuals):
#    for i in individuals:
#        print(i.age)
    KEY_WORD = "ERROR: INDIVIDUALS: US07: "
    output = []
    for indi in individuals:
        isOver150 = indi.age != '' and int(indi.age) > 149
        if isOver150:
            print(KEY_WORD + indi.iD + ": Age " + str(indi.age) + ", over 150")
            output.append(indi.iD)
    return output


'''
    This function loops through families and makes sure that
    birth of all children occur after marriage and if there is an error, outputs
    information about error and list of id's with errors.
'''


def us08BirthBeforeMarriage(families, individuals):
    KEY_WORD = "ERROR: FAMILY: US08: "
    output = []
    isBirthBeforeMarriage = False
    for fam in families:
        for indi in individuals:
            if (indi.iD in fam.children and (
                    datetime.strptime(indi.birthday, '%d %b %Y') - datetime.strptime(fam.married,
                                                                                     '%d %b %Y')).days <= 0):
                isBirthBeforeMarriage = True
                if isBirthBeforeMarriage:
                    print(
                        KEY_WORD + fam.iD + ": Married " + fam.married + " after birth of " + indi.name + " on " + indi.birthday)
                    output.append(fam.iD)
    return output


def findParentDeath(indi_iD, listOfIndis):
    '''Loops through list of individuals, finds a specific parent's death date, and returns that information'''
    for i in listOfIndis:
        if indi_iD == i.iD:
            if not i.alive:
                return i.death


def findChildBday(child_iD, listOfIndis):
    '''Loops through list of individuals, finds a specific individuals birth date, and returns that information'''
    for i in listOfIndis:
        if child_iD == i.iD:
            return i.birthday


def makeDateTimeObject(date):
    return datetime.strptime(date, "%d %b %Y")


def us09BirthBeforeDeathOfParents(listOfFamilies, listOfIndividuals):
    '''Returns ids of children whose birthdates come before the death of their mother and/or after 9 months following the death of their father'''
    output = []
    KEY_WORD = "ERROR: INDIVIDUALS: US09: "
    for f in listOfFamilies:
        husbandDeath = findParentDeath(f.husbId, listOfIndividuals)  # store husband's death date if applicable
        wifeDeath = findParentDeath(f.wifeId, listOfIndividuals)  # store wife's death date if applicable
        for c in f.children:  # loop through list of children IDs
            if findParentDeath(f.wifeId, listOfIndividuals) is not None:  # check if wifeDeath exists
                if makeDateTimeObject(findChildBday(c, listOfIndividuals)) > makeDateTimeObject(wifeDeath):  # if Mother's death date is before birth of child, not possible
                    print(KEY_WORD + "Mother's death cannot come before Child's birth")
                    output.append(c)  # appends problematic child id to output
            if findParentDeath(f.husbId, listOfIndividuals) is not None:  # check if husbandDeath exists
                if (makeDateTimeObject(findChildBday(c, listOfIndividuals)) - dateutil.relativedelta.relativedelta(months=9)) > makeDateTimeObject(husbandDeath):  # left operand is conception date. if that's greater than the father's death date, that is impossible
                    print(KEY_WORD + "Father's death cannot come after 9 months before Child's birth (Child's conception date)")
                    output.append(c)  # appends problematic child id to output
    return output


def us10MarriageAfter14(listOfFamilies, listOfIndividuals):
    output = []
    KEY_WORD = "ERROR: INDIVIDUALS: US10: "
    for f in listOfFamilies:
        husband = f.husbId
        wife = f.wifeId
        for i in listOfIndividuals:
            if (i.iD == husband or i.iD == wife) and (
                    datetime.strptime(f.married, '%d %b %Y') - datetime.strptime(i.birthday,
                                                                                 '%d %b %Y')).days / 365 < 14:
                print(KEY_WORD + i.iD + " got married under the age of 14.")
                output.append(i.iD)
    return output


'''
    This function loops through families and makes sure nobody is married to two people at the same time.
'''


def us11NoBigamy(families, individuals):
    KEY_WORD = "ERROR - US11: "
    output = []
    big = False
    f1 = ""
    f2 = ""
    fams = [f for f in families]
    for family in fams:
        hid = family.husbId
        wid = family.wifeId
        fams.remove(family)

        for fam in fams:
            h2 = fam.husbId
            w2 = fam.wifeId
            if hid == h2:
                if datetime.strptime(fam.married, '%d %b %Y') < datetime.strptime(family.married, '%d %b %Y'):
                    w = next(w for w in individuals if w.iD == w2)
                    if ((fam.divorced == "NA" and (
                            w.death == "NA" or datetime.strptime(w.death, '%d %b %Y') > datetime.strptime(
                            family.married, '%d %b %Y'))) or
                            (fam.divorced != "NA" and datetime.strptime(fam.divorced, '%d %b %Y') > datetime.strptime(
                                family.married, '%d %b %Y'))):
                        big = True
                        f1 = fam.iD
                        f2 = family.iD
                        ind1 = fam.husbName + " " + hid
                        ind2 = fam.wifeName + " " + w2
                        ind3 = family.wifeName + " " + wid
                        output.extend([hid, w2, wid, f1, f2])
                else:
                    w = next(w for w in individuals if w.iD == wid)
                    if ((family.divorced == "NA" and (
                            w.death == "NA" or datetime.strptime(w.death, '%d %b %Y') > datetime.strptime(fam.married,
                                                                                                          '%d %b %Y'))) or
                            (family.divorced != "NA" and datetime.strptime(family.divorced,
                                                                           '%d %b %Y') > datetime.strptime(fam.married,
                                                                                                           '%d %b %Y'))):
                        big = True
                        f1 = fam.iD
                        f2 = family.iD
                        ind1 = fam.husbName + " " + hid
                        ind2 = fam.wifeName + " " + w2
                        ind3 = family.wifeName + " " + wid
                        output.extend([hid, w2, wid, f1, f2])

            if wid == w2:
                if datetime.strptime(fam.married, '%d %b %Y') < datetime.strptime(family.married, '%d %b %Y'):
                    h = next(h for h in individuals if h.iD == h2)
                    if ((fam.divorced == "NA" and (
                            h.death == "NA" or datetime.strptime(h.death, '%d %b %Y') > datetime.strptime(
                            family.married, '%d %b %Y'))) or
                            (fam.divorced != "NA" and datetime.strptime(fam.divorced, '%d %b %Y') > datetime.strptime(
                                family.married, '%d %b %Y'))):
                        big = True
                        f1 = fam.iD
                        f2 = family.iD
                        ind1 = fam.wifeName + " " + wid
                        ind2 = fam.husbName + " " + h2
                        ind3 = family.husbName + " " + hid
                        output.extend([wid, h2, hid, f1, f2])
                else:
                    h = next(h for h in individuals if h.iD == hid)
                    if ((family.divorced == "NA" and (
                            h.death == "NA" or datetime.strptime(h.death, '%d %b %Y') > datetime.strptime(fam.married,
                                                                                                          '%d %b %Y'))) or
                            (family.divorced != "NA" and datetime.strptime(family.divorced,
                                                                           '%d %b %Y') > datetime.strptime(fam.married,
                                                                                                           '%d %b %Y'))):
                        big = True
                        f1 = fam.iD
                        f2 = family.iD
                        ind1 = fam.wifeName + " " + wid
                        ind2 = fam.husbName + " " + h2
                        ind3 = family.husbName + " " + hid
                        output.extend([wid, h2, hid, f1, f2])

    if big:
        print(
            KEY_WORD + ind1 + " is married to " + ind2 + " while also married to " + ind3 + ". Families " + f1 + " and " + f2)
    return output


'''
    This function loops through families and makes sure that
    Mother is less than 60 years older than her children and
    father is less than 80 years older than his children.
    if there is an error, outputs information about error and list of id's with errors.
'''


def us12ParentsNotTooOld(families, individuals):
    KEY_WORD = "ERROR - US11: "
    output = []
    tooOld = False
    fams = [f for f in families if f.children != []]

    for family in fams:
        hid = family.husbId
        wid = family.wifeId
        h = next(h for h in individuals if h.iD == hid)
        w = next(w for w in individuals if w.iD == wid)
        for child in family.children:
            c = next(c for c in individuals if c.iD == child)
            if (datetime.strptime(c.birthday, '%d %b %Y') - datetime.strptime(w.birthday, '%d %b %Y')).days > 21900:
                tooOld = True
                ind1 = family.wifeName + " " + wid
                ind2 = c.name + " " + c.iD
                years = "60"
                f1 = family.iD
                output.extend([wid, c.iD, f1])
            if (datetime.strptime(c.birthday, '%d %b %Y') - datetime.strptime(h.birthday, '%d %b %Y')).days > 29200:
                tooOld = True
                ind1 = family.husbName + " " + hid
                ind2 = c.name + " " + c.iD
                years = "80"
                f1 = family.iD
                output.extend([hid, c.iD, f1])
    if tooOld:
        print(KEY_WORD + ind1 + " is more than " + years + " years older than their child, " + ind2 + ". Family " + f1)
    return output


def us13SiblingSpacing(families, individuals):
    KEY_WORD = "ERROR: FAMILY : US13: "
    output = []
    for fam in families:
        for id1 in fam.children:
            for id2 in fam.children:
                if id1 != id2:
                    c1 = [x for x in individuals if x.iD == id1][0]
                    c2 = [x for x in individuals if x.iD == id2][0]
                    d = abs(
                        (datetime.strptime(c1.birthday, '%d %b %Y') - datetime.strptime(c2.birthday, '%d %b %Y')).days)
                    if d >= 2 and d <= 30 * 8 and (not fam.iD in output):
                        print(KEY_WORD, "Sibling Spacing is not valid")
                        output.append(fam.iD)
    return output


def us14MultipleBirths(families):
    KEY_WORD = "ERROR: FAMILY : US14: "
    output = []
    for fam in families:
        if len(fam.children) > 5:
            print(KEY_WORD + fam.iD + " has more than 5 children")
            output.append(fam.iD)
    return output

'''
    This function loops through individuals and makes sure that
    birth occurs before death and if there is an error outputs
    that there is a death before birth error returns list of id's with errors
'''
def us17NoMarriagesToDescendents(individuals, families):
    KEY_WORD = "ERROR: INDIVIDUALS: US17: "
    output = []
    for fam in families:
        husbIsMarriedToDescendent = False
        wifeIsMarriedToDescendent = False
        if fam.children != "NA":
          for indi in fam.children:
            if fam.wifeId == indi:
              husbIsMarriedToDescendent = True
            if fam.husbId == indi:
              wifeIsMarriedToDescendent = True
        if husbIsMarriedToDescendent:
            print(KEY_WORD + fam.iD + ": husband " + fam.husbId + " is married to descendent wife " + fam.wifeId)
            output.append(fam.husbId)
        elif wifeIsMarriedToDescendent:
            print(KEY_WORD + fam.iD + ": wife " + fam.wifeId + " is married to descendent husband " + fam.husbId)
            output.append(fam.wifeId)
    return output

'''
  This function returns the family that the individual is a child in
'''
def getFamOfId(id, individuals):
  return individuals[int(id[1:])-1].child

'''
    This function loops through individuals and makes sure that
    birth occurs before death and if there is an error outputs
    that there is a death before birth error returns list of id's with errors
'''
def us18NoSiblingMarriages(individuals, families):
  KEY_WORD = "ERROR: FAMILY: US18: "
  output = []
  for fam in families:
    husbFam = getFamOfId(fam.husbId, individuals)
    wifeFam = getFamOfId(fam.wifeId, individuals)
    isMarriedToSibling = husbFam != "NA" and wifeFam != "NA" and wifeFam == husbFam
    if isMarriedToSibling:
      print(KEY_WORD + fam.iD + ": husband " + fam.husbId + " married to sibling wife " + fam.wifeId)
      output.append(fam.iD)
  return output


def us21CorrectGenderForRole(individuals, families):
    KEY_WORD = "ERROR: FAMILY: US21: "
    output = []
    for fam in families:
        husbandId = fam.husbId
        wifeId = fam.wifeId
        for indi in individuals:
            incorrectHusbRole = indi.iD == husbandId and indi.gender == 'F'
            incorrectWifeRole = indi.iD == wifeId and indi.gender == 'M'
            if (incorrectHusbRole):
                print(KEY_WORD + indi.iD + ": " + fam.iD +  ": Husband is Female")
                output.append(indi.iD)
            if (incorrectWifeRole):
                print(KEY_WORD + indi.iD + ": " + fam.iD +  ": Wife is Male")
                output.append(indi.iD)
    return output

def us22UniqueIDs(individuals, families):
    KEY_WORD = "ERROR: FAMILY: US22: "
    output = []
    famList = []
    indiList = []
    for fam in families:
        famList.append(fam.iD)
    for indi in individuals:
        indiList.append(indi.iD)
    for famID in famList:
        DupeFamId = famList.count(famID) > 1
        if (DupeFamId):
                print(KEY_WORD + famID + ": Duplicate Family ID")
                output.append(famID)
    for indiID in indiList:
        DupeIndiId = indiList.count(indiID) > 1
        if (DupeIndiId):
            print(KEY_WORD + indiID + ": Duplicate Individual ID")
            output.append(indiID)
    return output


def findDupes(itemList):
    dupes = []
    checked = []
    for i in itemList:
        if i not in checked:
            checked.append(i)
        else:
            dupes.append(i)
    return dupes


def us23UniqueNameAndBirthDate(individuals):
    '''Returns duplicate birthdays and names, if they exist'''
    KEY_WORD = "ERROR: INDIVIDUALS: US23: "
    output = []
    birthdays = []
    names = []
    for i in individuals:  # loops through list of individuals and grabs all birthdays and names
        birthdays.append(i.birthday)
        names.append(i.name)
    bday_dupes = findDupes(birthdays)
    name_dupes = findDupes(names)
    if (len(bday_dupes) > 0):
        print(KEY_WORD + "Duplicate birthday(s): " + str(bday_dupes))  # prints error messages if there are duplicates
    if (len(name_dupes) > 0):
        print(KEY_WORD + "Duplicate name(s): " + str(name_dupes))
    output.extend(bday_dupes)
    output.extend(name_dupes)
    return output


def us24UniqueFamiliesBySpouses(families):
    '''Returns duplicate spouse name pairs and marriage dates, if they exist'''
    KEY_WORD = "ERROR: INDIVIDUALS: US24: "
    output = []
    spouseNamePairs = []
    marriageDates = []
    for f in families:                                              #loops through list of families and grabs all spouse names and marriage dates
        spouseNamePairs.append([f.husbName, f.wifeName])            #places spouse names in a pair of type list, so we compare family to family as opposed to simply name to name
        marriageDates.append(f.married)
    c = Counter(map(tuple, spouseNamePairs))                        #sets up Counter, maps each element in spouseNamePairs to a tuple (each spouse pair name becomes a tuple)
    spouseDupes = [k for k,v in c.items() if v>1]                   #finds duplicate name pairs using the Counter
    marriageDupes = findDupes(marriageDates)
    if (len(spouseDupes) > 0):
        print(KEY_WORD + "Duplicate spouse name pairs: " + str(spouseDupes))        #prints error messages if there are duplicates
    if (len(marriageDupes) > 0):
        print(KEY_WORD + "Duplicate marriage date(s): " + str(marriageDupes))
    output.extend(spouseDupes)
    output.extend(marriageDupes)
    return output

def us25UniqueFirstNames(families, individuals):
    '''Checks for multiple children in the same family with the same first name and birthday'''
    KEY_WORD = "ERROR - US25: "
    output = []
    fams = [f for f in families if len(f.children) > 1]

    for family in fams:
        kids, chldrn = [], []
        for child in family.children:
            c = next(c for c in individuals if c.iD == child)
            chldrn.append([c.iD, [c.name, c.birthday]])
            kids.append([c.name, c.birthday])
        for kid in kids:
            kids.remove(kid)
            if kid in kids:
                lst = [c[0] for c in chldrn if kid == c[1]]
                lst.append(family.iD)
                output.extend(lst)
                print(KEY_WORD + "There is more than one " + kid[0] + " with the same birthday in family " + family.iD)
    return output

def us26CorrespondingEntries(families, individuals):
    '''Checks that all entries in Families have properly corresponding Individual entries, and vice versa'''
    KEY_WORD = "ERROR - US26: "
    output = []
    fams = [f for f in families]
    inds = [i for i in individuals]
    for fam in fams:
        h = next(h for h in inds if h.iD == fam.husbId)
        w = next(w for w in inds if w.iD == fam.wifeId)
        if(w.spouse != fam.husbId or h.spouse != fam.wifeId):
            print(KEY_WORD + fam.wifeName + "'s (" + fam.wifeId + ") and " + fam.husbName + "'s (" + fam.husbId + ") individual spousal records do not align with their family (" + fam.iD + ") record.")
            output.extend([fam.wifeId, fam.husbId, fam.iD])
        if(fam.children != w.child):
                print(KEY_WORD + fam.wifeName + "'s (" + fam.wifeId + ") individual child record does not align with her family (" + fam.iD + ") record.")
                output.extend([fam.wifeId, fam.iD])
        if(fam.children != h.child):
                print(KEY_WORD + fam.husbName + "'s (" + fam.husbId + ") individual child record does not align with his family (" + fam.iD + ") record.")
                output.extend([fam.husbId, fam.iD])

    for ind in inds:
        if ind.spouse != "NA":
            f = next(f for f in fams if ind.iD == f.husbId or ind.iD == f.wifeId)
            if not ((ind.iD == f.husbId and ind.spouse == f.wifeId) or (ind.iD == f.wifeId and ind.spouse == f.husbId)):
                print(KEY_WORD + ind.name + "'s (" + ind.iD + ") individual spousal record does not align with their family (" + f.iD + ") record.")
                output.extend([ind.iD, ind.spouse, f.iD])
            if ind.child != f.children:
                print(KEY_WORD + ind.name + "'s (" + ind.iD + ") individual child record does not align with their family (" + f.iD + ") children record.")
                output.extend([ind.iD, f.iD])
        asKid = [f for f in fams if ind.iD in f.children]
        if len(asKid) > 0:
            fam = asKid[0]
            h = next(h for h in inds if h.iD == fam.husbId)
            w = next(w for w in inds if w.iD == fam.wifeId)
            if ind.iD not in h.child:
                print(KEY_WORD + ind.name + " (" + ind.iD + ") does not appear in one or more of their father's (" + h.iD + ") child record.")
                output.extend([ind.iD, h.iD, f.iD])
            if ind.iD not in w.child:
                print(KEY_WORD + ind.name + " (" + ind.iD + ") does not appear in one or more of their mother's (" + w.iD + ") child record.")
                output.extend([ind.iD, w.iD, f.iD])
    return output

def getChildrenNames(childrenIds, individuals):
    childrenNames = []
    for c in childrenIds:
        for i in individuals:
            if c.iD == i.iD:
                childrenNames.append(i.name)
    return childrenNames
'''def us21CorrectGenderForRole(individuals, families):
    KEY_WORD = "ERROR: FAMILY: US21: "
    output = []
    for fam in families:
        husbandId = fam.husbId
        wifeId = fam.wifeId
        for indi in individuals:
            incorrectHusbRole = indi.iD == husbandId and indi.gender == 'F'
            incorrectWifeRole = indi.iD == wifeId and indi.gender == 'M'
            if (incorrectHusbRole):
                print(KEY_WORD + indi.iD + ": " + fam.iD +  ": Husband is Female")
                output.append(indi.iD)
            if (incorrectWifeRole):
                print(KEY_WORD + indi.iD + ": " + fam.iD +  ": Wife is Male")
                output.append(indi.iD)
    return output'''
    # List all individuals born in the last 30 days
def us35ListRecentBirths(individuals, families):
    KEY_WORD = "ERROR: INDIVIDUALS: US35: "
    output = []
    for i in individuals:
        if (datetime.today() - makeDateTimeObject(i.birthday)).days <=30:
            print(KEY_WORD + i.iD + ": " + "Born in the last 30 days")
            output.append(i.iD)
    return output

    # List all individuals who have died in the last 30 days
def us36ListRecentDeaths(individuals, families):
    KEY_WORD = "ERROR: INDIVIDUALS: US36: "
    output = []
    for i in individuals:
        if i.alive==False and (datetime.today() - makeDateTimeObject(i.death)).days <=30:
            print(KEY_WORD + i.iD + ": " + "Died in the last 30 days")
            output.append(i.iD)
    return output

def us31ListLivingSingle(individuals, families):
  '''Prints out a list of all living people in a GEDCOM file over 30 and who have never been married'''
  KEY_WORD = "LIST: LIVING PEOPLE: "
  output = []
  married = []
  for f in families:
    married.append(f.husbId)
    married.append(f.wifeId)
  for i in individuals:
    if i.alive and int(i.age) >= 30 and i.iD not in married:
      output.append(i.iD)
  print(KEY_WORD)
  if len(output) > 0:
    for id in output:
      print("\t" + id)
  return output

def us32ListMultipleBirths(individuals):
  '''Prints out a list of all multiple births in a GEDCOM file'''
  KEY_WORD = "LIST: MULTIPLE BIRTHS: "
  output = []
  for i in individuals:
    for i2 in individuals:
      if i.iD != i2.iD and i.birthday == i2.birthday:
        if i.iD not in output:
          output.append(i.iD)
        if i2.iD not in output:
          output.append(i2.iD)
  if len(output) > 0:
    print(KEY_WORD)
    for id in output:
      print("\t" + id)
  return output

def us37ListRecentSurvivors(individuals, families):
    '''Prints out the recent survivors (spouses and descendants) of individuals who died in the last 30 days'''
    KEY_WORD = "ERROR: INDIVIDUALS: US37: "
    output = []
    for i in individuals:
        if not i.alive and (datetime.today() - makeDateTimeObject(i.death)).days <= 30:
            for f in families:
                if i.iD == f.husbId:
                    descendantNames = getChildrenNames(f.children, individuals)
                    print("Recent survivors of " + i.name + "'s untimely death: ")
                    print("\tSpouse of " + i.name + ": " + f.wifeName)
                    print("\tDescendants of " + i.name + " with " + f.wifeName + ": " + str(descendantNames) + "\n")
                    output.append([f.wifeName, descendantNames])
                if i.iD == f.wifeId:
                    descendantNames = getChildrenNames(f.children, individuals)
                    print("Recent survivors of " + i.name + "'s untimely death:")
                    print("\tSpouse of " + i.name + ": " + f.husbName)
                    print("\tDescendants of " + i.name + " with " + f.husbName + ": " + str(descendantNames) + "\n")
                    output.append([f.husbName, descendantNames])
    return output

def us38ListUpcomingBirthdays(individuals):
    '''Prints out a list of all living people in a GEDCOM file whose birthdays occur within the next 30 days'''
    KEY_WORD = "ERROR: INDIVIDUALS: US38: "
    output = []
    for i in individuals:
        if ((makeDateTimeObject(i.birthday) - datetime.today()).days <= 30) and ((makeDateTimeObject(i.birthday) - datetime.today()).days >= 0):
            output.append(i.name)
    print("Upcoming Birthdays:")
    for name in output:
        print("\t" + name)
    return output

def us39ListUpcomingAnniversaries(families, individuals):
    '''List all anniversaries of living couples that are coming up within 30 days'''
    KEY_WORD = "List - US39: "
    output = []
    fams = [f for f in families if f.married]
    today = datetime.now()
    month = today + timedelta(days=30)
    for fam in fams:
        h = next(h for h in individuals if h.iD == fam.husbId)
        w = next(w for w in individuals if w.iD == fam.wifeId)
        anniv = datetime.strptime(fam.married, '%d %b %Y')
        if today.month == 12 and today.day > 1:
            if anniv.month == 12:
                anniv = anniv.replace(year = today.year)
                if h.alive and w.alive and (today <= anniv <= month):
                    output.append([h.iD, w.iD, fam.iD])
                    print(KEY_WORD + h.name + " and " + w.name + " have their anniversary coming up! Family " + fam.iD)
            elif anniv.month == 1:
                anniv = anniv.replace(year = month.year)
                if h.alive and w.alive and (anniv <= month):
                    output.append([h.iD, w.iD, fam.iD])
                    print(KEY_WORD + h.name + " and " + w.name + " have their anniversary coming up! Family " + fam.iD)
        else:
            anniv = anniv.replace(year = today.year)
            if h.alive and w.alive and (today <= anniv <= month):
                output.append([h.iD, w.iD, fam.iD])
                print(KEY_WORD + h.name + " and " + w.name + " have their anniversary coming up! Family " + fam.iD)
    return output

'''
    This function loops through individuals in each family and 
    returns a list with the oldest family members
'''
def us43oldestFamilyMember(families, individuals):
    output = []
    age = 0
    for fam in families:
        for ind in individuals:
            if (ind.iD in fam.iD):
                if (ind.age > age):
                    age = ind.age
                    oldest = ind.name
        output.append(oldest)
    return output

'''
    This function loops through individuals in each family and 
    returns a list with the youngest family members
'''
def us44YoungestFamilyMembers(families, individuals):
    output = []
    age = 10000
    for fam in families:
        for ind in individuals:
            if (ind.iD in fam.iD):
                if (ind.age < age):
                    age = ind.age
                    youngest = ind.name
         output.append(youngest)
    return output


'''
    This function loops through individuals and makes sure that
    age exists and is greater than 0 and if there is an error outputs
    that there is a age <= 0 error returns list of id's with errors
'''
def us45AgeGreaterThan0(individuals):
  KEY_WORD = "ERROR: INDIVIDUALS: US45: "
  output = []
  for indi in individuals:
    isAgeLessThan0 = indi.age != "" and int(indi.age) < 0
    if isAgeLessThan0:
        print(KEY_WORD + indi.iD + ": Age " + indi.age + " is less than 0 or doesn't exist")
        output.append(indi.iD)
  return output

'''
    This function loops through individuals and lists unique lastnames
'''
def us46ListUniqueLastnames(individuals):
  KEY_WORD = "LIST: INDIVIDUALS: US46: "
  output = []
  for indi in individuals:
    lastname = indi.name.split(" ")[1]
    if lastname not in output:
        output.append(lastname)
  if len(output) > 0:
    print(KEY_WORD)
    for n in output:
      print("\t",n)
  return output
'''
    This functions loops through individuals and returns the list of individuals' ID's 
    who do not have a first name
'''
def us49IndiHaveFirstName(individuals):
    KEY_WORD = "LIST: US49: "
    output = []
    for indi in individuals:
        firstname = indi.name.split(" ")[0]
        if not isinstance(firstname, str) or firstname[0] == "/":
            print(KEY_WORD + indi.iD + ": First name is empty or doesnt exist")
            output.append(indi.iD)
    return output
'''
    This function loops through individuals and families and lists all families with at least 1 child
'''
def us50FamilyHasChild(individuals, families):
    KEY_WORD = "LIST: US50: "
    output = []
    for fam in families:
        if fam.children != [] and fam.children != "NA":
            print(KEY_WORD + fam.iD + ": Family has at least one child")
            output.append(fam.iD)
    return output
      

def findMaleChild(childID, individuals):
    for i in individuals:
        if i.iD == childID and i.gender == 'M':
            return True

def us51FamilyHasMaleChild(families, individuals):
    '''Lists all Families with at least 1 male child'''
    KEY_WORD = "List - US51: "
    output = []
    fams = [f for f in families if f.children != []]
    for fam in fams:
        for c in fam.children:
            if (findMaleChild(c.iD, individuals)):
                if fam.iD not in output:
                    output.append(str(fam.iD))
    return output

def us52DivorcedInTenYears(families, individuals):
    '''List all couples that divorced within 10 years of getting married'''
    KEY_WORD = "List - US52: "
    output = []
    fams = [f for f in families if f.divorced != "NA"]
    for fam in fams:
        marr = datetime.strptime(fam.married, '%d %b %Y')
        div = datetime.strptime(fam.divorced, '%d %b %Y')
        ten = marr + dateutil.relativedelta.relativedelta(years=10)
        if (marr <= div <= ten):
            output.append([fam.husbId, fam.wifeId, fam.iD])
            print(KEY_WORD + "Family " + fam.iD + " was divorced within ten years of marriage.")
    return output

def us53DivorcedInFiveYears(families, individuals):
    '''List all couples that divorced within 5 years of getting married'''
    KEY_WORD = "List - US53: "
    output = []
    fams = [f for f in families if f.divorced != "NA"]
    for fam in fams:
        marr = datetime.strptime(fam.married, '%d %b %Y')
        div = datetime.strptime(fam.divorced, '%d %b %Y')
        five = marr + dateutil.relativedelta.relativedelta(years=5)
        if (marr <= div <= five):
            output.append([fam.husbId, fam.wifeId, fam.iD])
            print(KEY_WORD + "Family " + fam.iD + " was divorced within five years of marriage.")
    return output

def us54DivorcedInFifteenYears(families, individuals):
    '''List all couples that divorced within 15 years of getting married'''
    KEY_WORD = "List - US54: "
    output = []
    fams = [f for f in families if f.divorced != "NA"]
    for fam in fams:
        marr = datetime.strptime(fam.married, '%d %b %Y')
        div = datetime.strptime(fam.divorced, '%d %b %Y')
        if (marr <= div <= (marr + dateutil.relativedelta.relativedelta(years=15))):
            output.append([fam.husbId, fam.wifeId, fam.iD])
            print(KEY_WORD + "Family " + fam.iD + " was divorced within fifteen years of marriage.")
    return output
