import re

products = [
"Apple iPhone",
"Apple Watch",
"Samsung Galaxy",
"Galaxy Buds",
"Wireless Mouse",
"Gaming Mouse",
"Bluetooth Speaker",
"Smart Speaker",
"USB Cable",
"Laptop Stand"
]

print("========== PRODUCT SEARCH SYSTEM ==========")

keyword = input("Enter Search Keyword : ")

exact = []
prefix = []
suffix = []
partial = []
case = []

for product in products:

    if re.fullmatch(keyword, product):
        exact.append(product)

    if re.match(keyword, product):
        prefix.append(product)

    if re.search(keyword + r"$", product):
        suffix.append(product)

    if re.search(keyword, product):
        partial.append(product)

    if re.search(keyword, product, re.I):
        case.append(product)

print("\nExact Match")
print(exact)

print("\nPrefix Match")
print(prefix)

print("\nSuffix Match")
print(suffix)

print("\nPartial Match")
print(partial)

print("\nCase Insensitive Match")
print(case)

print("\nSearch Report")
print("Exact Matches :", len(exact))
print("Prefix Matches:", len(prefix))
print("Suffix Matches:", len(suffix))
print("Partial Matches:", len(partial))
print("Case-insensitive Matches:", len(case))

