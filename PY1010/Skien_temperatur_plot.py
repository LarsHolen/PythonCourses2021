# -*- coding: utf-8 -*-
"""
    Monthly Temperatures in Skien
    
    Temperatures are median temperatures 2005-2016
    http://www.timeanddate.no/vaer/norge/skien/klima
    
    By Lars Holen (244697@student.usn.no)
    
    Date 1. february 2021
    
    (Original script from Finn Andre Haugen(finn.haugen@usn.no))
"""


# %% Import av pakker:
    
import numpy as np
import matplotlib.pyplot as plt


# %% Definisjoner av variabler

mnd = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # mnd nummer
tempCelcius = np.array([-3,-2,2,7,11,15,17,16,12,6,2,-3]) # grader C
tempFarenheit = tempCelcius*(9/5) +32

"""
# %% Gjøre om Temperaturer fra Celcius til Farenheit
for i, tmp in enumerate(temp):
    print("Celcius: ", temp[i])
    temp[i] = tmp * (9/5) + 32
    print("Farenheit: ", temp[i])
"""




# %% Bergeninger av middelverdi:
    
mean_temp_celcius = np.mean(tempCelcius)
mean_temp_farenheit = np.mean(tempFarenheit)
print("Middelverdi av alle mnd temp in celcius = ", mean_temp_celcius)
print("Middelverdi av alle mnd temp = ", mean_temp_farenheit)


# %% Plottingen av verdiene:
    
plt.close("all")
plt.figure(1)
plt.plot(mnd, tempFarenheit, "go-")
plt.plot(mnd,tempFarenheit*0 + mean_temp_farenheit, "r")
plt.xlim(1,12)
#plt.ylim(min(tempFarenheit) - 10, max(tempFarenheit) + 10)
plt.title("Median temperature in Skien 2005-2016")
plt.xlabel("Month #")
plt.ylabel("Degrees Farenheit")
plt.grid()
plt.legend(labels=("Monthly avg.", "Yearly avg."))
plt.show()



