"""
# Demonstrates import and random.choice

import random

coin = random.choice(["heads", "tails"])
print(coin)

# Demonstrates from

from random import choice

coin = choice(["heads", "tails"])
print(coin)


# Demonstrates randint

import random

number = random.randint(1, 10)
print(number)


# Demonstrates shuffle

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


# Demonstrates sys.argv

import sys

print("hello, my name is", sys.argv[1])


# Demonstrates IndexError

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


# Adds error checking

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])



# Demonstrates sys.exit

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])


# Demonstrates list slice

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)




# Demonstrates pip-installed package

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

# Demonstrates a t-rex

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])


# Demonstrates requests

import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(response.json())
# Demonstrates json

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(json.dumps(response.json(), indent=2))



# Demonstrates iterating over JSON

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
)
o = response.json()
for result in o["results"]:
    print(result["trackName"])


# Demonstrates own module

import sys

from sayings1 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
"""
# Demonstrates own module

import sys

from sayings2 import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
