import pandas as pd


fields_needed = ['Respondent', 'Hobby', 'OpenSource', 'Country', 'Student', 'Employment', 'FormalEducation', 'DevType',
                 'YearsCoding', 'YearsCodingProf', 'JobSatisfaction', 'CareerSatisfaction', 'ConvertedSalary',
                 'AgreeDisagree1', 'AgreeDisagree2', 'AgreeDisagree3', 'LanguageWorkedWith', 'LanguageDesireNextYear',
                 'IDE', 'OperatingSystem', 'AIDangerous', 'AIInteresting', 'AIResponsible', 'AIFuture',
                 'StackOverflowRecommend', 'StackOverflowVisit', 'Age', 'StackOverflowHasAccount',
                 'StackOverflowConsiderMember', 'HoursComputer', 'Gender', 'CheckInCode', 'StackOverflowParticipate']


def read_public_csv(file_path):
    """
    :return: returns a dictionary of users and their answers to the survey questions
    """
    df = pd.read_csv(file_path,
                     usecols=fields_needed,
                     sep=',', low_memory=False, error_bad_lines=False, index_col=False, dtype='unicode')

    # data analysis
    print('\n~ Public DataFrame:\n')
    print(f'{df.head()}\n\n')
    print(f'{df.count()}\n\n')
    print(f'{df.describe()}\n\n')

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
    df = pd.read_csv(file_path)

    # data analysis
    print('~ Schema DataFrame:\n')
    print(f'{df.head()}\n\n')
    print(f'{df.count()}\n\n')
    print(f'{df.describe()}\n\n')

    # eliminating NA values
    df = df.dropna()

    # making a dictionary
    schema_dict = df.to_dict(orient='list')
    question_info = dict(zip(schema_dict['Column'], schema_dict['QuestionText']))
    wanted_keys = fields_needed
    questions = {key: question_info[key] for key in wanted_keys}

    return questions

