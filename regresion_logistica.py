# Importación de librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# -----------------------------
# Etapa 1: Definición del problema
# -----------------------------
# Aquí se explica brevemente el objetivo del análisis
# Clasificación binaria: predecir si un paciente tiene diabetes (Outcome)

# -----------------------------
# Etapa 2: Carga y exploración de datos
# -----------------------------
df = pd.read_csv('/content/diabetes.csv')

# Vista previa de los datos
df.head()

# Información general del DataFrame
df.info()

# Estadísticas descriptivas
df.describe()

# -----------------------------
# Etapa 3: Análisis de la variable objetivo
# -----------------------------
# Conteo de cada clase
df['Outcome'].value_counts()

# Graficar variable Outcome
plt.figure(figsize=(3,3))
plt.pie(df['Outcome'].value_counts(), 
        labels=['No diabetes', 'Diabetes'], 
        autopct='%1.1f%%',
        startangle=90)
plt.show()

# -----------------------------
# Etapa 4: Preparación de datos
# -----------------------------
# Separación de características y variable objetivo
X = df.drop('Outcome', axis=1)
Y = df['Outcome']

X.info()

# División en conjunto de entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=123
)

print(X_train)

# -----------------------------
# Etapa 5: Entrenamiento del modelo
# -----------------------------
modelo = LogisticRegression()
modelo.fit(X_train, Y_train)  # Entrenamiento del modelo

# Score del modelo en datos de entrenamiento
modelo.score(X_train, Y_train)

# Coeficientes del modelo
modelo.coef_

# -----------------------------
# Etapa 6: Evaluación del modelo
# -----------------------------
y_pred = modelo.predict(X_test)
coef = confusion_matrix(Y_test, y_pred)
coef

# Métricas
Exa = (coef[0,0] + coef[1,1]) / coef.sum()
print('Exactitud =', Exa)

precision = coef[0,0] / (coef[0,0] + coef[0,1])
print('Presicion =', precision)

sensitividades = coef[0,0] / (coef[0,0] + coef[1,0])
print('Sensibilidad =', sensitividades)

especificidad = coef[1,1] / (coef[1,1] + coef[0,1])
print('Especificidad =', especificidad)

Puntaje_F1 = 2 * (precision * sensitividades) / (precision + sensitividades)
print('Puntaje F1 =', Puntaje_F1)
