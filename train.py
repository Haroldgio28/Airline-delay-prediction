
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
import pickle


# Parameters
random_state = 42
n_components_opt = 20
best_estimator = 50
max_depth_opt = 15
best_min_samples_split = 20
best_min_samples_leaf = 10


#Load Data
df = pd.read_csv("data/Airlines.csv")


#Data Preparation

df.columns = df.columns.str.lower().str.replace(' ', '_')

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

# Delete columns useless for classification
del df['id']
del df['flight']

# Convert data type of day_of_week
df['dayofweek'] = df['dayofweek'].astype('object')

# Creation of new features
# df['airport_mix'] = df['airportfrom'] + ' - ' + df['airportto']

target = 'delay'
cat = ['airline', 'airportfrom', 'airportto', 'dayofweek'
    #    ,'airport_mix'
        ]
num = ['time', 'length']


# Splitting data into train and test

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=random_state)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=random_state)

df_full_train = df_full_train.reset_index(drop=True)
y_full_train = df_full_train[target].values
del df_full_train[target]

df_train = df_train.reset_index(drop=True)
y_train = df_train[target].values
del df_train[target]

df_val = df_val.reset_index(drop=True)
y_val = df_val[target].values
del df_val[target]

df_test = df_test.reset_index(drop=True)
y_test = df_test[target].values
del df_test[target]


def vectorize(df_train):
    dicts_train = df_train.to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts_train)

    return dv,X_train


dv,X_train = vectorize(df_train)


def vectorize_df(df, dv):
    '''transform dataframe to matrix and return de X dataframe with respective name as name variable'''
    dicts = df.to_dict(orient='records')
    df_name = dv.transform(dicts)
    return df_name


# X_val = vectorize_df(df_val, dv)
# X_test = vectorize_df(df_test, dv)


def dimention_reduction(X_train, n_components):
    '''reduce dimention of data using PCA and return the new X_train, X_val, X_test'''
    pca = PCA(n_components=n_components, random_state=random_state)
    X_train_pca = pca.fit_transform(X_train)

    return X_train_pca,pca


X_train_pca,pca = dimention_reduction(X_train, n_components_opt)


X_train_pca.shape


X_train.shape


def train(X_train_pca, y_train, n_estimators, max_depth, min_samples_split, min_samples_leaf):
    '''train the model and return the model'''
    rf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf, random_state=random_state, n_jobs=-1)
    rf.fit(X_train_pca, y_train)
    return rf


def predict(model, df, dv, pca):
    '''predict the model and return the prediction'''
    X = vectorize_df(df, dv)
    X_pca = pca.transform(X)
    y_pred = model.predict_proba(X_pca)[:, 1]
    return y_pred


# print('-------------------------------------')
# print('Train')
# rf = train(X_train_pca, y_train, best_estimator, max_depth_opt, best_min_samples_split, best_min_samples_leaf)
# # print('Training completed')
# # print('-------------------------------------')


# # print('-------------------------------------')
# # print('Evaluation on validation')
# y_pred_val = predict(rf, df_val, dv , pca)
# auc_val = roc_auc_score(y_val, y_pred_val)
# # print('AUC on validation: {:.3f}'.format(auc_val))


# # print('-------------------------------------')
# # print('Evaluation on test')
# y_pred_test = predict(rf, df_test, dv , pca)
# auc_test = roc_auc_score(y_test, y_pred_test)
# print('AUC on test: {:.3f}'.format(auc_test))


print('-------------------------------------')
print('Train with full train data')

dv,X_full_train = vectorize(df_full_train)
X_full_train_pca,pca = dimention_reduction(X_full_train, n_components_opt)
rf = train(X_full_train_pca, y_full_train, best_estimator, max_depth_opt, best_min_samples_split, best_min_samples_leaf)

print('Training completed')
print('-------------------------------------')


print('-------------------------------------')
print('Evaluation on test')
y_pred_test = predict(rf, df_test, dv , pca)

auc_test = roc_auc_score(y_test, y_pred_test)
print('AUC on test: {:.3f}'.format(auc_test))


# Save model 
output_file = 'final_model.bin'

with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, pca, rf), f_out)
print('\n')
print(f'The model is saved to {output_file}')

