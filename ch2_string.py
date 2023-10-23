name = "ada lovelace"
print(name.title())

print(name.upper())

print(name.lower())

first_name = "ada"
last_name = "lovelace"

# f-string, from python 3.6
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"{first_name.upper()} {last_name.upper()}")

# remove space
print(full_name.rstrip())
print(full_name.lstrip())
print(full_name.strip())

# Long number
universe_age = 14_000_000_000
print(universe_age)

# Multi- assignment
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

