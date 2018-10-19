from skfuzzy.membership import *
from skfuzzy import control as ctrl
import pandas as pd
import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot
import math

#Parse the dict to get all the inputs from the
def get_score(dict):
    kopidict=dict
    kopi_input= float(kopidict['kopi'])
    milk_input = float(kopidict['milk'])
    sugar_input = float(kopidict['sugar'])
    count=1

    #To set the universe range dynamically
    max_level=11
    # print("Max Level and count:")
    # print(max_level)
    # print(count)
    min_level=0
    milk_y = 0
    sugar_y = 0
    score = 0
    sugar_level= 11
    print("Milk Value:"+str(milk_input),end="\t")
    print("Sugar Value:"+str(sugar_input),end="\t")
    print("Kopi Value:"+str(kopi_input))
    # max_level=100

    """Kopi Level"""
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
    # print(kopi_bins)
    # print(kopi_HP_2,kopi_HP_1)
    kopi_thick=fuzz.smf(kopi.universe,kopi_HP_1,kopi_HP_2)
    kopi_norm=fuzz.trimf(kopi.universe,[kopi_TR_1,kopi_TR_2,kopi_TR_3])
    kopi_thin=fuzz.zmf(kopi.universe,kopi_LP_1,kopi_LP_2)
    kopi['thin']=kopi_thin
    kopi['norm']=kopi_norm
    kopi['thick']=kopi_thick
    # kopi.view()
    # pyplot.show()
    # print("Printing Kopi MFs:")
    # print(fuzz.interp_membership(kopi.universe,kopi_thin,kopi_input))
    # print(fuzz.interp_membership(kopi.universe,kopi_norm,kopi_input))
    # print(fuzz.interp_membership(kopi.universe,kopi_thick,kopi_input))

    """Milk Level"""
    milk_pre_bins = np.arange(0,1,0.1)
    milk_pre=ctrl.Antecedent(milk_pre_bins,'milk_pre')
    milk_pre_mf=fuzz.sigmf(milk_pre.universe,0.5,1)
    milk_pre['milk_pre']=milk_pre_mf
    #milk input value being passed as the last argument
    val_milk = fuzz.interp_membership(milk_pre.universe,milk_pre_mf,milk_input)
    # print("Milk MF:")
    # print(val_milk)

    if val_milk == 0.0:
        milk_y=1
        # print("Milk Required")
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
        milk_extra=fuzz.smf(milk.universe,milk_HP_1,milk_HP_2)
        milk_norm=fuzz.trimf(milk.universe,[milk_TR_1,milk_TR_2,milk_TR_3])
        milk_less=fuzz.zmf(milk.universe,milk_LP_1,milk_LP_2)
        milk['less']=milk_less
        milk['norm']=milk_norm
        milk['extra']=milk_extra
        milk_temp=fuzz.smf(milk_pre.universe,0.5,1)
        milk_pre['milk_pre']=milk_temp
        # milk.view()
        # pyplot.show()
        # print("Printing Milk MFs:")
        # print(fuzz.interp_membership(milk.universe,milk_less,milk_input))
        # print(fuzz.interp_membership(milk.universe,milk_norm,milk_input))
        # print(fuzz.interp_membership(milk.universe,milk_extra,milk_input))
        # print(fuzz.interp_membership(milk_pre.universe,milk_temp,milk_input))
    else:
        milk_y=0
        # print("No milk")
        milk_bins= np.arange(0,max_level,count)
        milk=ctrl.Antecedent(milk_bins,'milk')
        milk_mf=fuzz.smf(milk.universe,0.5,1)
        milk['less']=milk_mf
        milk['norm']=milk_mf
        milk['extra']=milk_mf
        milk_temp=fuzz.zmf(milk_pre.universe,0.5,1)
        milk_pre['milk_pre']=milk_temp
        # print(fuzz.interp_membership(milk.universe,milk_mf,milk_input))
        # print(fuzz.interp_membership(milk.universe,milk_mf,milk_input))
        # print(fuzz.interp_membership(milk.universe,milk_mf,milk_input))
        # print(fuzz.interp_membership(milk_pre.universe,milk_temp,milk_input))


    """Sugar Membership Function"""
    sugar_pre_bins = np.arange(0,1,0.1)
    sugar_pre=ctrl.Antecedent(sugar_pre_bins,'sugar_pre')
    sugar_pre_mf=fuzz.sigmf(sugar_pre.universe,0.5,1)
    sugar_pre['sugar_pre']=sugar_pre_mf
    #sugar input value being passed as the last argument
    val_sugar = fuzz.interp_membership(sugar_pre.universe,sugar_pre_mf,sugar_input)
    # print("Sugar MF:")
    # print(val_sugar)

    if val_sugar == 0.0:
        sugar_y = 1
        sugar_bins= np.arange(0,sugar_level,1)
        sugar=ctrl.Antecedent(sugar_bins,'sugar')
        # print("Sugar Required")
        sugar_extra=fuzz.smf(sugar.universe,6,8)
        sugar_norm=fuzz.trimf(sugar.universe,[3,5,7])
        sugar_less=fuzz.zmf(sugar.universe,2,4)
        sugar['norm']=sugar_norm
        sugar['extra']=sugar_extra
        sugar['less'] = sugar_less
        sugar_temp=fuzz.smf(sugar_pre.universe,0.5,1)
        sugar_pre['sugar_pre']=sugar_temp
        # sugar.view()
        # pyplot.show()
        # print(fuzz.interp_membership(sugar.universe,sugar_less,sugar_input))
        # print(fuzz.interp_membership(sugar.universe,sugar_norm,sugar_input))
        # print(fuzz.interp_membership(sugar.universe,sugar_extra,sugar_input))
        # print(fuzz.interp_membership(sugar_pre.universe,sugar_temp,sugar_input))
    else:
        sugar_y = 0
        sugar_bins= np.arange(0,sugar_level,1)
        sugar=ctrl.Antecedent(sugar_bins,'sugar')
        sugar_mf=fuzz.smf(sugar.universe,0.5,1)
        sugar['norm']=sugar_mf
        sugar['extra'] = sugar_mf
        sugar['less']= sugar_mf
        sugar_temp=fuzz.zmf(sugar_pre.universe,0.5,1)
        sugar_pre['sugar_pre']=sugar_temp
        # print(fuzz.interp_membership(sugar.universe,sugar_mf,sugar_input))
        # print(fuzz.interp_membership(sugar.universe,sugar_mf,sugar_input))
        # print(fuzz.interp_membership(sugar.universe,sugar_mf,sugar_input))
        # print(fuzz.interp_membership(sugar_pre.universe,sugar_temp,sugar_input))
        print("No Sugar")


    """Ouput Membership Function"""
    universe = np.linspace(-19, 19, 39)
    # print(universe)
    output = ctrl.Consequent(universe, 'output')
    # names = ['Kopi_O', 'Kopi_O_KoSong', 'Kopi_O_Siew_Dai', 'Kopi_O_Ga_Dai', 'Kopi_C','Kopi_C_Siew_Dai','Kopi_C_Ga_Dai','Kopi','Kopi_Gao','Kopi_C_Gau_Ga_Dai','Kopi_Po']
    names = ['KOPSD', 'KOP', 'KOPGD', 'KOSD', 'KOGD','KO','KOGSD','KOG','KOGGD','KOPK','KOK','KOGK','KP','KG','KDL','KPSD','KSD','KGSD','KP','KP','K','NA','KPGD','KGD','KGGD','KCPSD','KCSD','KCGSD','KCP','KC','KCG','KCPGD','KCGD','KCGGD','KCPK','KCK','KCGK','NA','NA']
    # print(len(names))
    out=output.automf(names=names)


    # Rules for zero milk and various sugar levels
    rule_1= ctrl.Rule(milk_pre['milk_pre'] & sugar['less'] & kopi['thin'], output['KOPSD'], label='KOPSD')
    rule_2= ctrl.Rule(milk_pre['milk_pre'] & sugar['norm'] & kopi['thin'], output['KOP'], label='KOP')
    rule_3= ctrl.Rule(milk_pre['milk_pre'] & sugar['extra'] & kopi['thin'], output['KOPGD'], label='KOPGD') #KOP
    rule_4= ctrl.Rule(milk_pre['milk_pre'] & sugar['less'] & kopi['norm'], output['KOSD'], label='KOSD') #KOPGD
    rule_5= ctrl.Rule(milk_pre['milk_pre'] & sugar['extra'] & kopi['norm'], output['KOGD'], label='KOGD')
    rule_6= ctrl.Rule(milk_pre['milk_pre'] & sugar['norm'] & kopi['norm'], output['KO'], label='KO')
    rule_7= ctrl.Rule(milk_pre['milk_pre'] & sugar['less'] & kopi['thick'], output['KOGSD'], label='KOGSD')
    rule_8= ctrl.Rule(milk_pre['milk_pre'] & sugar['norm'] & kopi['thick'], output['KOG'], label='KOG')
    rule_9= ctrl.Rule(milk_pre['milk_pre'] & sugar['extra'] & kopi['thick'], output['KOGGD'], label='KOGGD')

    # #Rules for zero sugar and zero milk
    rule_10= ctrl.Rule(milk_pre['milk_pre'] & sugar_pre['sugar_pre'] & kopi['thin'], output['KOPK'], label='KOPK')
    rule_11= ctrl.Rule(milk_pre['milk_pre'] & sugar_pre['sugar_pre'] & kopi['norm'], output['KOK'], label='KOK')
    rule_12= ctrl.Rule(milk_pre['milk_pre'] & sugar_pre['sugar_pre'] & kopi['thick'], output['KOGK'], label='KOGK')

    #Rules for no sugar and various milk levels (Normal and Less - Condensed)
    rule_13= ctrl.Rule((milk['less'] | milk['norm']) & sugar_pre['sugar_pre'] & kopi['thin'], output['KP'], label='KP')
    rule_14= ctrl.Rule((milk['less'] | milk['norm']) & sugar_pre['sugar_pre'] & kopi['norm'], output['KG'], label='KG')
    rule_15= ctrl.Rule((milk['less'] | milk['norm']) & sugar_pre['sugar_pre'] & kopi['thick'], output['KDL'], label='KDL')

    #Rules for various sugar levels and various milk levels (Normal and Less - Condensed)
    rule_16= ctrl.Rule((milk['less'] | milk['norm']) & sugar['less'] & kopi['thin'], output['KPSD'], label='KPSD')
    rule_17= ctrl.Rule((milk['less'] | milk['norm']) & sugar['less'] & kopi['norm'], output['KSD'], label='KSD')
    rule_18= ctrl.Rule((milk['less'] | milk['norm']) & sugar['less'] & kopi['thick'], output['KGSD'], label='KGSD')
    rule_19= ctrl.Rule((milk['less'] | milk['norm']) & sugar['norm'] & kopi['thin'], output['KP'], label='KP_1')
    rule_20= ctrl.Rule((milk['less'] | milk['norm']) & sugar['norm'] & kopi['norm'], output['K'], label='K')
    rule_21= ctrl.Rule((milk['less'] | milk['norm']) & sugar['norm'] & kopi['thick'], output['KG'], label='KG_1')
    rule_22= ctrl.Rule((milk['less'] | milk['norm']) & sugar['extra'] & kopi['thin'], output['KPGD'], label='KPGD') #KPGD
    rule_23= ctrl.Rule((milk['less'] | milk['norm']) & sugar['extra'] & kopi['norm'], output['KGD'], label='KGD') #KGD
    rule_24= ctrl.Rule((milk['less'] | milk['norm']) & sugar['extra'] & kopi['thick'], output['KGGD'], label='KGGD') #KGGD

    #Rules for various sugar and extra milk levels
    rule_25= ctrl.Rule(milk['extra'] & sugar['less'] & kopi['thin'], output['KCPSD'], label='KCPSD')
    rule_26= ctrl.Rule(milk['extra'] & sugar['less'] & kopi['norm'], output['KCSD'], label='KCSD')
    rule_27= ctrl.Rule(milk['extra'] & sugar['less'] & kopi['thick'], output['KCGSD'], label='KCGSD')
    rule_28= ctrl.Rule(milk['extra'] & sugar['norm'] & kopi['thin'], output['KCP'], label='KCP')
    rule_29= ctrl.Rule(milk['extra'] & sugar['norm'] & kopi['norm'], output['KC'], label='KC')
    rule_30= ctrl.Rule(milk['extra'] & sugar['norm'] & kopi['thick'], output['KCG'], label='KCG')
    rule_31= ctrl.Rule(milk['extra'] & sugar['extra'] & kopi['thin'], output['KCPGD'], label='KCPGD')
    rule_32= ctrl.Rule(milk['extra'] & sugar['extra'] & kopi['norm'], output['KCGD'], label='KCGD')
    rule_33= ctrl.Rule(milk['extra'] & sugar['extra'] & kopi['thick'], output['KCGGD'], label='KCGGD')

    #Rules for no sugar and extra milk levels
    rule_34= ctrl.Rule(milk['extra'] & sugar_pre['sugar_pre'] & kopi['thin'], output['KCPK'], label='KCPK')
    rule_35= ctrl.Rule(milk['extra'] & sugar_pre['sugar_pre'] & kopi['norm'], output['KCK'], label='KCK')
    rule_36= ctrl.Rule(milk['extra'] & sugar_pre['sugar_pre'] & kopi['thick'], output['KCGK'], label='KCGK')
    # rule_1.view()

    # print("Milk_y and Sugar_y:"+str(milk_y)+"   "+str(sugar_y))
    if milk_y == 0 and sugar_y == 1:
        # print("Rules for kopi without milk and various sugar levels")
        ctrl_sys= ctrl.ControlSystem([rule_1,rule_2,rule_3,rule_4,rule_5,rule_6,rule_7,rule_8,rule_9])
        # sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=35 * 35 + 1)
        sim = ctrl.ControlSystemSimulation(ctrl_sys)
        sim.input['kopi']= kopi_input
        sim.input['sugar']= sugar_input
        sim.input['milk_pre']= milk_input
        sim.compute()
        score = sim.output['output']
        # output.view(sim=sim)
        # pyplot.show()
    elif milk_y == 0 and sugar_y == 0:
        # print("Rules for kopi without milk and sugar ")
        ctrl_sys= ctrl.ControlSystem([rule_10,rule_11,rule_12])
        # sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=35 * 35 + 1)
        sim = ctrl.ControlSystemSimulation(ctrl_sys)
        sim.input['kopi']= kopi_input
        sim.input['sugar_pre']= sugar_input
        sim.input['milk_pre']= milk_input
        sim.compute()
        score = sim.output['output']
        # output.view(sim=sim)
        # pyplot.show()
    elif milk_y == 1 and sugar_y == 0:
        # print("Rules for kopi with milk and no sugar")
        ctrl_sys= ctrl.ControlSystem([rule_13,rule_14,rule_15,rule_34,rule_35,rule_36])
        # sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=35 * 35 + 1)
        sim = ctrl.ControlSystemSimulation(ctrl_sys)
        sim.input['kopi']= kopi_input
        sim.input['sugar_pre']= sugar_input
        sim.input['milk']= milk_input
        sim.compute()
        score = sim.output['output']
        # output.view(sim=sim)
        # pyplot.show()
    elif milk_y == 1 and sugar_y == 1:
        # print("Rules for kopi various levels of milk and sugar")
        ctrl_sys= ctrl.ControlSystem([rule_16,rule_17,rule_18,rule_19,rule_20,rule_21,rule_22,rule_23,rule_24,rule_25,rule_26,rule_27,rule_28,rule_29,rule_30,rule_31,rule_32,rule_33])
        # sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=35 * 35 + 1)
        sim = ctrl.ControlSystemSimulation(ctrl_sys)
        sim.input['kopi']= kopi_input
        sim.input['sugar']= sugar_input
        sim.input['milk']= milk_input
        sim.compute()
        score = sim.output['output']
        # output.view(sim=sim)
        # pyplot.show()

    # #Calculate fuzzy score output for determing the Kopi type
    # # score = fuzzyscore()
    # ctrl_sys= ctrl.ControlSystem([rule_1,rule_2,rule_3,rule_4,rule_5,rule_6,rule_7,rule_8,rule_9,rule_10,rule_11,rule_12,rule_13,rule_14,rule_15,rule_16,rule_17,rule_18,rule_19,rule_20,rule_21,rule_22,rule_23,rule_24,rule_25,rule_26,rule_27,rule_28,rule_29,rule_30,rule_31,rule_32,rule_33,rule_34,rule_35,rule_36])
    # sim = ctrl.ControlSystemSimulation(ctrl_sys, flush_after_run=35 * 35 + 1)


    # for i in range(1,11):
    #     print(fuzz.interp_membership(kopi.universe,kopi_thin,i))
    #     print(fuzz.interp_membership(kopi.universe,kopi_norm,i))
    #     print(fuzz.interp_membership(kopi.universe,kopi_thick,i))
    #     for j in range(1,11):
    #         print("milk")
    #         milk_input=j
    #         sugar_input=9
    #         print(fuzz.interp_membership(milk.universe,milk_less,milk_input))
    #         print(fuzz.interp_membership(milk.universe,milk_norm,milk_input))
    #         print(fuzz.interp_membership(milk.universe,milk_extra,milk_input))
    #         sim.input['kopi']= i
    #         sim.input['milk']= milk_input
    #         sim.input['milk_pre']= milk_input
    #         sim.input['sugar']= sugar_input
    #         sim.input['sugar_pre']= sugar_input
    #         sim.compute()
    #         score = sim.output['output']
    #         print(score)

    print("score = ",end="\t")
    print(score)
    #return (score)
    return names[int(round(score))+19]

"""
print(score)
kopi_check=round(score)
print("Final Kopi:", kopi_check)
# fig=ControlSystemVisualizer.view()
# fig.show()
"""
# f=open("results.txt","a")
# for i in range(1,11):
#     for j in range(0,11):
#         for k in range(0,11):
#             print(i,j,k)
#             score=get_score({'kopi':i,'milk':j,'sugar':k})
#             f.write(str(i)+","+str(j)+","+str(k)+","+str(score)+"\n")

