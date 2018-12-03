year = input("saisissez une année:")
year = int(year)
bissextile = False

if year % 400 == 0:
    bissextile = True
elif year % 100 == 0:
    bissextile = False
elif year % 4 == 0:
    bissextile = True
else:
    bissextile = False   


#if year / 4 and year / 100 and year / 400:
#    print("C'est une année bissextile")
#else:
#    print("Ce n'est pas une année bissextile")



