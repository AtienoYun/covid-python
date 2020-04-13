class Covid:
  def __init__(impact,currentlyInfected, infectionsByRequestedTime):
     impact.currentlyInfected = currentlyInfected
     impact.infectionsByRequestedTime = infectionsByRequestedTime
  def __init__(severe,severeCurrentlyInfected , severeinfectionsByRequestedTime):
    severe.severeCurrentlyInfected = severeCurrentlyInfected
    severe.severeinfectionsByRequestedTime = severeinfectionsByRequestedTime
     
  def displayCovid(impact):
   print(impact.currentlyInfected)
   print(impact.infectionsByRequestedTime)
  def displayCovid(severe):
   print(severe.severeCurrentlyInfected)
   print(severe.severeinfectionsByRequestedTime)
  
   print(casesForICUByRequestedTime)
   print(casesForVentilatorsByRequestedTime)
   print(dollarsInFlight)
