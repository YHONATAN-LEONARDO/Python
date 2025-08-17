import pandas as pd

s = pd.Series([1,2,3,4,5])

data = {
    'Nombre': ['Ana', 'Luis', 'Marta'],
    'Edad': [23, 34, 29],
    'Ciudad': ['La Paz', 'Cochabamba', 'Santa Cruz']
}
df = pd.DataFrame(data)

df = pd.read_csv("Automobile_data.csv")

print(df.info())

print("-"*30)
print(df['price'])