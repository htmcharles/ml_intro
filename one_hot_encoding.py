import pandas as pd

data = {
    'color': ['red','green', 'blue'],
    'size': ['S', 'M', 'L'],
    'location': ['Musanze', 'Kigali', 'Muhanga'],
    'price': [10.5, 20.0, 15.75],
    'delivery': ['drone', 'truck', 'car']
}

df = pd.DataFrame(data)

one_hot_encoded_df = pd.get_dummies(df, columns=['color', 'size', 'location', 'delivery'])
one_hot_encoded_df = one_hot_encoded_df.astype('int')

print(one_hot_encoded_df)
