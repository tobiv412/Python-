#!/Users/victor.tobi/.pyenv/shims/python

planets = ["Mercury", "Venus", "Earth", "Mars"]

# for loop

for p in planets:
    print(p)

# Dictionaries
distance_from_sun ={
    "Mercury": 0.4,
    "Venus": 0.7,
    "Earth": 1,
    "Mars": 1.5
}

for key, value in distance_from_sun.items():
    print(key + "--> " + str(value))