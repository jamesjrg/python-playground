class Aquarium:
	def __init__(self, size="medium"):
		self.size = size
		self.fish = []
		self.water_temperature = 25  # in Celsius

	def add_fish(self, fish_name, fish_type):
		self.fish.append({
			"name": fish_name,
			"type": fish_type
		})
		return f"{fish_name} the {fish_type} has been added to the aquarium!"

	def list_fish(self):
		if not self.fish:
			return "The aquarium is empty!"
		return "\n".join([f"- {fish['name']} ({fish['type']})" for fish in self.fish])

	def feed_fish(self):
		if not self.fish:
			return "No fish to feed!"
		return f"Fed {len(self.fish)} fish in the aquarium!"

if __name__ == "__main__":
	tank = Aquarium("large")
	print(tank.add_fish("Nemo", "Clownfish"))
	print(tank.add_fish("Dory", "Blue Tang"))
	print("\nFish in the aquarium:")
	print(tank.list_fish())
	print("\n" + tank.feed_fish())