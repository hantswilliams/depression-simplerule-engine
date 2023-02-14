

## 1st var: season - is it winter, or not winter (winter == more depression)
## 2nd var: gender - male versus female (male == more depression)
## 3rd var: age - young versus old (young == more depression)

## this is a example text for checking github

def sad_decesion(season, gender, age):
    """
    this is a basic function that takes in 3 variables and returns a string
    the values are: 
    ::season
    ::gender
    ::age
    """

    ## if season = winter, then return true 
    if season == 'winter':
        seasonValue = True 
    else:
        seasonValue = False

    if gender == "male":
        genderValue = True
    else:
        genderValue = False

    if age == 'young':
        ageValue = True
    else:
        ageValue = False

    ## if any value is true, return 'there is risk', else return 'no risk'
    interpretedValues = [seasonValue, genderValue, ageValue]
    stringValuePos = 'there is risk - maybe take some vitD'
    stringValueNeg = 'no risk - or at least we dont think so...'


    if seasonValue == True or genderValue == True or ageValue == True:
        return interpretedValues, stringValuePos

    else:
        return interpretedValues, stringValueNeg

    
sad_decesion(season='summer', gender='female', age='adult')
  
returnA, returnB = sad_decesion(season='summer', gender='female', age='adult')

returnA 

returnB
