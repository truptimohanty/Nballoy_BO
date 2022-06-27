import numpy as np
from scipy.stats import norm

# DETERMINING the mean and standard Deviation using bootstrp sampling with 1000 bootstrap samples

def bootstrap_estimator(model, X_train, y_train, X_test, n_iter=1000):
    
    '''
    Function to estimate the mean and standard deviation
    
    paramenters:
    model = best model hyperparameters
    X_train = training features
    y_tain = training target
    X_test = test features
    n_iter = no of bootstrap sample
    seed = 20 is fixed to have repeatability in boot straping
    
    return:
    returns mean and and standard deviation 
    '''

    
    bootstrap_preds = np.zeros([len(X_test), n_iter])
    
    index = np.arange(X_train.shape[0])
    
    ## set the seed to repeat the boot strapping 
    np.random.seed(20)
    for i in range(n_iter):
        #sample from X_train, y_train
        index_sampled = np.random.choice(index, size=X_train.shape[0], replace=True)

        X_train_sample = X_train[index_sampled,:]
        y_train_sample = y_train[index_sampled]
        
        #model.fit(X_train_sample, y_train_sample)
        model.fit(X_train_sample, y_train_sample)
        
        #pred_i = model.predict(X_test)
        
        pred_i = model.predict(X_test)
        #print('pred_i:', pred_i)
        
        bootstrap_preds[:,i] = pred_i
        #print(bootstrap_preds)
        
    return(bootstrap_preds.mean(1),bootstrap_preds.std(1))

        


## Expection Improvement Calculation 


def Expected_Improvement(X_test, X_train_all, y_train_all, model, xi=0.01):
    
    '''
     Calcualting the Expected Improvement
     More information : http://krasserm.github.io/2018/03/21/bayesian-optimization/
     parameters: mean, std, y_train, xi
     return :
     Expected improvement value
     
    '''
     
    mu_x, sigma_x = bootstrap_estimator(model, X_train_all, y_train_all, X_test, n_iter=1000) 
    mu_max = np.max(y_train_all) 
    # mu_max is the highest material property value in the training data which is at 24 deg C 
    # therefore the candidate search space is choosen at 24 deg C
    
    diff = (mu_x-mu_max-xi)
    z = diff/sigma_x
    ei = diff*norm.cdf(z)+sigma_x*norm.pdf(z)
    ei[sigma_x == 0.0] = 0.
    return(ei,mu_x,sigma_x)
    
