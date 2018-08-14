from reading_csv import read_schema_csv, read_public_csv
from visualization import languages_statistic, salary_statistic


def main():
    file_schema = '../survey_results_schema.csv'
    file_public = '../survey_results_public.csv'

    questions = read_schema_csv(file_schema)
    answers = read_public_csv(file_public)

    languages_statistic(answers)


if __name__ == '__main__':
    main()