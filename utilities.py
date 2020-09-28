#This is the utilities script for how we are going to implement stories for each sprint
from datetime import datetime
from datetime import date

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
    for y in familes:
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