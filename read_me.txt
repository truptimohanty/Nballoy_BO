


Mechanical properties prediction performance comparison between different models and different featurizaton: 

1. UTS_Oliynyk.ipynb : Python program file to compare performance in predicting UTS value for different ml models GBR, RF, SVR, KNN using Oliynyk feature

2. UTS_SelectedFeatures.ipynb : Python program file to compare performance in predicting UTS value for different ml models GBR, RF, SVR, KNN using domain knowledge based features

3. UTS_composition.ipynb : Python program file to compare performance in predicting UTS value for different ml models GBR, RF, SVR, KNN using atom percentage of alloying elements as features


4. YS_Oliynyk.ipynb : Python program file to compare performance in predicting YS value for different ml models GBR, RF, SVR, KNN using Oliynyk feature

5. YS_SelectedFeatures.ipynb : Python program file to compare performance in predicting YS value for different ml models GBR, RF, SVR, KNN using domain knowledge based features

6. YS_composition.ipynb : Python program file to compare performance in predicting YS value for different ml models GBR, RF, SVR, KNN using domain knowledge based features

Candidate search for optimal alloy composition 

1. main_candidate_search_UTS_quaternary.ipynb : Python program file suggest the best quaternary alloy candidates for optimizing UTS  

2. main_candidate_search_YS_quaternary.ipynb : Python program file suggest the best quaternary alloy candidates for optimizing YS 

3. main_candidate_search_addition_quaternay.ipynb : Python program file suggest the best quaternay alloy candidates for optimizing composite target (addition)

4. main_candidate_search_Sqrt_quaternary.ipynb : Python program file suggest the best quaternay alloy candidates for optimizing composite target (Sqrt)

5. EI_Calculation_chunkwise.ipynb : Python program file to calculate the EI values for large candidate size (quinary alloy having more than 74 million candidates)


Others 

1. Virtual_candidates_alloy_derivation.ipynb : Python program file for creating the virtual alloy candidates depending on different combinations such as quaternay/quinary/senary

2. Nb_strength_data_splitting_F.ipynb : Python program file for splitting the original data into different train/test datasets based on alloy uniqueness so that the alloy present in the training data should not repeat in the test dataset

3. performance_diff_traintest_split.ipynb : Python program file to compare the performance for different train/test split of the original alloy dataset

4. UMAP_All.ipynb : Pyhton program file to represent the alloy compositions (Experimental as well as Suggested) in the two dimensional UMAP representations 

5. MOO_relationship.ipynb : Python program file to represent the relationship between YS, UTS and the composite properties for Multi Objective optimization 

6. MLP_UTS.ipynb : Python program file for performance evaluation of Multi Layer Perceptron for UTS prediction 

7. MLP_YS.ipynb : Python program file for performance evaluation of Multi Layer Perceptron for YS prediction 

8. Dstance_suggested_alloy.ipynb : Eucledian Distance of all suggested alloy candidates from Nb87.7W11.2Zr1.1 (highest performing existing alloy)

9. Nb_Dataset.ipynb : Visualization of Nb alloy existing strength data

