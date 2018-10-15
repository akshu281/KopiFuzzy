from skfuzzy.membership import *
from skfuzzy import control as ctrl
import pandas as pd
import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot

#Parse the dict to get all the inputs from the UI
kopidict={'kopi':10,'milk':0,'sugar':0}
kopi_input= kopidict['kopi']*10
milk_input = kopidict['milk']*10
sugar_input = kopidict['sugar']
max_level_temp=kopi_input+milk_input
count=kopidict['kopi']+kopidict['milk']

#To set the universe range dynamically
max_level=max_level_temp+count
print("Max Level and count:")
print(max_level)
print(count)
min_level=1
milk_y = 0
sugar_y = 0
# max_level=100

"""Kopi Level"""

# kopi_LP_1= mid_kopi//3
# kopi_TR_1= (mid_kopi+kopi_LP_1)//2
# kopi_LP_2=(mid_kopi+kopi_TR_1)//2
# kopi_TR_2= mid_kopi
# kopi_LP_2= (mid_kopi+kopi_TR_1)//2
# kopi_HP_2= (max_level//2)+mid_kopi
# # kopi_TR_3= (mid_kopi+kopi_HP_2)//3+mid_kopi
# kopi_TR_3= (kopi_HP_2+mid_kopi)//4+mid_kopi
# kopi_HP_1= (mid_kopi+kopi_TR_3)//2

kopi_bins= np.arange(0,max_level,count)
kopi=ctrl.Antecedent(kopi_bins,'kopi')
mid_kopi = max_level//2
kopi_LP_1=(min_level+mid_kopi)//5
kopi_LP_2=(kopi_LP_1+mid_kopi)//2
kopi_TR_1= mid_kopi//2
kopi_TR_2=mid_kopi
kopi_TR_3=kopi_TR_1+kopi_TR_2
kopi_HP_1=(max_level+mid_kopi)//2.5
kopi_HP_2=(max_level+mid_kopi)//5 + mid_kopi

kopi_thick=fuzz.smf(kopi.universe,kopi_HP_1,kopi_HP_2)
kopi_norm=fuzz.trimf(kopi.universe,[kopi_TR_1,kopi_TR_2,kopi_TR_3])
kopi_thin=fuzz.zmf(kopi.universe,kopi_LP_1,kopi_LP_2)
kopi['thin']=kopi_thin
kopi['norm']=kopi_norm
kopi['thick']=kopi_thick
# print(kopi_LP_1)
# print(kopi_LP_2)
# print(kopi_HP_1)
# print(kopi_HP_2)
# print(kopi_TR_1)
# print(kopi_TR_2)
# print(kopi_TR_3)
kopi.view()
pyplot.show()
print("Printing Kopi MFs:")
print(fuzz.interp_membership(kopi.universe,kopi_thin,kopi_input))
print(fuzz.interp_membership(kopi.universe,kopi_norm,kopi_input))
print(fuzz.interp_membership(kopi.universe,kopi_thick,kopi_input))

"""Milk Level"""

milk_pre_bins = np.arange(0,1,0.1)
milk_pre=ctrl.Antecedent(milk_pre_bins,'milk_pre')
milk_pre_mf=fuzz.sigmf(milk_pre.universe,0.5,1)
milk_pre['milk_pre']=milk_pre_mf
#milk input value being passed as the last argument
val_milk = fuzz.interp_membership(milk_pre.universe,milk_pre_mf,milk_input) 
print("Milk MF:")
print(val_milk)

milk_bins= np.arange(0,max_level,count)
# print(milk_bins)
milk=ctrl.Antecedent(milk_bins,'milk')

if val_milk == 0.0:
    milk_y=1
    print("Milk Required")
    mid_milk = max_level//2
    milk_LP_1=(min_level+mid_milk)//5
    milk_LP_2=(milk_LP_1+mid_milk)//2
    milk_TR_1= mid_milk//2
    milk_TR_2=mid_milk
    milk_TR_3=milk_TR_1+milk_TR_2
    milk_HP_1=(max_level+mid_milk)//2.5
    milk_HP_2=(max_level+mid_milk)//5 + mid_milk
    milk_more=fuzz.smf(milk.universe,milk_HP_1,milk_HP_2)
    milk_medium=fuzz.trimf(milk.universe,[milk_TR_1,milk_TR_2,milk_TR_3])
    milk_less=fuzz.zmf(milk.universe,milk_LP_1,milk_LP_2)
    milk['less']=milk_less
    milk['medium']=milk_medium
    milk['more']=milk_more
    milk.view()
    pyplot.show()
    print("Printing Milk MFs:")
    print(fuzz.interp_membership(milk.universe,milk_less,milk_input))
    print(fuzz.interp_membership(milk.universe,milk_medium,milk_input))
    print(fuzz.interp_membership(milk.universe,milk_more,milk_input))
else:
    milk_y=0
    # milk['zero']= val_milk
    print("No milk")

# mid_milk = max_level//2
# milk_LP_1= mid_milk//3
# milk_TR_1= (mid_milk+milk_LP_1)//2
# milk_LP_2=(mid_milk+milk_TR_1)//2
# milk_TR_2= mid_milk
# milk_LP_2= (mid_milk+milk_TR_1)//2
# # milk_HP_2= (max_level//3)+mid_milk
# milk_HP_2= (max_level//2)+mid_milk
# # milk_TR_3= (mid_milk+milk_HP_2)//3+mid_milk
# milk_TR_3= (mid_milk+milk_HP_2)//4+mid_milk
# milk_HP_1= (mid_milk+milk_TR_3)//2

"""Sweetness Membership Function"""

sugar_pre_bins = np.arange(0,1,0.1)
sugar_pre=ctrl.Antecedent(sugar_pre_bins,'sugar_pre')
sugar_pre_mf=fuzz.sigmf(sugar_pre.universe,0.5,1)
sugar_pre['sugar_pre']=sugar_pre_mf
#sugar input value being passed as the last argument
val_sugar = fuzz.interp_membership(sugar_pre.universe,sugar_pre_mf,sugar_input) 
print("Sugar MF:")
print(val_sugar)

sugar_bins= np.arange(0,10,0.5)
sugar=ctrl.Antecedent(sugar_bins,'sugar')

if val_sugar == 0.0:
    sugar_y = 1
    print("Sugar Required")
    sugar_extra=fuzz.smf(sugar.universe,6,8)
    sugar_norm=fuzz.trimf(sugar.universe,[3,5,7])
    sugar_less=fuzz.zmf(sugar.universe,2,4)
    # sugar_pre= 0
    # sugar['zero']=sugar_pre
    sugar['norm']=sugar_norm
    sugar['extra']=sugar_extra
    sugar['less'] = sugar_less
    # sugar.view()
    # pyplot.show()
    print(fuzz.interp_membership(sugar.universe,sugar_less,sugar_input))
    print(fuzz.interp_membership(sugar.universe,sugar_norm,sugar_input))
    print(fuzz.interp_membership(sugar.universe,sugar_extra,sugar_input))
else:
    sugar_y = 0
    # sugar['zero'] = sugar_pre
    print("No Sugar")
    
"""Ouput Membership Function"""

# output=ctrl.Consequent(np.arange(0,1,0.1),'output')
# output=fuzz.sigmf(output.universe,0.5,1)
# output['Kopi_O']=output
# output['Kopi_O_KoSong']=output
# output['Kopi_O_Siew_Dai']=output
# output['Kopi_O_Ga_Dai']=output
# output['Kopi_C']=output
# output['Kopi_C_Siew_Dai']=output
# output['Kopi_C_Ga_Dai']=output
# output['Kopi']=output
# output['Kopi_Gao']=output
# output['Kopi_Di_Lo']=output
# output['Kopi_Poh']=output

universe = np.linspace(-5, 5, 11)
output = ctrl.Consequent(universe, 'output')
names = ['Kopi_O', 'Kopi_O_KoSong', 'Kopi_O_Siew_Dai', 'Kopi_O_Ga_Dai', 'Kopi_C','Kopi_C_Siew_Dai','Kopi_C_Ga_Dai','Kopi','Kopi_Gao','Kopi_Di_Lo','Kopi_Poh']
output.automf(names=names)

# output.view()
# pyplot.show()

# Rules for zero milk and various sugar levels
rule_1= ctrl.Rule(milk_pre['milk_pre'] & sugar['less'] & kopi['thick'], output['Kopi_O'], label='Kopi_O')
rule_2= ctrl.Rule(milk_pre['milk_pre'] & sugar['less'] & kopi['norm'], output['Kopi_O_Siew_Dai'], label='Kopi_O_Siew_Dai')
rule_3= ctrl.Rule(milk_pre['milk_pre'] & sugar['extra'] & kopi['norm'], output['Kopi_O_Ga_Dai'], label='Kopi_O_Ga_Dai')

#Rules for zero sugar and zero milk
rule_4= ctrl.Rule(milk_pre['milk_pre'] & sugar_pre['sugar_pre'] & kopi['norm'], output['Kopi_O_KoSong'], label='Kopi_O_KoSong')

#Rules for zero sugar and various milk levels
# rule_5= rule_4= ctrl.Rule(milk_pre['milk_pre'] & sugar_pre['sugar_pre'] & kopi['norm'], output['Kopi_O_KoSong'], label='Kopi')
# rule_6= rule_4= ctrl.Rule(milk_pre['milk_pre'] & sugar_pre['sugar_pre'] & kopi['norm'], output['Kopi_O_KoSong'], label='Kopi Gao')
# rule_7= rule_4= ctrl.Rule(milk_pre['milk_pre'] & sugar_pre['sugar_pre'] & kopi['norm'], output['Kopi_O_KoSong'], label='Kopi Di Lo')

#Rules for various sugar and milk levels 
#rule_=

def fuzzyscore():
    #Check with direct input variable or flag !?!
    if milk_y == 0.0 and sugar_y == 1.0:
        print("Rules for kopi without milk and various sugar levels")
        ctrl_sys= ctrl.ControlSystem([rule_1,rule_2,rule_3])
        sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=21 * 21 + 1)
        sim.input['kopi']= kopi_input
        sim.input['sugar']= sugar_input
        sim.input['milk_pre']= milk_input
        sim.compute()
        return(sim.output['output'])
    elif milk_y == 0.0 and sugar_y == 0.0:
        print("Rules for kopi without milk and no sugar ")
    elif milk_y == 1.0 and sugar_y == 0.0:
        print("Rules for kopi with milk and no sugar")
        # ctrl_sys= ctrl.ControlSystem([rule_,rule_,rule_])
        # sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=21 * 21 + 1)
        # sim.input['kopi']= kopi_input
        # sim.input['sugar']= sugar_input
        # sim.input['milk']= milk_input
        # sim.compute()
        # return(sim.output['output'])
    elif milk_y == 1.0 and sugar_y == 1.0:
        print("Rules for kopi various levels of milk and sugar")

#Calculate fuzzy score output for determing the Kopi type
score = fuzzyscore()
print(score)
kopi_check=round(score)

# Assign and return the Kopi type based on the fuzzified inputs
if kopi_check == -5:
    print("Kopi_O")
elif kopi_check == -4:
    print("Kopi_O_KoSong")
elif kopi_check == -3:
    print("Kopi_O_Siew_Dai")
elif kopi_check == -2:
    print("Kopi_O_Ga_Dai")
# else if kopi_check == -1:
#     print("")