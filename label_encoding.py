from sklearn.preprocessing import LabelEncoder

data = ["small", "medium", "large", "small", "large"]

labe_encoder = LabelEncoder()
encoded_data = labe_encoder.fit_transform(data)

print(encoded_data)  # Output: [2 1 0 2 0]


