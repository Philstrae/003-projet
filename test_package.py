
try:
    import package.fonctions
    fonctions.table(5) # Appel de la fonction table

except NameError:
    print("La variable n'a pas été définie.")

except TypeError:
    print("La variable possède un type incompatible avec la division.")

except ZeroDivisionError:
    print("La variable est égale à 0.")

else:    
    from package.fonctions import table
    table(5) # Appel de la fonction table