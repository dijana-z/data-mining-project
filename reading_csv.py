import pandas as pd


fields_needed = ['Respondent', 'Hobby', 'OpenSource', 'Country', 'Student', 'Employment', 'DevType',
                 'YearsCoding', 'YearsCodingProf', 'CareerSatisfaction', 'ConvertedSalary', 'Age', 'AIFuture',
                 'LanguageWorkedWith', 'LanguageDesireNextYear', 'IDE', 'VersionControl', 'OperatingSystem',
                 'StackOverflowDevStory', 'StackOverflowRecommend', 'StackOverflowVisit', 'StackOverflowHasAccount',
                 'StackOverflowConsiderMember', 'StackOverflowParticipate']


def read_public_csv(file_path):
    """
    :return: returns a dictionary of users and their answers to the survey questions
    """
    df = pd.read_csv(file_path,
                     usecols=fields_needed,
                     sep=',', low_memory=False, error_bad_lines=False, index_col=False, dtype='unicode')

    # data analysis
    print('\n~ Public DataFrame:\n')
    print('{}\n\n'.format(df.head()))
    print('{}\n\n'.format(df.count()))
    print('{}\n\n'.format(df.describe()))

    # eliminating NA values
    df = df.dropna()

    # making a dictionary
    dict_list = []
    for index, row in df.iterrows():
        dict_list.append(dict(row))

    answer_dict = {}
    for dic in dict_list:
        resp = int(dic['Respondent'])
        the_rest = fields_needed[1:]
        answers = {key: dic[key] for key in the_rest}
        answer_dict[resp] = answers

    return answer_dict


def read_schema_csv(file_path):
    """
    :return: returns a dictionary of questions in the survey
    """
    df = pd.read_csv(file_path, dtype='unicode')

    # data analysis
    print('~ Schema DataFrame:\n')
    print('{}\n\n'.format(df.head()))
    print('{}\n\n'.format(df.count()))
    print('{}\n\n'.format(df.describe()))

    # eliminating NA values
    df = df.dropna()

    # making a dictionary
    schema_dict = df.to_dict(orient='list')
    question_info = dict(zip(schema_dict['Column'], schema_dict['QuestionText']))
    wanted_keys = fields_needed
    questions = {key: question_info[key] for key in wanted_keys}

    return questions
