''' 
Le slicing permet d'extraire une sous séquence d'une séquence
Une séquence peut être :
- une_liste = ['a', 'b', 'c', 'd']
- un_tuple = ("a", "b", "c", "d")
- une_string = "chaine de caractere

Syntaxe du slicing : séquence[début:fin:fréquence]

Source : https://anislerouge.com/tutorial-python-slicing/
'''

ma_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Afficher les 3 premières valeurs
print(ma_list[:3])

# Afficher les 3 derniers 
print(ma_list[-3:])

# Afficher à l'envers
print(ma_list[::-1])

# Afficher un élément sur deux
print(ma_list[::2])

