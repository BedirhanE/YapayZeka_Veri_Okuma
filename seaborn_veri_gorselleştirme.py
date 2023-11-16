
#veri görselleştirme işlemleri

import seaborn as sns
import matplotlib.pyplot as plt

planets =sns.load_dataset("planets")
print(planets.head())




# Veri setini yükle
planets = sns.load_dataset("planets")

# Veri setinin ilk birkaç satırını yazdır
print(planets.head())

# Scatter plot (Nokta Grafiği)
sns.scatterplot(x='orbital_period', y='mass', data=planets)
plt.title('Orbital Period vs Mass')
plt.show()

# Box plot (Kutu Grafiği)
sns.boxplot(x='year', y='orbital_period', data=planets)
plt.title('Orbital Period by Year')
plt.show()

# Histogram
sns.histplot(x='distance', data=planets, bins=20, kde=True)
plt.title('Distribution of Distances')
plt.show()
