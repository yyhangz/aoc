def get_length(node, planet):
    global total_orbits
    for item in orbit_map[planet]:
        try:
            total_orbits += node
            get_length(node+1, str(item))
        except KeyError:
            print(f"branch ended at {item}, node is {node}")
        

filename = 'd6_input'
with open(filename, 'r') as f:

    orbits = f.readlines()

orbit_map = {}
orbiting_planets = set()

for item in orbits:
    planets = item.strip().split(")")
    if planets[0] not in orbit_map:
        orbit_map[planets[0]] = set()
    orbit_map[planets[0]].add(planets[1])
    orbiting_planets.add(str(planets[1]))


total_orbits = 0
for planet in orbit_map:
    if str(planet) not in orbiting_planets:
        get_length(1, str(planet))
    else:
        pass
print(total_orbits)