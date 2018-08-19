from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
import pycountry


def language_statistics(answers):
    """
    Plots the usage by language and the language future popularity
    """
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


def ai_sentiments(answers):
    """
    Plots the feelings about the future of AI by age
    """
    plt.rcdefaults()

    ai_answers = [(ans['AIFuture'], ans['Age']) for user, ans in answers.items()]

    year_sentiment = {}
    for ai in ai_answers:
        if ai[1] not in year_sentiment:
            year_sentiment[ai[1]] = [ai[0]]
        else:
            year_sentiment[ai[1]].append(ai[0])

    ai_positive = {}
    ai_negative = {}
    ai_neutral = {}
    age_groups = {}

    for age, ans in year_sentiment.items():
        sentiments = {k: ans.count(k) for k in set(ans)}

        ai_negative[age] = sentiments["I'm worried about the dangers more than I'm excited about the possibilities."]
        ai_positive[age] = sentiments["I'm excited about the possibilities more than worried about the dangers."]
        ai_neutral[age] = sentiments["I don't care about it, or I haven't thought about it."]

        age_groups[age] = ai_positive[age] + ai_negative[age] + ai_neutral[age]

    ai_positive = {k: ai_positive[k]*100/age_groups[k] for k in age_groups.keys()}
    ai_negative = {k: ai_negative[k]*100/age_groups[k] for k in age_groups.keys()}
    ai_neutral = {k: ai_neutral[k]*100/age_groups[k] for k in age_groups.keys()}

    print(ai_negative)
    print(ai_positive)
    print(ai_neutral)

    X = np.arange(len(ai_positive))
    ax = plt.subplot(111)
    ax.bar(X - 0.3, ai_negative.values(), width=0.2, color='r', align='center')
    ax.bar(X, ai_neutral.values(), width=0.2, color='b', align='center')
    ax.bar(X + 0.3, ai_positive.values(), width=0.2, color='g', align='center')

    ax.legend(('Negative', 'Neutral', 'Positive'))
    plt.xticks(X, ai_neutral.keys(), fontsize=5)
    plt.title("AI Sentiments", fontsize=17)
    plt.show()


def country_map(file_path):
    """
    Displays users per country on a world map
    -- taken from https://www.kaggle.com/ranjeetjain3/stack-over-flow-results --
    """
    df = pd.read_csv(path, sep=',', low_memory=False, error_bad_lines=False, index_col=False, dtype='unicode')
    countries = df['Country'].value_counts()

    countries = countries.to_frame().reset_index()
    countries.loc[2]['code'] = 'test'

    for i,country in enumerate(countries['index']):
        user_input = country
        mapping = {country.name: country.alpha_3 for country in pycountry.countries}
        countries.set_value(i, 'code', mapping.get(user_input))
    data = [ dict(
            type = 'choropleth',
            locations = countries['code'],
            z = countries['Country'],
            text = countries['index'],
            colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
                [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
            autocolorscale = False,
            reversescale = True,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar = dict(
                autotick = False,
                tickprefix = '',
                title = 'Total Count'),
          ) ]

    layout = dict(
        title = 'countries which responded to the survey',
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )

    fig = dict( data=data, layout=layout )
    py.plot( fig, validate=False)
