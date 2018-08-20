import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR

def salary_regression(answers):
    data_needed = [(ans['Country'], ans['Age'], float(ans['ConvertedSalary'])) for user, ans in answers.items()]
    data_needed = list(filter(lambda x: x[0] == 'United States', data_needed))
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

    lm = LinearRegression()
    reg = MLPRegressor(max_iter=10000)

    age_numeric = np.array(age_numeric).reshape(-1, 1)
    salary = np.array(salary)

    pred = reg.fit(age_numeric, salary)

    x = np.linspace(14, 70, 1000).reshape(-1, 1)
    y = reg.predict(x)

    plt.plot(x, y, color='red')
    plt.scatter(age_numeric, salary)
    plt.show()

    pred1 = lm.fit(age_numeric, salary)
    y = lm.predict(x)

    plt.plot(x, y, color='red')
    plt.scatter(age_numeric, salary)
    plt.show()
