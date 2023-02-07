import pandas as pd
import numpy as np
import pathlib

FILE_DATA = pathlib.Path(__file__).parent.parent.joinpath("data/data_pret.csv")
data_csv = pd.read_csv(FILE_DATA)

"""Importez une base de données à partir d'un fichier CSV ou Excel et explorez les données en utilisant des méthodes telles que head, tail, info et describe. """
print(
    data_csv.head(10),
    data_csv.tail(10),
    data_csv.info(),
    data_csv.describe(),
    data_csv.describe(percentiles=[.1, .2, .3, .7, .9]),
    sep="\n"
)

""" Afficher les statistiques pour les colonnes numériques incluant le 10e, 50e et 90e percentile """
print(
    data_csv.describe(percentiles=[.1, .5, .9])
)

"""Sélectionnez des colonnes spécifiques du DataFrame en utilisant le slicing et les méthodes telles que loc et iloc. """
""" slicing """
print(data_csv[['revenu', 'taux', 'remboursement']])

""" 
    loc est utilisé pour sélectionner des lignes en utilisant des étiquettes, par exemple :
    loc: selection la ligne dont le revenu est >=  5118.0, ville NICE, et toutes les colonnes"""
print(data_csv.loc[(data_csv['revenu']>=5118) & (data_csv['ville']=='NICE') & (data_csv['taux']>=1.1844), :])

""" 
    iloc est utilisé pour sélectionner des lignes en utilisant des indices entiers, par exemple :
    iloc, meme resultat avec iloc"""
index_value = data_csv.index[(data_csv['revenu']>=5118) & (data_csv['ville'] == 'NICE') & (data_csv['taux']>=1.1844)]
print(data_csv.iloc[index_value, :])

"""Effectuez des opérations de filtrage sur le DataFrame en utilisant les conditions booléennes et les méthodes telles que isin, where et query. """
""" isin """
ville_search = ['NICE', 'TOULOUSE']
print(data_csv[data_csv['ville'].isin(ville_search)])

""" where """
wh = data_csv.where((data_csv['taux']>=3) & (data_csv['ville'] == 'PARIS')).dropna(how='all')
print(wh)

""" query """
q = data_csv.query('taux > 3 and duree ==64')
    # or even if there's a difference
q = data_csv.query('taux > 3 & duree ==64')
print(q)

"""Sauvegardez le DataFrame résultant dans un fichier CSV ou Excel à l'aide de la méthode to_csv ou to_excel. """
data_csv.to_csv("data_csv.csv")