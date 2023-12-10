import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Sample dataset (list of transactions)
dataset = [
    ['Milk', 'Eggs', 'Bread'],
    ['Beer', 'Diapers'],
    ['Milk', 'Beer', 'Chips', 'Diapers'],
    ['Milk', 'Bread', 'Chips'],
    ['Eggs', 'Bread', 'Diapers']
]

# Convert the dataset to a one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Generate association rules
association_rules_df = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)

# Display frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# Display association rules with support and confidence
print("\nAssociation Rules:")
print(association_rules_df)
