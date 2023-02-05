import numpy as np

""" Créez un tableau Numpy aléatoire 2D et trouvez la somme de tous les éléments. """
random_table = np.random.randint(12, 89, size=(2, 5))
print(random_table.sum())

""" Concaténez deux tableaux Numpy 1D en un seul tableau Numpy 2D."""
table_1D = np.arange(12)
even_number, odd_number = table_1D[table_1D %2==0], table_1D[table_1D %2!=0]
table2D = np.concatenate((even_number, odd_number)).reshape(2, 6)
print(table2D)

""" Remplacer tous les éléments supérieurs à 2 par 7 dans un tableau Numpy 2D."""
tbale_sup = np.where(table2D > 2, 7, table2D)
print(tbale_sup)

""" Calculez la moyenne et la déviation standard pour chaque colonne d'un tableau Numpy 2D."""
mean, std = np.mean(table2D, axis=0), np.std(table2D, axis=0)
print(mean, std)

""" Normalisez les valeurs d'un tableau Numpy 1D en utilisant la formule (x - mean) / std."""
table_1D = np.arange(80, 90)
mean_, std_ = np.mean(table_1D), np.std(table_1D)
normalisation = (table_1D-mean_)/mean_ 
print(normalisation)

""" Trouvez le minimum, le maximum et la position de l'élément minimal et maximal dans un tableau Numpy 1D."""
min_, max_ = table_1D.min(), table_1D.max()
argmin_, argmax_ = table_1D.argmin(), table_1D.argmax()
TEXT = "min value: {}, max value: {} , position min value: {}, position max value: {}".format(min_, max_, argmin_, argmax_)
print(TEXT)

""" Extraire les éléments uniques d'un tableau Numpy 1D en utilisant la fonction numpy.unique."""
random_table_1D = np.random.randint(80, 83, size=15)
print(np.unique(random_table_1D))

""" Trouvez les 10 premiers éléments les plus fréquents dans un tableau Numpy 1D en utilisant la fonction numpy.bincount."""
random_1D = np.array([2,2,3,4,5,6,7,83,3,4,5,6,3,3,2,2])
top_10 = np.bincount(random_1D)
top_10.sort()
print(top_10[::-1][:10])

""" Effectuez une réduction cumulative sur un tableau Numpy 1D en utilisant la fonction numpy.cumsum."""
print(random_1D.cumsum())

""" Trouvez le produit de tous les éléments dans un tableau Numpy 1D en utilisant la fonction numpy.prod """
print(random_1D.prod())

""" Trouvez le produit de tous les éléments dans un tableau Numpy 2D en utilisant la fonction numpy.prod """
data_2D = random_1D.reshape(2, 8)
print(data_2D)
print(data_2D.prod(axis=0))