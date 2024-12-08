class Fish:
	def __init__(self, species, color, size):
		self.species = species
		self.color = color
		self.size = size
		self.is_swimming = False

	def swim(self):
		self.is_swimming = True
		return f"The {self.color} {self.species} is swimming!"

	def stop_swimming(self):
		self.is_swimming = False
		return f"The {self.color} {self.species} has stopped swimming."

	def __str__(self):
		return f"A {self.size} {self.color} {self.species}"

# Example usage
if __name__ == "__main__":
	goldfish = Fish("Goldfish", "orange", "small")
	tuna = Fish("Tuna", "silver", "large")

	print(goldfish)
	print(tuna.swim())