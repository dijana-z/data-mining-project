import matplotlib.pyplot as plt
import numpy as np


def language_statistics(answers):
    plt.rcdefaults()

    languages = [item for sublist in list(ans['LanguageWorkedWith'].split(';') for user, ans in answers.items()) for
                 item in sublist]
    lang_count = {k: languages.count(k) for k in set(languages)}

    langs = list(lang_count.keys())
    y_pos = np.arange(len(langs))
    usage = [lang_count[l] for l in langs]

    plt.bar(y_pos, usage, align='center', alpha=0.5)
    plt.xticks(y_pos, langs, rotation='vertical')
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.show()

    l_desire = [item for sublist in list(ans['LanguageDesireNextYear'].split(';') for user, ans in answers.items()) for
                item in sublist]
    l_desire_count = {k: l_desire.count(k) for k in set(l_desire)}

    subtracted_usage = [l_desire_count[l] - lang_count[l] for l in langs]
    plt.bar(y_pos, subtracted_usage, align='center', alpha=0.5)
    plt.xticks(y_pos, langs, rotation='vertical')
    plt.ylabel('Usage')
    plt.title('Programming language popularity')

    plt.show()
