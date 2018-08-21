from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
import pycountry


def hobby_pie_plot(answers):
    """
    'Do you code as a hobby?' answers pie plot
    """
    data_needed = [ans['Hobby'] for user, ans in answers.items()]
    hobby_count = {k: data_needed.count(k) for k in set(data_needed)}

    labels = list(hobby_count.keys())
    sizes = [hobby_count[l] for l in labels]
    explode = (0, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Do they code as a hobby?')
    plt.show()


def student_pie_plot(answers):
    """
    'Are you a student?' answers pie plot
    """
    data_needed = [ans['Student'] for user, ans in answers.items()]
    st_count = {k: data_needed.count(k) for k in set(data_needed)}

    labels = list(st_count.keys())
    sizes = [st_count[l] for l in labels]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Are they students?')
    plt.show()


def employment_pie_plot(answers):
    """
    'Are you employed?' answers pie plot
    """
    data_needed = [ans['Employment'] for user, ans in answers.items()]
    em_count = {k: data_needed.count(k) for k in set(data_needed)}

    labels = list(em_count.keys())
    sizes = [em_count[l] for l in labels]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Are they employed?')
    plt.show()


def country_map(file_path):
    """
    Displays users per country on a world map
    -- taken from https://www.kaggle.com/ranjeetjain3/stack-over-flow-results --
    """
    df = pd.read_csv(file_path, sep=',', low_memory=False, error_bad_lines=False, index_col=False, dtype='unicode')
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


# TODO: proveri sto ne radi govno
def devtype_statistics(answers):
    """
    Plots the developer type of people who participated in the survey
    """
    plt.rcdefaults()
    data_needed = [ans['DevType'] for user, ans in answers.items()]
    dt_count = {k: data_needed.count(k) for k in set(data_needed)}
    devtypes = list(dt_count.keys())
    y_pos = np.arange(len(devtypes))
    dt = sorted([dt_count[l] for l in devtypes], reverse=True)
    devtypes = [l for _,l in sorted(zip(dt, devtypes), reverse=True)]

    plt.bar(y_pos, dt, align='center', alpha=0.5)
    plt.xticks(y_pos, devtypes, rotation='vertical', fontsize=5.5)
    plt.title('Developer type of people who participated in the survey')
    plt.show()


def career_satisfaction_pie(answers):
    """
    'How satisfied are you with your career?' answers pie chart
    """
    data_needed = [ans['CareerSatisfaction'] for user, ans in answers.items()]
    cs_count = {k: data_needed.count(k) for k in set(data_needed)}

    labels = list(cs_count.keys())
    sizes = [cs_count[l] for l in labels]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Career satisfaction')
    plt.show()


def yearscoding_pie_plot(answers):
    """
    'How many years do you code?' answers pie plot
    """
    data_needed = [ans['YearsCoding'] for user, ans in answers.items()]
    yc_count = {k: data_needed.count(k) for k in set(data_needed)}

    labels = list(yc_count.keys())
    sizes = [yc_count[l] for l in labels]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    plt.legend(labels=labels)
    my_circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.title('How many years do you code?')
    plt.show()


def yearscodingprof_pie_plot(answers):
    """
    'How many years do you code professionally?' answers pie plot
    """
    data_needed = [ans['YearsCodingProf'] for user, ans in answers.items()]
    yc_count = {k: data_needed.count(k) for k in set(data_needed)}

    labels = list(yc_count.keys())
    sizes = [yc_count[l] for l in labels]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    plt.legend(labels=labels)
    my_circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.title('How many years do you code professionally?')
    plt.show()


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
    usage = sorted([lang_count[l] for l in langs], reverse=True)
    langs = [l for _,l in sorted(zip(usage,langs), reverse=True)]


    plt.bar(y_pos, usage, align='center', alpha=0.5)
    plt.xticks(y_pos, langs, rotation='vertical', fontsize=5.5)
    plt.ylabel('Usage')
    plt.title('Programming language usage')
    plt.show()

    l_desire = [item for sublist in list(ans['LanguageDesireNextYear'].split(';') for user, ans in answers.items()) for
                item in sublist]
    l_desire_count = {k: l_desire.count(k) for k in set(l_desire)}

    subtracted_usage = sorted([l_desire_count[l] - lang_count[l] for l in langs])
    plt.bar(y_pos, subtracted_usage, align='center', alpha=0.5)
    plt.xticks(y_pos, langs, rotation='vertical', fontsize=5.5)
    plt.ylabel('Usage')
    plt.title('Programming language future popularity')
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


def opensource_pie_plot(answers):
    """
    'Do you contribute to open source projects?' answers pie plot
    """
    data_needed = [ans['OpenSource'] for user, ans in answers.items()]
    os_count = {k: data_needed.count(k) for k in set(data_needed)}

    labels = list(os_count.keys())
    sizes = [os_count[l] for l in labels]
    explode = (0, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    my_circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.title('Do they contribute to Open Source?')
    plt.show()


def opensource_and_hobby(file_path):
    """
    'Do you contribute to Open Source?' answers based on if they code as a hobby
    """
    df = pd.read_csv(file_path, sep=',', low_memory=False, error_bad_lines=False, index_col=False, dtype='unicode')
    data = df[['Hobby','OpenSource']].dropna()

    trace1 = go.Bar(
        x=['Yes', 'No'],
        y=[data[(data['OpenSource'] == 'Yes') & (data['Hobby'] == 'Yes')].count()[0], data[(data['OpenSource'] == 'Yes') & (data['Hobby'] == 'No')].count()[0]],
        name='Yes',
        opacity=0.6
    )

    data = [trace1]
    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig)


def opensource_and_operatingsystem(answers):
    plt.rcdefaults()
    """
    'Do you contribute to Open Source'? answers based on the Operating System they use
    """
    os = [(ans['OpenSource'],ans['OperatingSystem']) for user, ans in answers.items()]

    os_yes = list(filter(lambda x: x[0] == 'Yes', os))
    os_yes = [x[1] for x in os_yes]
    os_count = {k: os_yes.count(k) for k in set(os_yes)}
    os_yes = list(os_count.keys())
    y_pos = np.arange(len(os_yes))
    usage = sorted([os_count[l] for l in os_yes], reverse=True)
    os_yes = [l for _,l in sorted(zip(usage,os_yes), reverse=True)]

    plt.bar(y_pos, usage, align='center', alpha=0.5)
    plt.xticks(y_pos, os_yes, rotation='vertical', fontsize=5.5)
    plt.ylabel('Usage')
    plt.title('Operating System/Contributes to Open Source')
    plt.show()

    plt.rcdefaults()

    os_no = list(filter(lambda x: x[0] == 'No', os))
    os_no = [x[1] for x in os_no]
    os_count = {k: os_no.count(k) for k in set(os_no)}
    os_no = list(os_count.keys())
    y_pos = np.arange(len(os_no))
    usage = sorted([os_count[l] for l in os_no], reverse=True)
    os_no = [l for _,l in sorted(zip(usage,os_no), reverse=True)]

    plt.bar(y_pos, usage, align='center', alpha=0.5)
    plt.xticks(y_pos, os_no, rotation='vertical', fontsize=5.5)
    plt.ylabel('Usage')
    plt.title("Operating System/Doesn't contribute to Open Source")
    plt.show()
