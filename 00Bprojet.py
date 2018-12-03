year = input("Saisissez une année :")
year = int(year)

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")