"""
# Validates email address by checking for @

email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")

# Validates email address by checking for . too

email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")



# Validates email address by checking username and domain separately

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")

# Validates email address by checking whether domain ends with .edu

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

# Validates email address by checking for @ with regex

import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")


# Adds .*

import re

email = input("What's your email? ").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")

# Changes * to +

import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")

# Adds \.edu

import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")


# Adds ^ and $ to regex

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# Adds character class

import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# Replaces character class with \w

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(com|edu|gov|be)$", email):
    print("Valid")
else:
    print("Invalid")


# Adds re.IGNORECASE

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# Adds optional subdomain

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



# Reformats "last, first" as "first last"

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")

# Uses re.search

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = first + " " + last
print(f"hello, {name}")

# Uses walrus operator

import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")


# Extracts Twitter username from URL using str.replace

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
"""

# Extracts Twitter username from URL using str.removeprefix

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")

# Uses re.sub

import re

url = input("URL: ").strip()

username = re.sub(r"^https://twitter\.com/", "", url)
print(f"Username: {username}")

# Uses capture group

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))

# Ignores query and fragment

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))

# check this link: https://cs50.harvard.edu/python/2022/weeks/7/