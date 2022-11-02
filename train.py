import pandas as pd
import pickle
from sklearn.ensemble import HistGradientBoostingClassifier
# import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer

# Importing cleaning datas
df_train = pd.read_csv('../input/df_train.csv')
target = pd.read_csv('../input/target.csv')
df_test = pd.read_csv('../input/df_test.csv')

# The features with a score of 93%, just to lighten flask queries
f_importance = [ 
                'lead_time',  
                'stays_in_weekend_nights',
                'stays_in_week_nights',
                'adr',
                'total_of_special_requests',
                'agent_numeric', 
                'meal',
                'hotel',
                'country',
                'market_segment',
                'reserved_room_type',
                'assigned_room_type',
                'season', 
                ]

# dv is used here to retrieve feature names in dictionary form, 
# it is important for the future request in json format in flask.
# If you import the original data instead of cleaned data,
# you should fit and transform the categorical features
# and use label encoder instead of dv.
# If you would try ohe dataset, you should again fit and
# transform categorical features but this time with one hot
# encoder
def train(df_train, target):
    '''Capting the best model and fitting the model'''
    dicts = df_train[f_importance].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)

    X_train = dv.fit_transform(dicts)

    model = model_hist = HistGradientBoostingClassifier(
        learning_rate=0.24155975540325098,
        max_iter=353,
        max_leaf_nodes=119,
    )

    # You can use XGBOOST model tha gives a score of 93%
    # model_xgb = xgb.XGBClassifier(
    #             eta=0.4545367539753776,
    #             max_depth=15,
    #             min_child_weight=7,
    #         )
    # model_xgb.fit(X_train, target)

    model.fit(X_train, target)
    return dv, model

# fit the model
dv, model = train(df_train, target)

# version of model
v=1
output_file = f'hotel_v.{v}.bin'

# save the model in binary file
with open(output_file, 'wb') as f:
    pickle.dump((dv, model), f)
print('done!')

