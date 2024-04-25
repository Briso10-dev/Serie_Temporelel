# importations des differents modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Calcule de la moyenne, la variance et l'écart-type
def calculate_statistics(data):
    mean = np.mean(data)
    variance = np.var(data)
    std_dev = np.std(data)
    return mean, variance, std_dev

# Representation de la série temporelle
def plot_time_series(data):
    x = np.arange(len(data))
    y = data

    plt.plot(x, y, '-o')
    plt.xlabel('Temps')
    plt.ylabel('Valeur(X)')
    plt.title('Série temporelle')
    plt.show()

# Representation des nuages de points N1,N2,...N8
def plot_scatter_plots(data):
    num_plots = len(data.columns)
    fig, axs = plt.subplots(num_plots, 1, figsize=(8, num_plots*4))
    
    for i, col in enumerate(data.columns):
        axs[i].scatter(data.index, data[col])
        axs[i].set_xlabel('Temps')
        axs[i].set_ylabel('Valeur')
        axs[i].set_title(f'Nuage de points {col}')
    
    plt.tight_layout()
    plt.show()

# Representation de la courbe des autocorrelations
def plot_autocorrelation(data):
    autocorr = pd.plotting.autocorrelation_plot(data)
    autocorr.set_xlim([1, 50])
    autocorr.set_ylim([-1, 1])
    plt.xlabel('Décalage (k)')
    plt.ylabel('Corrélation(ACF)')
    plt.title('Courbe des autocorrélations')
    plt.show()

# Génération des jeux de données:
# Jeu de donnees 1
n = 100  # Nombre d'observations
t = np.arange(1, n+1)
a = 2
b = 3

data_lineaire_trend = a * t + b # Tendance lineaire
noise1 = np.random.normal(0, 1, n) # Bruit aléatoire

#Serie temporelle
data1 = data_lineaire_trend + noise1

# Jeu de donnees 2
n = 100
t = np.arange(1, n+1)
a = 1

seasonality1 = a * np.cos(2 * t * np.pi / t) #saisonnalite sinusoïdale
noise2 = np.random.normal(0, 1, n) 

#Serie temporelle
data2 = seasonality1 + noise2

# Jeu de donnees 3 : Serie a tendance exponentielle
n = 100  
t = np.arange(1, n+1)
a = 2
b = 3

data_exponential_trend = a * np.exp(b * t) # Tendance exponentielle
seasonality2 = np.sin(2 * np.pi * t / 12)  #  saisonnalite sinusoïdale
noise3 = np.random.normal(0, 1, n)  

# Serie temporelle
data3 = data_exponential_trend + seasonality2 + noise3

# Jeu de données 4 : Serie avec une saisonnalite non periodique 
n = 100  
t = np.arange(1, n+1)
a = 1

data_linear_trend = a * t # Tendance lineaire
seasonality3 = np.random.normal(0, 1, n) #saisonnalite non périodique
noise4 = np.random.normal(0, 1, n) # Bruit aléatoire

# Serie temporelle
data4 = data_linear_trend + seasonality3 + noise4

# Jeu de données 5 : Serie avec tendance et saisonnalite multiples
n = 100 
t = np.arange(1, n+1)

# Tendance 1 (lineaire)
a1 = 1
b1 = 2
data_linear_trend_1 = a1 * t + b1
# Tendance 2 (exponentielle)
a2 = 0.5
b2 = 0.02
data_exponential_trend_2 = a2 * np.exp(b2 * t)

seasonality_1 = np.sin(2 * np.pi * t / 12)  # saisonnalite sinusoïdale
seasonality_2 = np.cos(2 * np.pi * t / 6)  # saisonnalite cosinusoïdale
noise5 = np.random.normal(0, 1, n) # Bruit aléatoire

# Serie temporelle
data5 = data_linear_trend_1 + data_exponential_trend_2 + seasonality_1 + seasonality_2 + noise5

# Statistiques et representations graphiques pour chaque jeu de donnees
datasets = [data1, data2,data3,data4,data5] 

for i, data in enumerate(datasets):
    print(f"Jeu de données {i+1}:")
    
    # Calcul des statistiques
    mean, variance, std_dev = calculate_statistics(data)
    print(f"Moyenne: {mean}")
    print(f"Variance: {variance}")
    print(f"Ecart-type: {std_dev}")
    
    # Representation de la serie temporelle
    plot_time_series(data)
    
    # Representation des nuages de points
    random_data = np.random.rand(len(data), 8)  # données aléatoires
    df = pd.DataFrame(random_data, columns=['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8'])
    plot_scatter_plots(df)
    
    # Representation de la courbe des autocorrélations
    plot_autocorrelation(data)
    
    print('\n')