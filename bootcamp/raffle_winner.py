#Program by: Royce March 2, 2018 9:47 PM
#Description: This program shuffles a list of names and choose one  to be a winner in raffle!

from random import shuffle
from random import choice

names = [ "Jadwiga", "Illa", "Kimbery", "Carlene", "Brenton", "Eleanora", "Jacinto", "Lorita", "Lucas", "Mable", "Karine", "Venetta" ,"Deandre", "Arthur", "Jackeline", "Galina", "Brendan", "Mary" ,"Emelina" ,"Shona" ,"Wilbert" ,"Rivka" ,"Kori", "Owen" ,"Valentine", "Kimber" ,"Maritza"  ,"Ophelia"  ,"Shawanna" ,"Charisse", "Royce", "Sham", "Angelica", "Trisha", "Dy", "Arvs", "Ronnie", "Von", "Rommel", "Francis", "Abdol", "Niko", "Jelyn"]
shuffle(names)
winner = choice(names)
print(f'The winner is {winner}')