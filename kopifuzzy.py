from skfuzzy.membership import *
from skfuzzy import control as ctrl
import pandas as pd
import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot

#Parse the dict to get all the inputs from the UI
kopidict={'kopi':10,'milk':0,'sugar':10}
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
score = 0
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
# kopi.view()
# pyplot.show()
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

if val_milk == 0.0:
    milk_y=1
    print("Milk Required")
    milk_bins= np.arange(0,max_level,count)
    milk=ctrl.Antecedent(milk_bins,'milk')
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
    milk_bins= np.arange(0,1,0.1)
    milk=ctrl.Antecedent(milk_bins,'milk')
    milk_mf=fuzz.sigmf(milk.universe,0.5,1)
    milk['less']=milk_mf
    milk['medium']=milk_mf
    milk['more']=milk_mf
    print(fuzz.interp_membership(milk.universe,milk_mf,milk_input))
    print(fuzz.interp_membership(milk.universe,milk_mf,milk_input))
    print(fuzz.interp_membership(milk.universe,milk_mf,milk_input))
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

if val_sugar == 0.0:
    sugar_y = 1
    sugar_bins= np.arange(0,11,0.5)
    sugar=ctrl.Antecedent(sugar_bins,'sugar')
    print("Sugar Required")
    sugar_extra=fuzz.smf(sugar.universe,6,8)
    sugar_norm=fuzz.trimf(sugar.universe,[3,5,7])
    sugar_less=fuzz.zmf(sugar.universe,2,4)
    # sugar_pre= 0
    # sugar['zero']=sugar_pre
    sugar['norm']=sugar_norm
    sugar['extra']=sugar_extra
    sugar['less'] = sugar_less
    sugar.view()
    pyplot.show()
    print(fuzz.interp_membership(sugar.universe,sugar_less,sugar_input))
    print(fuzz.interp_membership(sugar.universe,sugar_norm,sugar_input))
    print(fuzz.interp_membership(sugar.universe,sugar_extra,sugar_input))
else:
    sugar_y = 0
    # sugar['zero'] = sugar_pre
    sugar_bins= np.arange(0,1,0.1)
    sugar=ctrl.Antecedent(sugar_bins,'sugar')
    sugar_mf=fuzz.sigmf(sugar.universe,0.5,1)
    sugar['norm']=sugar_mf
    sugar['extra'] = sugar_mf
    sugar['less']= sugar_mf
    print(fuzz.interp_membership(sugar.universe,sugar_mf,sugar_input) )
    print(fuzz.interp_membership(sugar.universe,sugar_mf,sugar_input))
    print(fuzz.interp_membership(sugar.universe,sugar_mf,sugar_input) )
    print("No Sugar")
    
"""Ouput Membership Function"""
universe = np.linspace(-5, 5, 11)
output = ctrl.Consequent(universe, 'output')
names = ['Kopi_O', 'Kopi_O_KoSong', 'Kopi_O_Siew_Dai', 'Kopi_O_Ga_Dai', 'Kopi_C','Kopi_C_Siew_Dai','Kopi_C_Ga_Dai','Kopi','Kopi_Gao','Kopi_C_Gau_Ga_Dai','Kopi_Po']
output.automf(names=names)
# output.view()
# pyplot.show()

print("Milk_y and Sugar_y:"+str(milk_y)+"   "+str(sugar_y))
# Rules for zero milk and various sugar levels
rule_1= ctrl.Rule(milk_pre['milk_pre'] & sugar['norm'] & kopi['norm'], output['Kopi_O'], label='Kopi_O')
rule_2= ctrl.Rule(milk_pre['milk_pre'] & sugar['less'] & kopi['norm'], output['Kopi_O_Siew_Dai'], label='Kopi_O_Siew_Dai')
rule_3= ctrl.Rule(milk_pre['milk_pre'] & sugar['extra'] & kopi['norm'], output['Kopi_O_Ga_Dai'], label='Kopi_O_Ga_Dai')

#Rules for zero sugar and various milk levels
rule_4= ctrl.Rule(milk['less'] & sugar_pre['sugar_pre'] & kopi['norm'], output['Kopi'], label='Kopi')
rule_5= ctrl.Rule(milk['less'] & sugar_pre['sugar_pre'] & kopi['thick'], output['Kopi_Gao'], label='Kopi_Gao')

#Rules for various sugar and milk levels 
rule_6= ctrl.Rule(milk['medium'] & sugar['norm'] & kopi['norm'], output['Kopi_C'], label='Kopi_C')
rule_7= ctrl.Rule(milk['medium'] & sugar['less'] & kopi['norm'], output['Kopi_C_Siew_Dai'], label='Kopi_C_Siew_Dai')
rule_8= ctrl.Rule(milk['medium'] & sugar['extra'] & kopi['norm'], output['Kopi_C_Ga_Dai'], label='Kopi_C_Ga_Dai')
rule_9= ctrl.Rule(milk['more'] & sugar['extra'] & kopi['thick'], output['Kopi_C_Gau_Ga_Dai'], label='Kopi_C_Gau_Ga_Dai')
rule_10= ctrl.Rule(milk['less'] & sugar['extra'] & kopi['thin'], output['Kopi_Po'], label='Kopi_Po')
#rule_11= ctrl.Rule(milk['extra'] & sugar['less'] & kopi['thin'], output['Kopi_C_Po_Siew_Dai'], label='Kopi_C_Po_Siew_Dai')

#Rules for zero sugar and zero milk
rule_11= ctrl.Rule(milk_pre['milk_pre'] & sugar_pre['sugar_pre'] & kopi['norm'], output['Kopi_O_KoSong'], label='Kopi_O_KoSong')
rule_12= ctrl.Rule(milk_pre['milk_pre'] & sugar_pre['sugar_pre'] & kopi['thick'], output['Kopi_O_KoSong'], label='Kopi_O_KoSong')

# print("Milk_y and Sugar_y:"+str(milk_y)+"   "+str(sugar_y))
if milk_y == 0 and sugar_y == 1:    	
    print("Rules for kopi without milk and various sugar levels")
    ctrl_sys= ctrl.ControlSystem([rule_1,rule_2,rule_3])
    sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=21 * 21 + 1)
    sim.input['kopi']= kopi_input
    sim.input['sugar']= sugar_input
    sim.input['milk_pre']= milk_input
    sim.compute()
    score = sim.output['output']
elif milk_y == 0 and sugar_y == 0:
    print("Rules for kopi without milk and sugar ")
    ctrl_sys= ctrl.ControlSystem([rule_11,rule_12])
    sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=21 * 21 + 1)
    sim.input['kopi']= kopi_input
    sim.input['sugar_pre']= sugar_input
    sim.input['milk_pre']= milk_input
    sim.compute()
    score = sim.output['output']
elif milk_y == 1 and sugar_y == 0:
    print("Rules for kopi with milk and no sugar")
    ctrl_sys= ctrl.ControlSystem([rule_4,rule_5])
    sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=21 * 21 + 1)
    sim.input['kopi']= kopi_input
    sim.input['sugar_pre']= sugar_input
    sim.input['milk']= milk_input
    sim.compute()
    score = sim.output['output']
elif milk_y == 1 and sugar_y == 1:
    print("Rules for kopi various levels of milk and sugar")
    ctrl_sys= ctrl.ControlSystem([rule_6,rule_7,rule_8,rule_9,rule_10])
    sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=21 * 21 + 1)
    sim.input['kopi']= kopi_input
    sim.input['sugar']= sugar_input
    sim.input['milk']= milk_input
    sim.compute()
    score = sim.output['output']

#Calculate fuzzy score output for determing the Kopi type
# score = fuzzyscore()
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
elif kopi_check == -1:
    print("Kopi_C")
elif kopi_check == -0:
    print("Kopi_C_Siew_Dai")
elif kopi_check == 1:
    print("Kopi_C_Ga_Dai")
elif kopi_check == 2:
    print("Kopi")
elif kopi_check == 3:
    print("Kopi_Gao")
elif kopi_check == 4:
    print("Kopi_C_Gau_Ga_Dai")
elif kopi_check == 5:
    print("Kopi_Po")
elif kopi_check == 6:
    print("Kopi_C_Po_Siew_Dai")