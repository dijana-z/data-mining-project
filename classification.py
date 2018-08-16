import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


def data_preprocessor(answers):
    ans = list(answers.values())
    wanted_ans = ['StackOverflowVisit', 'StackOverflowRecommend', 'Student', 'Employment', 'OperatingSystem',
                  'OpenSource', 'StackOverflowHasAccount', 'StackOverflowConsiderMember']
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

    y = df['StackOverflowConsiderMember']
    x = df[df.columns.drop(['StackOverflowConsiderMember']).tolist()]

    x = np.array(x).reshape(-1, 7)
    y = np.array(y).reshape(-1, 1)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    return X_train, X_test, y_train, y_test


def neural_network_classifier(answers):
    """
    Predicts if the user considers himself a member of Stack Overflow
    """
    X_train, X_test, y_train, y_test = data_preprocessor(answers)
    clf = MLPClassifier(solver='lbfgs', alpha = 1e-5)
    clf.fit(X_train, y_train.ravel())
    res = clf.predict(X_test)

    print('Neural network classification results:\n')
    print(classification_report(res, y_test))
    print(confusion_matrix(y_test, res))


def support_vector_classifier(answers):
    """
    Predicts if the user considers himself a member of Stack Overflow
    """
    X_train, X_test, y_train, y_test = data_preprocessor(answers)
    clf = LinearSVC()
    clf.fit(X_train, y_train.ravel())
    res = clf.predict(X_test)

    print('Support vector classification results:\n')
    print(classification_report(res, y_test))
    print(confusion_matrix(y_test, res))
