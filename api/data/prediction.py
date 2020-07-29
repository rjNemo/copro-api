import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# TODO: use one hot encoding to handle unknown values in transform step
from sklearn.preprocessing import LabelEncoder

from .statistics import data_path


class LinearRegressor:

    def __init__(self):
        self.X, self.y = self.preprocessing()

    def preprocessing(self):
        """Prepare data for modelling."""

        # read csv
        raw_data = pd.read_csv(
            data_path, dtype={'DEPT_CODE': str, 'ZIP_CODE': str, 'INSEE_CODE': str})

        # drop missing values from significative columns
        feature_cols = ['CONDOMINIUM_EXPENSES',
                        'DEPT_CODE', 'ZIP_CODE', 'CITY', 'SURFACE']
        data = raw_data.dropna(subset=feature_cols)

        # columns used in modelling
        cols = ['ZIP_CODE', 'DEPT_CODE', 'CITY', 'INSEE_CODE', 'LATITUDE',
                'LONGITUDE', 'SURFACE', 'HEATING_MODE', 'ELEVATOR']

        # target
        y = data['CONDOMINIUM_EXPENSES']
        # features
        X = data[cols]

        # surface rows are not correctly typed I do it manually
        X['SURFACE'] = X['SURFACE'].astype(float)

        # split dataset for training
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, train_size=0.7, random_state=0)

        # fill missing values with most frequent values. TODO: suboptimal method
        train_mode = dict(X_train.mode().iloc[0])
        X_train = X_train.fillna(train_mode)

        cols = X_train.dtypes == 'object'
        cat_cols = list(cols[cols].index)
        cols = X_train.dtypes != 'object'
        num_cols = list(cols[cols].index)

        # handle missing values on categorical columns
        imputer = SimpleImputer(strategy='constant')
        X_train[cat_cols] = imputer.fit_transform(X_train[cat_cols])
        X_val[cat_cols] = imputer.transform(X_val[cat_cols])

        # encode categorical data
        encoder = LabelEncoder()

        for col in cat_cols:
            X_train[col] = encoder.fit_transform(X_train[col])

        # handle numerical missing values
        num_imputer = SimpleImputer(strategy='mean')

        X_train[num_cols] = num_imputer.fit_transform(X_train[num_cols])
        X_val[num_cols] = num_imputer.transform(X_val[num_cols])

        return X_train, y_train

    def get_trained_model(self):
        lin_reg = LinearRegression().fit(self.X, self.y)

        return lin_reg

    def predict_expenses(self, data):
        """Return condominium expenses as a function of data."""

        model = self.get_trained_model()

        return model.predict(data)
