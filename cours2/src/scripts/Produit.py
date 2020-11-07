class Produit:
	def __init__(self):
		print("Création de l'instance")

	# Définir la méthode __call__.
	def __call__(self, a, b):
		print(a * b)

# Création de l'instance
ans = Produit()

# La méthode __call__ sera appelée
ans(10, 20)