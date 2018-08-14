import matplotlib.pyplot as plt
import numpy as np


def languages_statistic(answers):
    plt.rcdefaults()

    languages = [item for sublist in list(ans['LanguageWorkedWith'].split(';') for user, ans in answers.items()) for
                 item in sublist]
    lang_count = {k: languages.count(k) for k in set(languages)}
    print(lang_count)
    print(len(lang_count.keys()))

    l_desire = [item for sublist in list(ans['LanguageDesireNextYear'].split(';') for user, ans in answers.items()) for
                item in sublist]
    l_desire_count = {k: l_desire.count(k) for k in set(l_desire)}
    print(l_desire_count)
    print(len(l_desire_count.keys()))

    # langs = list(lang_count.keys())
    # y_pos = np.arange(len(langs))
    # usage = [lang_count[l] for l in langs]
    #
    # print(langs), print(usage)
    # plt.bar(y_pos, usage, align='center', alpha=0.5)
    # plt.xticks(y_pos, langs)
    # plt.ylabel('Usage')
    # plt.title('Programming language usage')
    #
    # plt.show()

    # TODO: napraviti dva dijagrama od kojih prvi pokazuje koji je jezik koliko zastupljen a drugi koliko je opala-porasla popularnost nekog jezika u zavisnosti od toga da li hoce da rade sa njim

def salary_statistic(answers):
    plt.rcdefaults()

    salary_stat = [(ans['ConvertedSalary'], ans['YearsCodingProf']) for user, ans in answers.items()]
    print(salary_stat)

    # TODO: napraviti dijagram koji pokazuje odnos plate i godina rada


# TODO: generalno treba ovde jos neki density plot da se odradi