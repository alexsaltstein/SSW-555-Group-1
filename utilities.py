#This is the utilities script for how we are going to implement stories for each sprint
from datetime import datetime
from datetime import date
import dateutil.relativedelta

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
    # This needs to be fixed merp  merp
    #now = now.strftime('%d %b %Y') 
    # the now date time is not the right type to subtract
    dateStr = now.strftime("%d %b %Y ")
    now = datetime.strptime(dateStr, '%d %b %Y')
    for x in individuals:
        if (now - datetime.strptime(x.birthday, '%d %b %Y')).days <= 0:
            print(KEY_WORD + x.iD + ": Born " + x.birthday + " after today " + now)
            output.append(x.iD)
        if (now - datetime.strptime(x.death, '%d %b %Y')).days <= 0:
            print(KEY_WORD + x.iD + ": Died " + x.death + " after today " + now)
            output.append(x.iD)
    for y in families:
        if (now - datetime.strptime(y.married, '%d %b %Y')).days <= 0:
            print(KEY_WORD + x.iD + ": Married " + y.married + " after today " + now)
            output.append(y.iD)
        if ( now - datetime.strptime(y.divorced, '%d %b %Y')).days <= 0:
            print(KEY_WORD + x.iD + ": Died " + x.death + " after today " + now)
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
            if (indi.iD in fam.iD and (datetime.strptime(fam.married, '%d %b %Y') - datetime.strptime(indi.birthday, '%d %b %Y')).days <= 0):
                    print(KEY_WORD + fam.iD + ": Married " + fam.married + " after birth "  + indi.birthday)
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
        isDeathBeforeBirth = indi.death != "NA" and (datetime.strptime(indi.death, '%d %b %Y') - datetime.strptime(indi.birthday, '%d %b %Y')).days <= 0
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
        isDivorceBeforeMarriage = fam.divorced != "NA" and (datetime.strptime(fam.divorced, '%d %b %Y') - datetime.strptime(fam.married, '%d %b %Y')).days <= 0
        if isDivorceBeforeMarriage:
            print(KEY_WORD + fam.iD + ": Divorced " + fam.divorced + " before married " + fam.married)
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
            if (indi.iD in fam.children and (datetime.strptime(indi.birthday, '%d %b %Y') - datetime.strptime(fam.married, '%d %b %Y')).days <= 0):
                isBirthBeforeMarriage = True
                if isBirthBeforeMarriage:
                    print(KEY_WORD + fam.iD + ": Married " + fam.married + " after birth of " + indi.name + " on " + indi.birthday)
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
        listOfChildren = f.children     #List of strings of individual ids of children
        husband = f.husbId              #string of husband's individual id
        wife = f.wifeId                 #string of wife's individual id
        husbandDeath = findParentDeath(husband, listOfIndividuals)     #store husband's death date if applicable
        wifeDeath = findParentDeath(wife, listOfIndividuals)           #store wife's death date if applicable
        for c in listOfChildren:                                       #loop through list of children IDs
            childBirthday = findChildBday(c, listOfIndividuals)        #get child's birthday
            cBDatetime = datetime.strptime(childBirthday, "%d %b %Y")
            if wifeDeath is not None:                                   #check if wifeDeath exists
                wDDatetime = datetime.strptime(wifeDeath, "%d %b %Y")   #convert wife's death to datetime object from string
                if cBDatetime > wDDatetime:                             #if Mother's death date is before birth of child, not possible
                    print(KEY_WORD + "ANOMALY: Mother's death cannot come before Child's birth")
                    output.append(c)        #appends problematic child id to output
            if husbandDeath is not None:                                                           #check if husbandDeath exists
                hDDatetime = datetime.strptime(husbandDeath, "%d %b %Y")                           #convert husband's death to datetime object from string
                if (cBDatetime - dateutil.relativedelta.relativedelta(months=9)) > hDDatetime:     #left operand is conception date. if that's greater than the father's death date, that is impossible
                    print(KEY_WORD + "ANOMALY: Father's death cannot come after 9 months before Child's birth (Child's conception date)")
                    output.append(c)        #appends problematic child id to output
    return output

def us10MarriageAfter14(listOfFamilies, listOfIndividuals):
    output = []
    KEY_WORD = "ERROR: INDIVIDUALS: US10: "
    for f in listOfFamilies:
        husband = f.husbId
        wife = f.wifeId
        for i in listOfIndividuals:
            if (i.iD == husband or i.iD == wife) and (datetime.strptime(f.married, '%d %b %Y') - datetime.strptime(i.birthday, '%d %b %Y')).days/365 < 14:
                print(KEY_WORD + i.iD + " got married under the age of 14.")
                output.append(i.iD)
    return output