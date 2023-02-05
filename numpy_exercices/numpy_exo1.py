import numpy as np
"""Créez un tableau Numpy 1D contenant les nombres entiers de 0 à 9."""
table_num01 = np.arange(10)
print(table_num01)

"""Convertir le tableau 1D en un tableau 2D de forme (3,3)."""
reshape3x3 = table_num01[:-1].reshape(3,3)
print(reshape3x3)

"""Remplacer tous les éléments négatifs du tableau 2D par 0."""
table_negatif = np.arange(-3, 6).reshape(3,3)
table_negatif = np.where(table_negatif < 0, 0, table_negatif)
print(table_negatif)

"""Calculez la somme de tous les éléments du tableau 2D."""
print(table_negatif.sum())

"""Calculez la moyenne de tous les éléments du tableau 2D."""
print(table_negatif.mean())

"""Trouvez l'index du plus petit élément du tableau 1D."""
table_1d = np.arange(5, 10)
np.random.shuffle(table_1d)
print(table_1d.argmin())


"""Effectuer une rotation de 90 degrés sur le tableau 2D."""
table_2d = np.arange(9).reshape(3,3)
table_2d = np.rot90(table_2d)
print(table_2d)

"""Triez le tableau 1D en ordre décroissant."""
table_sort = np.arange(11)
np.random.shuffle(table_sort)
table_sort.sort()
print(table_sort[::-1])