FISH_SPECIES = {
	"tropical": [
		{
			"name": "Guppy",
			"scientific_name": "Poecilia reticulata",
			"water_type": "freshwater",
			"size_cm": 3
		},
		{
			"name": "Neon Tetra",
			"scientific_name": "Paracheirodon innesi",
			"water_type": "freshwater",
			"size_cm": 2.5
		},
		{
			"name": "Clownfish",
			"scientific_name": "Amphiprioninae",
			"water_type": "saltwater",
			"size_cm": 11
		}
	],
	"coldwater": [
		{
			"name": "Goldfish",
			"scientific_name": "Carassius auratus",
			"water_type": "freshwater",
			"size_cm": 20
		},
		{
			"name": "Koi",
			"scientific_name": "Cyprinus rubrofuscus",
			"water_type": "freshwater",
			"size_cm": 60
		}
	]
}

def get_fish_by_type(water_type):
	all_fish = []
	for category in FISH_SPECIES.values():
		all_fish.extend([fish for fish in category if fish["water_type"] == water_type])
	return all_fish

def get_fish_by_size(min_size, max_size):
	all_fish = []
	for category in FISH_SPECIES.values():
		all_fish.extend([fish for fish in category if min_size <= fish["size_cm"] <= max_size])
	return all_fish

if __name__ == "__main__":
	print("Freshwater fish:", get_fish_by_type("freshwater"))
	print("\nSmall fish (under 5cm):", get_fish_by_size(0, 5))