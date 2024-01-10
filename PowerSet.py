a = 0b00101010
b = 0b10111100
print(bin(a))
print(bin(b))
		

print(bin(a & b))
print(a & b)
## & (= ET binaire) compare les deux valeurs binaires
## si a et b on un 1 en commun alors ca laisse 1 sinon c'est 0
## Donc a & b = (0b00101000)2 = (40)10

k = 2
print(bin(1<<k))
## avec k = 2
## on sait que (1)10 -> (0001)2 -> (1)2
## alors 1 << k décale de deux crans à gauche donc (1)2 devient (100)2 soit 4

print(bin(a & 1 << k))
print(a & 1<<k)
## a & 1 << k renvoie 0 car 
## a = 0b101010 et 1 << k = 0b100
## Sauf qu'on compare pas de <- à -> mais -> à <- soit la 1 << k[-1] avec a[-1]
## donc ca fait que a et 1 << k n'ont aucun 1 en commun ce qui renvoit 0


## & 	: Et Binaire
## << 	: décalage de bits vers la gauche
print("\n\n\n")

def powerset(E):
	"""
	Renvoie toute les parties de l'ensemble E
	"""
	P = []
	for i in range(2**len(E)):
		partie = []
		for j in range(len(E)):
			## Si i & 1 << j renvoie une valeur non nulle (car 0 = False et R* = True)
			if i & 1 << j:
				partie.append(E[j])
		P.append(partie)
	return P

def powerset_comp(E):
	return [[E[j] for j in range(len(E)) if i & 1 << j]		for i in range(2**len(E))]

print(powerset([1,2,3,4,5]))