import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


def frequent_items_languages(answers):
    languages = [item for item in list(ans['LanguageWorkedWith'].split(';') for user, ans in answers.items())]

    te = TransactionEncoder()
    te_fit = te.fit(languages).transform(languages)

    df = pd.DataFrame(te_fit, columns=te.columns_)

    frequent_items = apriori(df, min_support=0.4, use_colnames=True)
    print(frequent_items)
    print()
    print(association_rules(frequent_items, metric='confidence', min_threshold=0.7))


def frequent_items_ide(answers):
    ides = [item for item in list(ans['IDE'].split(';') for user, ans in answers.items())]

    te = TransactionEncoder()
    te_fit = te.fit(ides).transform(ides)

    df = pd.DataFrame(te_fit, columns=te.columns_)

    frequent_items = apriori(df, min_support=0.1, use_colnames=True)
    print(frequent_items)
    print()
    print(association_rules(frequent_items, metric='confidence', min_threshold=0.3))
