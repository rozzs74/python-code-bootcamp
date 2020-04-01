# Date created: July 21, 2018
# Created by: Royce
# Set usage


dc = ["Flash", "Superman", "Batman", "Wonderwoman", "Cyborg", "Batman"]
marvel =["Iron man", "Hulk", "Thor", "Captain America", "Spider-man", "Hulk"]

dc = set(dc)
marvel = set(marvel)

print(dc)
print(marvel)
print(dc.union(marvel))
print(dc.intersection(marvel))
print(dc.difference(marvel))
print(marvel.difference(dc))
print(dc.symmetric_difference(marvel))

print("===")

print(dc | marvel)