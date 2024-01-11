# from src.logger import logging
# import os
# import sys
# from sklearn.model_selection import RandomizedSearchCV
# from sklearn.model_selection import GridSearchCV
# import pandas as pd
# from pandas import DataFrame
# import numpy as np
# from src.utils import save_object, evaluate_models
# from sklearn.model_selection import GridSearchCV
# from pandas import DataFrame

# def tune_model(X_train, y_train, param, models):
#     results_list = []
    
#     for model_name, model in models.items():
#         param_grid = param[model_name]
#         gs = GridSearchCV(model, param_grid, cv=3)
#         gs_results = gs.fit(X_train, y_train)
#         best_model = gs_results.best_estimator_
        
#         results = DataFrame(gs_results.cv_results_)
#         results.loc[:, 'mean_test_score'] *= 100
#         results = results.loc[:, ('rank_test_score', 'mean_test_score', 'params')]
#         results.sort_values(by='rank_test_score', ascending=True, inplace=True)
        
#         results_list.append({
#             'model_name': model_name,
#             'best_model': best_model,
#             'results': results
#         })
    
#     return results_list


