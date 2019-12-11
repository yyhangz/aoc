def trace_santa(node, planet):
    global visited_planets
    visited_planets.add(str(planet))
    for item in orbit_map[planet]:
        try:
            if item not in visited_planets and str(item) != "SAN":
                trace_santa(node+1, str(item))
            elif str(item) == "SAN":
                print(f"distance to santa: {node-2}")
        except KeyError:
            print(f"branch ended at {item}, node is {node}")

filename = 'd06_input'
with open(filename, 'r') as f:

    orbits = f.readlines()

orbit_map = {}
visited_planets = set()

for item in orbits:
    planets = item.strip().split(")")
    for i in range(2):
        if planets[i] not in orbit_map:
            orbit_map[planets[i]] = set()
        orbit_map[planets[i]].add(str(planets[1-i]))

current = 'YOU'
trace_santa(1, current)