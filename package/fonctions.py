# -*- coding:utf8 -*-

"""module fonctions contenant la fonction table"""

import os

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1)* nb)
        i += 1