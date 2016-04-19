#!/usr/bin/python2.7

print("Bienvenue dans le calculator 3000.\n")
print("Entrez 1 pour activer le mode calcul de puissance.")
print("Entrez 2 pour activer le mode calcul de complexes.")
print("Entrez 3 pour activer le mode calcul de tables de multiplications.")
print("Entrez 4 pour activer le mode calcul de multiplications.")
print("Entrez 5 pour activer le mode calcul de divisions.")
print("Entrez 6 pour activer le mode calcul de restes.")
print("Entrez 7 pour activer le mode calcul d'additions.")
print("Entrez 0 pour quitter le programme.\n")

while 1:
	mode = input("\nVeuillez selectionner le mode : ")
	mode = int(mode)
	if mode == 1:
		power = input("Tapez le nombre dont vous voulez obtenir la puissance : ")
		print "La puissance de", power, "est", power * power, ".\n"
	elif mode == 2:
		cplx = input("Tapez le nombre dont vous voulez obtenir la complexe : ")
		print "La valeur complexe de", cplx, "est", cplx * cplx, ".\n"
	elif mode == 3:
		mult = input("Tapez le nombre dont vous voulez calculer les tables de multiplications : ")
		i = 1
		while i <= 10:
			print i, "*", mult, "=", i * mult
			i += 1
	elif mode == 0:
		print("Fin de la boucle.")
		break
	elif mode == 4:
		mult_one = input("Veuillez entrer le premier nombre a multiplier : ")
		mult_two = input("Veuillez entrer le second nombre a multiplier : ")
		print "Le resultat de la multiplication de", mult_one, "par", mult_two, "est", mult_one * mult_two
	elif mode == 5:
		div_one = input("Veuillez entrer le premier nombre a diviser : ")
		div_two = input("Veuillez entrer le second nombre a diviser : ")
		print "Le resultat de la division de", div_one, "par", div_two, "est", div_one / div_two
	elif mode == 6:
		mod_one = input("Veuillez entrer le premier nombre a diviser : ")
		mod_two = input("Veuillez entrer le second nombre a diviser : ")
		print "Le reste de la division de", mod_one, "par", mod_two, "est", mod_one % div_two
	elif mode == 7:
		add_one = input("Veuillez entrer le premier nombre a additionner : ")
		add_two = input("Veuillez entrer le second nombre a additionner : ")
		print "Le resultat de l'addition de", add_one, "et", add_two, "est", add_one + add_two
	else:
		print("Le mode que vous tentez d'utiliser n'existe pas, reessayez.")
