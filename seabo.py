import seaborn as sns
import matplotlib.pyplot as plt

data = [1,2,2,3,3,3,4,4,5]
sns.histplot(data, bins=5, kde=True)  # bins: número de barras, kde: curva de densidad
plt.show()
