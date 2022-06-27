#!/usr/bin/env python
# coding: utf-8

# In[8]:


from cbfv.composition import _fractional_composition
import pandas as pd       
####### saving the element and their corresponding atomic weight in a dictionary ############
ele_weight = pd.read_csv('data/element_atweight.csv')
ele_wt_dict = dict(ele_weight.values)


############## function for converting atomic fraction to weight fraction and viceversa ###########
def atfrac_To_wtfrac(formula):
    
    frac_dict = _fractional_composition(formula)

    s = {k: ele_wt_dict[k]*v for k,v in frac_dict.items()}
    sum_weight =  sum(s.values())     
    
    s = {k: round((s[k]/sum_weight),3)for k in s}
        
    return(''.join([''.join((k,str(v))) for k,v in s.items()]))


def atpct_To_wtpct(formula):
    
    frac_dict = _fractional_composition(formula)

    s = {k: ele_wt_dict[k]*v for k,v in frac_dict.items()}
    sum_weight =  sum(s.values())     
    
    s = {k: round(round(s[k]/sum_weight,3)*100,3) for k in s}
        
    return(''.join([''.join((k,str(v))) for k,v in s.items()]))
    
        
def wtfrac_To_atfrac(formula):
    frac_dict = _fractional_composition(formula)

    s={k: v/ele_wt_dict[k] for k,v in frac_dict.items()} 
    sum_atoms = sum(s.values())
    
    s = {k: round(s[k]/sum_atoms,3) for k in s}   
    return(''.join([''.join((k,str(v))) for k,v in s.items()]))


def wtpct_To_atpct(formula):
    
    frac_dict = _fractional_composition(formula)

    s={k: v/ele_wt_dict[k] for k,v in frac_dict.items()} 
    sum_atoms = sum(s.values())
    
    s = {k: round(round(s[k]/sum_atoms,3)*100,3) for k in s}   
    #s = {k: round((s[k]/sum_atoms)*100,3) for k in s}   
    return(''.join([''.join((k,str(v))) for k,v in s.items()]))
      
    
    

