#import numpy as np

species_data = [
    {'name': 'Lion', 'populations': {'Africa': 3000, 'India': 500}},
    {'name': 'Elephant', 'populations': {'Africa': 20000, 'Asia': 10000}},
    {'name': 'Panda', 'populations': {'China': 1800}},
]

# def total_pop_calculator(species_data):
#     for species in species_data:
#         total_pop = sum(species['populations'].values())  # Sum all the population values
#         print(f"a) Total population of {species['name']}: {total_pop}")

# def highest_population(species_data):
#     highest_pop = 0
#     for species in species_data:
#         total_pop = sum(species['populations'].values()) # population of first species
#         if total_pop > highest_pop : 
#             highest_pop = total_pop # remember the highest population
#             animal = species
#     print(f"b) {species['name']} has the highest population with a total of {highest_pop} individuals.") 

print("a)")
for species in species_data:
    total_pop = sum(species['populations'].values())  # Sum all the population values
    print(f"  > Total population of {species['name']}: {total_pop}")


highest_pop = 0
for species in species_data:
    total_pop = sum(species['populations'].values()) # population of first species
    if total_pop > highest_pop : 
        highest_pop = total_pop # remember the highest population
        animal = species
 
print(f"b) {animal['name']}s have the highest population with a total of {highest_pop} individuals.") 
    