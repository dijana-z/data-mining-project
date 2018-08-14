import pandas as pd


def read_public_csv(file_path):
    df = pd.read_csv(file_path,
                     usecols=['Respondent', 'Hobby', 'OpenSource', 'Country', 'Student', 'Employment',
                              'FormalEducation', 'DevType', 'YearsCoding', 'YearsCodingProf', 'JobSatisfaction',
                              'CareerSatisfaction', 'ConvertedSalary', 'AgreeDisagree1', 'AgreeDisagree2',
                              'AgreeDisagree3', 'LanguageWorkedWith', 'LanguageDesireNextYear', 'IDE',
                              'OperatingSystem', 'AIDangerous', 'AIInteresting', 'AIResponsible', 'AIFuture',
                              'StackOverflowRecommend', 'StackOverflowVisit', 'Age', 'StackOverflowHasAccount',
                              'StackOverflowConsiderMember', 'HoursComputer', 'Gender'],
                     sep=',', low_memory=False, error_bad_lines=False, index_col=False, dtype='unicode')
    df = df.dropna()

    print('\n~ Public DataFrame:\n')
    print(f'{df.head()}\n\n')
    print(f'{df.count()}\n\n')
    print(f'{df.describe()}\n\n')

    dict_list = []
    for index, row in df.iterrows():
        dict_list.append(dict(row))

    answer_map = {}
    for dic in dict_list:
        resp = int(dic['Respondent'])
        the_rest = ['Hobby', 'OpenSource', 'Country', 'Student', 'Employment',
                    'FormalEducation', 'DevType', 'YearsCoding', 'YearsCodingProf', 'JobSatisfaction',
                    'CareerSatisfaction', 'ConvertedSalary', 'AgreeDisagree1', 'AgreeDisagree2',
                    'AgreeDisagree3', 'LanguageWorkedWith', 'LanguageDesireNextYear', 'IDE',
                    'OperatingSystem', 'AIDangerous', 'AIInteresting', 'AIResponsible', 'AIFuture',
                    'StackOverflowRecommend', 'StackOverflowVisit', 'Age', 'StackOverflowHasAccount',
                    'StackOverflowConsiderMember', 'HoursComputer', 'Gender']
        answers = {key: dic[key] for key in the_rest}
        answer_map[resp] = answers

    return answer_map


def read_schema_csv(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()

    print('~ Schema DataFrame:\n')
    print(f'{df.head()}\n\n')
    print(f'{df.count()}\n\n')
    print(f'{df.describe()}\n\n')

    schema_dict = df.to_dict(orient='list')
    question_info = dict(zip(schema_dict['Column'], schema_dict['QuestionText']))
    wanted_keys = ['Respondent', 'Hobby', 'OpenSource', 'Country', 'Student', 'Employment',
                   'FormalEducation', 'DevType', 'YearsCoding', 'YearsCodingProf', 'JobSatisfaction',
                   'CareerSatisfaction', 'ConvertedSalary', 'AgreeDisagree1', 'AgreeDisagree2',
                   'AgreeDisagree3', 'LanguageWorkedWith', 'LanguageDesireNextYear', 'IDE',
                   'OperatingSystem', 'AIDangerous', 'AIInteresting', 'AIResponsible', 'AIFuture',
                   'StackOverflowRecommend', 'StackOverflowVisit', 'Age', 'StackOverflowHasAccount',
                   'StackOverflowConsiderMember', 'HoursComputer', 'Gender']
    questions = {key: question_info[key] for key in wanted_keys}
    return questions

