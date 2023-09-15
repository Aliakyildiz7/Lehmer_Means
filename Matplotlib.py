from Lehmer_Means import lehmer_mean
import matplotlib.pyplot as plt
#import numpy as np

#User Panel(You can adjust the values under this panel to see different scenarios)
X = [10, 20, 30] #The series whomst lehmer means will be calculated
p_lower = -2#Lower limit of the p value
sensitivity = 0.2 #Increment of p in each iteration
p_upper = 2 + 0.005 #Upper limit of the p value

#Explanation for Upper Limit
    #Choosing the p_upper exactly is bound to cause floating point error(e.g. 0.1 + 0.2 = 0.30000000000000004)
    #So we must chose it greater than the exact value of the desired p_upper value.
    #But that excession should be lower than sensitivy not to cause overshoot
    #But then again, it is not guaranteed to work if sensitivity is smaller than floating point error(Unlikely but possible)


P = [] #Matrice  to save p values
L = [] #Matrice to save lehmer_means

p = p_lower
while p <= p_upper:
    P.append(p)
    L.append(lehmer_mean(*X, p=p))

    p += sensitivity


plt.figure(figsize=(12, 6))
plt.plot(P, L, marker="*", label="Lehmer Means", color="blue")

#I want to mark every point that has been calculated
plt.xticks(P)
plt.yticks(L)

#Marking the critical points
Dict = {1: "Arithmetic Mean", 0.5: "Geometric Mean", 0: "Harmonic  Mean"}
for num in Dict:
    critical_x = num
    critical_y = lehmer_mean(*X, p=critical_x)

    plt.annotate(Dict[num], xy=(critical_x, critical_y), xytext=(p_lower, critical_y),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    print(f"{Dict[num]} of the series {X} is {critical_y}")


#Very inefficient way (recalculates every xtick point) to mark points but can be done for any xtickslist.
"""
tick_list=list(range(p_lower, p_upper, 1))
plt.xticks(tick_list)
plt.yticks(list(map(lambda x: lehmer_mean(*X, p=x), tick_list)))
"""

plt.title(f"Lehmer means of the series {X}")
plt.xlabel("p values")

plt.grid()

plt.show()

