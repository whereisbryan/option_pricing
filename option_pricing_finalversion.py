#%%
from random import *
from math import *
import numpy as nm
import matplotlib.pyplot as mpl


rf=0.00017
time_d=1
vol=0.0381
repet = 100000
days = 11
k1 = 35
k2= 45
PV_tot=[]
PV_last=[]
payoff=[]
u=exp(vol*sqrt(time_d))
d=1/u
p=(exp(rf*time_d)-d)/(u-d)
last_price=[]
jack=0

for i in range(repet):
    init_price=39.56
    pathprice = []
    for j in range(days):
        evolution = random()
        if evolution<p:
            init_price=init_price*u
        else:
            init_price=init_price*d

        pathprice.append(init_price)

    last_price.append(init_price)
    jack=jack+1
    if jack>99:
        mpl.plot(pathprice)
        jack=0


for finale in last_price:
    if finale < k1 :
        payoff.append(0)
    if finale>k2:
        payoff.append(25)
    if finale >= k1 and finale <= k2:
        payoff.append(finale-20)

for discount in payoff:
    PV_last=discount*exp(-rf*days)
    PV_tot.append(PV_last)


average = sum(PV_tot) / float(len(PV_tot))
print('The average discounted option payoff is:', average)
print('max price is:',max(last_price))
mpl.show()


# %%
