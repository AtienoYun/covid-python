def estimator(data):
  return data
class Covid:
  def __init__(impact,currentlyInfected, infectionsByRequestedTime):
     impact.currentlyInfected = currentlyInfected
     impact.infectionsByRequestedTime = infectionsByRequestedTime
  def __init__(severe,severeCurrentlyInfected , severeinfectionsByRequestedTime):
    severe.severeCurrentlyInfected = severeCurrentlyInfected
    severe.severeinfectionsByRequestedTime = severeinfectionsByRequestedTime
     
print('                COVID-19 ESTIMATOR')

##impact
print('          Non-Severe Cases')
data = eval(input('Enter Number of the infected persons : '))
currentlyInfected = data * 10
print ('Total Number of people infected on a daily basis is: ',currentlyInfected )
infectionsByRequestedTime = currentlyInfected * 1024
print('Total Number of people infected in a month is : ',infectionsByRequestedTime,)
print('15% of the Infected Person by the requested time ',infectionsByRequestedTime * (15/100))


##severe impact
severeCurrentlyInfected = data * 50
print('             ')
print ('        SEVERE CASES ')
print('Severe Cases: ',severeCurrentlyInfected)
severeinfectionsByRequestedTime= severeCurrentlyInfected * 1024
print('Severe Cases by requested time include: ',severeinfectionsByRequestedTime)
print('15% of the Infected Person by the requested time ',severeinfectionsByRequestedTime * (15/100))

##Hospital Beds available
print("                  ")
print("          Hospital Beds")
HospitalBeds = 500
print('Total Beds in the hospital:',HospitalBeds)
availablebeds = severeinfectionsByRequestedTime /HospitalBeds
print('Number of beds Available:',availablebeds)
hospitalBedsByRequestedTime = availablebeds
print('Hospitals Bed by the Requested Time:',hospitalBedsByRequestedTime /0.35)
##ICU, Ventilators and Economy failure
print("                  ")
print("          ICU Care Cases")
casesForICUByRequestedTime = (5/100) * infectionsByRequestedTime  
print('THat will require ICU Care',casesForICUByRequestedTime )
casesForVentilatorsByRequestedTime = (2/100) *infectionsByRequestedTime  
print('Casees that will require ventilators',casesForVentilatorsByRequestedTime)
dollarsInFlight = (infectionsByRequestedTime * 0.65) * 1.5 * 30
print('The amount of money the economy is likely to lose: ', dollarsInFlight)

def displayCovid(impact):
  print(impact.currentlyInfected)
  print(impact.infectionsByRequestedTime)
def displayCovid(severe):
  print(severe.severeCurrentlyInfected)
  print(severe.severeinfectionsByRequestedTime)
  
  print(casesForICUByRequestedTime)
  print(casesForVentilatorsByRequestedTime)
  print(dollarsInFlight)
