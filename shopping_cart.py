import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]


item = 1
cart = []



# Checkpoint 1
while True:
	try:
		item = input("Please input a product item number, or 'Done' if there are no more items:")
		if item == "Done":
			break
		if item != "Done":
			if int(item) > 20 or int(item) < 1:
				item = input("Please input a valid product item number:")
			elif int(item) > 0 and int(item) < 21:
				cart.append(int(item))
	except ValueError:
		print("Error.")


#Checkpoint 2
import operator

print ("---------------")
print ("Sofiya's Grocery")
print ("---------------")
print ("Web: www.sofiyasgrocery.com")
print ("Phone: 123-456-7890")
print ("Checkout Time:", datetime.datetime.now().strftime("%B %d,%Y %I:%M %p"))
print ("---------------")

print ("Shopping cart items include:")

ids = []
for product in products:
	ids.append(product["id"])
#print (ids)
subtotal = 0
for num in ids:
	if num in cart:
		freq = cart.count(num)
		subtotal = subtotal + products[num-1]["price"]*freq
		print ("+", products[num-1]["name"], ', ${0:.2f}'.format(products[num-1]["price"]), 'x', freq)


tax = subtotal*0.08875
totalprice = subtotal+tax


print ("---------------")
subtotal = '${0:.2f}'.format(subtotal)
print ("Subtotal:", subtotal)
tax = '${0:.2f}'.format(tax)
print ("Sales Tax (8.875%):", tax)
totalprice = '${0:.2f}'.format(totalprice)
print ("Total:", totalprice)
print ("---------------")
print ("Thanks for your business. Please come again.")
