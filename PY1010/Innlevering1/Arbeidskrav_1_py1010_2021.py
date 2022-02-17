# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:36:41 2021

@author: Lars Holen (244697@student.usn.no)

"""

# %% Defining and calculating variables

totalKmDriven = 10000 # Antatt kjørelengde aarlig 

elInsurance = 5000 #Aarlig forsikring elbil
gasInsurance = 7000 #Aarlig forsikring bensinbil

elTrafficInsurance = 5.85 * 365 # el bil daglig trafikkforsikring * 365 days
gasTrafficInsurance = 8.4 * 365  # bensin bil daglig trafikkforsikring * 365 days

elFuelCost = 0.2 * 0.6 * totalKmDriven # Total drivstoffutgift på 10000km
gasFuelCost = 1 * totalKmDriven # Total drivstoffutgift på 10000km

elTollCost = 0.1 * totalKmDriven #bom avgifter på 10000km
gasTollCost = 0.3 * totalKmDriven #bom avgifter på 10000km

elTotal = elInsurance + elTrafficInsurance + elFuelCost + elTollCost #utgifter sammenlagt
gasTotal = gasInsurance + gasTrafficInsurance + gasFuelCost + gasTollCost #utgifter sammenlagt

defTotal = gasTotal - elTotal #forskjell i utgifter mellom bensin og el bil

# %% Print to screen

print("Gas car cost pr year: ", gasTotal, " NOK")
print("Eletric car cost pr year: ", elTotal, " NOK")
if defTotal > 0:
    print("Gas car cost ", defTotal, " NOK more than eletric car.")
elif defTotal < 0:
    print("Eletric cast cost", -defTotal, " NOK more than gas car.")
else:
    print("They cost the same")