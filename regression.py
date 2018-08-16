import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, mean_squared_error


def data_preprocessor(answers):
    """
    :return: transforms data into a convenient data type used for regression
    """
    ans = list(answers.values())
    wanted_ans = ['ConvertedSalary', 'FormalEducation', 'YearsCodingProf', 'Country', 'Student', 'Employment', 'Age',
                  'YearsCoding']
    ans_final = {key: [] for key in wanted_ans}

    for wanted in wanted_ans:
        for item in ans:
            if not wanted == 'ConvertedSalary':
                ans_final[wanted].append(item[wanted])
            else:
                ans_final[wanted].append(float(item[wanted]))

    pd.set_option('display.expand_frame_repr', False)
    df = pd.DataFrame.from_dict(ans_final)
    print('Regression dataframe')
    print(df.head())
    print(df.describe())

    # mozda ovako nesto?
    # education_coding = {'I never completed any formal education': 1,
    #                     'Primary/elementary school': 2,
    #                     'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 3,
    #                     'Some college/university study without earning a degree': 4,
    #                     'Associate degree': 4,
    #                     'Bachelor’s degree (BA, BS, B.Eng., etc.)': 6,
    #                     'Master’s degree (MA, MS, M.Eng., MBA, etc.)': 7,
    #                     'Professional degree (JD, MD, etc.)': 8,
    #                     'Other doctoral degree (Ph.D, Ed.D., etc.)': 9
    #                     }

    lb_make = LabelEncoder()
    for column in df:
        if column != 'ConvertedSalary':
            df[column] = lb_make.fit_transform(df[column])

    y = df['ConvertedSalary']
    x = df[df.columns.drop(['ConvertedSalary']).tolist()]

    x = np.array(x).reshape(-1, 7)
    y = np.array(y).reshape(-1, 1)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    return X_train, X_test, y_train, y_test


# lol
def linear_regression(answers):
    X_train, X_test, y_train, y_test = data_preprocessor(answers)

    lr = LinearRegression()
    lr.fit(X_train, y_train.ravel())

    r2_test = r2_score(y_test, lr.predict(X_test))
    r2_train = r2_score(y_train, lr.predict(X_train))

    # r2_test = lr.score(X_test, y_test)
    # r2_train = lr.score(X_train, y_train)
    print('\nR^2 test = {}'.format(r2_test))
    print('R^2 train = {}'.format(r2_train))

    mse_test = mean_squared_error(y_test, lr.predict(X_test))
    mse_train = mean_squared_error(y_train, lr.predict(X_train))
    print('\nMSE test = {}'.format(mse_test))
    print('MSE train = {}'.format(mse_train))

    rmse_test = np.sqrt(mse_test)
    rmse_train = np.sqrt(mse_train)
    print('\nRMSE test = {}'.format(rmse_test))
    print('RMSE train = {}'.format(rmse_train))


# jos veci lol
def logistic_regression(answers):
    X_train, X_test, y_train, y_test = data_preprocessor(answers)

    lr = LogisticRegression()
    lr.fit(X_train, y_train.ravel())

    r2_test = r2_score(y_test, lr.predict(X_test))
    r2_train = r2_score(y_train, lr.predict(X_train))

    # r2_test = lr.score(X_test, y_test)
    # r2_train = lr.score(X_train, y_train)
    print('\nR^2 test = {}'.format(r2_test))
    print('R^2 train = {}'.format(r2_train))

    mse_test = mean_squared_error(y_test, lr.predict(X_test))
    mse_train = mean_squared_error(y_train, lr.predict(X_train))
    print('\nMSE test = {}'.format(mse_test))
    print('MSE train = {}'.format(mse_train))

    rmse_test = np.sqrt(mse_test)
    rmse_train = np.sqrt(mse_train)
    print('\nRMSE test = {}'.format(rmse_test))
    print('RMSE train = {}'.format(rmse_train))

