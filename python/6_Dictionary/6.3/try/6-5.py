river = {
    'nile': 'egypt',
    'huanghe': 'china',
    'changjiang': 'china',
}
for river_0,country in river.items():
    print("The " + river_0.title() + " runs through " + 
    country.title() + ".")

print("\n")
for river_1 in river.keys():
    print("river: " + river_1)

print("\n")
for country_1 in river.values():
    print("Country: " + country_1)