# This is the utilities script for how we are going to implement stories for each sprint
from datetime import datetime
from datetime import date
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
    '''Families have a list of children. The list contains the individual IDs for each child
        For example: Family ID: F1 has Children with IDs: ['I1', 'I4', 'I5']

        This function loops through the list of families provided through the function call and stores
        the list of children ids, the husband id, and the wife id of one family at each iteration.
        On the same iteration, also finds the death dates of each parent if applicable with the use
        of a helper function called "findParentDeath". After getting this information, on the same
        iteration the function then loops through the now collected list of child ids and finds one child's
        birthday per iteration.  The birthday stored is then converted to datetime object format.
        The program then checks if the husband's or wife's death date indeed exists and if so converts
        this death date to datetime object format, and then does the
        appropriate comparison between the stored child birthdate and the specific parent death date.
        If the mother's death date predates the child's birthday, this is an anomaly and the program prints
        an according error message and collects the problematic child id in a list called "output".  If the father's
        death date predates 9 months before the child was born, this is an anomaly and the program prints
        an according error message and collects the problematic child id in a list called "output".  Once the function
        is finished looping through the provided list of families, it returns the output list of the problematic child ids
        collected throughout the iterations.'''
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
    for family in families:
        hid = family.husbId
        wid = family.wifeId
        families.remove(family)

        for fam in families:
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
