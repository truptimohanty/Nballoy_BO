# Nballoy_BO
Machine learning guided optimal composition selection for high strength Niobium alloy


# Python files and their information 

## Mechanical properties prediction peformance comparison between different models and different featurizaton: 

1. UTS_Oliynyk.ipynb : Python program file to compare perfromance in predicting UTS value for differnt ml models GBR, RF, SVR, KNN using Oliynyk feature

2. UTS_SelectedFeatures.ipynb : Python program file to compare perfromance in predicting UTS value for differnt ml models GBR, RF, SVR, KNN using domain knowledge based features

3. UTS_composition.ipynb : Python program file to compare perfromance in predicting UTS value for differnt ml models GBR, RF, SVR, KNN using atom percentage of alloying elements as features


4. YS_Oliynyk.ipynb : Python program file to compare perfromance in predicting YS value for differnt ml models GBR, RF, SVR, KNN using Oliynyk feature

5. YS_SelectedFeatures.ipynb : Python program file to compare perfromance in predicting YS value for differnt ml models GBR, RF, SVR, KNN using domain knowledge based features

6. YS_composition.ipynb : Python program file to compare perfromance in predicting YS value for differnt ml models GBR, RF, SVR, KNN using domain knowledge based features

## Candidate search for optimal alloy composition 

1. main_candidate_search_UTS_quaternary.ipynb : Python program file suggest the best quarternay alloy candidates for optimizing UTS  

2. main_candidate_search_YS_quaternary.ipynb : Python program file suggest the best quarternay alloy candidates for optimizing YS 

3. main_candidate_search_addition_quaternay.ipynb : Python program file suggest the best quarternay alloy candidates for optimizing composite target (addition)

4. main_candidate_search_Sqrt_quaternary.ipynb : Python program file suggest the best quarternay alloy candidates for optimizing composite target (Sqrt)

5. EI_Calculation_chunkwise.ipynb : Python program file to calcualte the EI values for large candidate size (quinary alloy having more than 74 million candidates)


## Other important python files 

1. Virtual_candidates_alloy_derivation.ipynb : Python program file for creating the virtual alloy candidates depending on different combinations such as quaternay/quinary/senary

2. Nb_strength_data_splitting_F.ipynb : Python program file for splitting the original data into different train/test datasets based on alloy uniqueness so that the alloy present in the training data should not repeat in the test dataset

3. performance_diff_traintest_split.ipynb : Python program file to compare the performance for differnt train/test split of the original alloy dataset

4. UMAP_All.ipynb : Pyhton program file to represent the alloy compostitons (Experimental as well as Suggested) in the two dimensional UMAP representations 

5. MOO_relationship.ipynb : Python program file to represent the relationship between YS, UTS and the composite properties for Multi Objective optimization 


## Required Packages
Python 3.9.6 <br>
numpy 1.20.3 <br>
scipy 1.7.0 <br>
pandas 1.3.0 <br>
matplotlib 3.4.2 <br>
seaborn 0.11.1 <br>
scikit-learn 0.24.2 <br>
umap-learn 0.5.2 
