import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


def cluster_langdevtypes(answers):
    data_needed = []

    for user, ans in answers.items():
        langs = ans['LanguageWorkedWith'].split(';')
        devtype = ans['DevType'].split(';')

        data_needed.append((random.choice(langs), random.choice(devtype)))

    data_needed = data_needed[:1000]

    langs = [dn[0] for dn in data_needed]
    devs = [dn[1] for dn in data_needed]

    df = pd.DataFrame(np.column_stack([langs, devs]), columns=['language', 'devtype'])
    print(df.head())

    lb_make = LabelEncoder()
    min_max_scaler = MinMaxScaler()

    for column in df:
        df[column] = lb_make.fit_transform(df[column])

    x = df.values
    x_scaled = min_max_scaler.fit_transform(x)
    df = pd.DataFrame(x_scaled)

    mat = df.values
    km = KMeans(n_clusters=5)
    km.fit(mat)
    y_kmeans = km.predict(mat)

    plt.scatter(mat[:, 0], mat[:, 1], c=y_kmeans)
    centers = km.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.show()


def cluster_agesalary(answers):
    data_needed = [(ans['Country'], ans['Age'], float(ans['ConvertedSalary'])) for user, ans in answers.items()]
    data_needed = list(filter(lambda x: x[0] == 'United States' or x[0] == 'India', data_needed))
    data_needed = list(filter(lambda x: x[2] < 500000, data_needed))

    data_needed = data_needed[:1000]

    salary = [dn[2] for dn in data_needed]
    age = [dn[1] for dn in data_needed]

    age = list(map(lambda x: '18' if x[0] == 'U' else '65' if x[3] == 'y' else x[:7], age))

    age_numeric = []

    for a in age:
        if a == '18':
            age_numeric.append(random.uniform(14, 18))
        elif a == '65':
            age_numeric.append(random.uniform(65, 70))
        else:
            start = int(a[:2])-1
            finish = int(a[-2:])
            age_numeric.append(random.uniform(start, finish))

    df = pd.DataFrame(np.column_stack([age_numeric, salary]), columns=['age', 'salary'])
    print(df.head())

    lb_make = LabelEncoder()
    min_max_scaler = MinMaxScaler()

    for column in df:
        df[column] = lb_make.fit_transform(df[column])

    x = df.values
    x_scaled = min_max_scaler.fit_transform(x)
    df = pd.DataFrame(x_scaled)

    mat = df.values
    km = KMeans(n_clusters=2)
    km.fit(mat)
    y_kmeans = km.predict(mat)

    plt.scatter(mat[:, 0], mat[:, 1], c=y_kmeans)
    centers = km.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.show()
