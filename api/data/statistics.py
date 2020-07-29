import os

import pandas as pd

from copro.settings import BASE_DIR

# TODO: put in env var and import it
data_path = os.path.join(BASE_DIR, 'api/data/annonces.csv')


def get_data_from_csv(path):
    """
    Create dataframe from csv filepath. Keep only needed columns

    `path` is the csv file location.
    """

    # import data as dataframe
    raw_data = pd.read_csv(path)

    # keep only useful columns
    feature_cols = ['CONDOMINIUM_EXPENSES', 'DEPT_CODE', 'ZIP_CODE', 'CITY']
    data = raw_data.dropna(subset=feature_cols)

    return data


def get_condo_expenses_by(col, value):
    """
    Return mean, 1st and 9th decile condominium expenses values for the given query type.

    `Col` can either be: `DEPT_CODE`, `CITY` or `ZIP_CODE`.

    `Value` is the actual query parameter.
    """

    assert col in ('DEPT_CODE', 'CITY',
                   'ZIP_CODE'), "col must be 'dept', 'city' or 'zip'"

    data = get_data_from_csv(data_path)

    # group data by column and compute statistics
    group = data.groupby(col, as_index=False)['CONDOMINIUM_EXPENSES']
    mean = group.mean()
    first_quantile = group.quantile(0.1)
    ninth_quantile = group.quantile(0.9)

    # build filtering condition
    if col == 'DEPT_CODE':
        condition = mean['DEPT_CODE'] == value
    elif col == 'CITY':
        condition = mean['CITY'] == value
    else:
        condition = mean['ZIP_CODE'] == value

    # TODO: refactor
    mean = mean['CONDOMINIUM_EXPENSES'][condition].iloc[0]
    first_quantile = first_quantile['CONDOMINIUM_EXPENSES'][condition].iloc[0]
    ninth_quantile = ninth_quantile['CONDOMINIUM_EXPENSES'][condition].iloc[0]

    return {
        "mean": mean,
        "1st_quantile": first_quantile,
        "9th_quantile": ninth_quantile,
    }
