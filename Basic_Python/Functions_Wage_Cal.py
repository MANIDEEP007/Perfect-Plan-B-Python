'''
Rewrite your pay computation and create a function called computeTotalpay which takes two parameters
(days and rate) and returns computed pay as answer. Enter Days: 45. Enter Rate: 10. Pay: 450.0
'''
def computeTotalpay(days,rate):
    try:
        float(days)
        float(rate)
    except:
        return "Error in Input. Days and Rate Should be Numbers"
    return "Pay is " + str(float(days * rate))

print(computeTotalpay(45,10))
