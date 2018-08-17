import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def data_preprocessor(answers):
    ans = list(answers.values())
    wanted_ans = ['OpenSource', 'OperatingSystem', 'VersionControl', 'Hobby', 'Student', 'Employment',
                  'StackOverflowHasAccount', 'StackOverflowConsiderMember', 'StackOverflowParticipate',
                  'StackOverflowDevStory']
    ans_final = {key: [] for key in wanted_ans}

    for wanted in wanted_ans:
        for item in ans:
            ans_final[wanted].append(item[wanted])

    pd.set_option('display.expand_frame_repr', False)
    df = pd.DataFrame.from_dict(ans_final)
    print('Classification dataframe')
    print(df.head())
    print(df.describe())

    lb_make = LabelEncoder()
    for column in df:
        df[column] = lb_make.fit_transform(df[column])

    y = df['OpenSource']
    x = df[df.columns.drop(['OpenSource']).tolist()]

    x = np.array(x).reshape(-1, 9)
    y = np.array(y).reshape(-1, 1)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    return X_train, X_test, y_train, y_test


def random_forest_classifier(answers):
    """
    Classifies users into categories based on whether they contribute to Open Source or not
    """
    X_train, X_test, y_train, y_test = data_preprocessor(answers)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train.ravel())
    res = clf.predict(X_test)

    print('Random forest classification results:\n')
    print(classification_report(res, y_test))
    print(confusion_matrix(y_test, res))


def neural_network_classifier(answers):
    """
    Classifies users into categories based on whether they contribute to Open Source or not
    """
    X_train, X_test, y_train, y_test = data_preprocessor(answers)
    clf = MLPClassifier(solver='lbfgs')
    clf.fit(X_train, y_train.ravel())
    res = clf.predict(X_test)

    print('Neural network classification results:\n')
    print(classification_report(res, y_test))
    print(confusion_matrix(y_test, res))
