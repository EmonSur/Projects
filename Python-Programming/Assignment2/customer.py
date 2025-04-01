# Customer class
class Customer(object):
    def __init__(self, name, address, phoneNumber):

        if not name or not address or not phoneNumber:
            raise ValueError("Name, address, and phone number must not be empty.")

        if type(name) != str:
            raise ValueError("Name must be a string.")
        
        if type(address) != str:
            raise ValueError("Address must be a string.")
        
        if type(phoneNumber) != str:
            raise ValueError("Phone number must be a string.")
        
        if len(phoneNumber) != 10:
        # Assuming a 10-digit number for a valid phoneNumber
            raise ValueError("Invalid phone number.")
        
        self._name = name
        self._address = address
        self._phoneNumber = phoneNumber
        self._shoppingCart = ShoppingCart()

    def getName(self):
        return self._name

    def getAddress(self):
        return self._address
    
    def setAddress(self, address):
        if type(address) != str:
            raise ValueError("Address must be a string.")
        self._address = address

    def getPhoneNumber(self):
        return self._phoneNumber
    
    def setPhoneNumber(self, phoneNumber):
        if type(phoneNumber) != str:
            raise ValueError("Phone number must be a string.")
        self._phoneNumber = phoneNumber
        
    name = property(getName)
    address = property(getAddress, setAddress)
    phoneNumber = property(getPhoneNumber, setPhoneNumber)

    def addToCart(self, product, quantity=1):
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self._shoppingCart.addProduct(product, quantity)

    def removeFromCart(self, product, quantity=1):
        if not isinstance(product, Product):
            raise ValueError("Item to be removed must be a Product instance.")
        self._shoppingCart.removeProduct(product, quantity)

    def viewCart(self):
        print("Products in %s's Cart:" % self._name)
        print("-" * 50)
        self._shoppingCart.listProducts()

    def viewMyCart(self):
        print(self._shoppingCart.viewCart())

    def checkout(self):
        totalPrice = self._shoppingCart.calculateTotal()
        print("Checkout complete %s. Total amount: €%s. \n\nYour order will be delivered to the following address: \n%s" % (self._name, totalPrice, self._address))

# Product class
class Product:
    def __init__(self, name, price, description, category, inventory):

        if not name or not description or not category or not price:
            raise ValueError("Name, description, category, and price must not be empty ")

        if type(name) != str:
            raise ValueError("Name must be a string.")
        
        if type(price) != float and type(price) != int :
            raise ValueError("Price must be an integer or float.")
        
        if type(description) != str:
            raise ValueError("The description must be a string.")
        
        if type(category) != str:
            raise ValueError("The category must be a string.")
        
        if type(inventory) != int:
            raise ValueError("The inventory value must be an integer.")
        
        if inventory < 0:
            raise ValueError("It is not possible to have negative inventory.")
    
        self._name = name
        self._price = price
        self._description = description
        self._category = category
        self._inventory = inventory

    def __str__(self):
        return ("Name: %s\nPrice: €%.2f\nDescription: %s\nCategory: %s\nInventory: %d" %
            (self._name, self._price, self._description, self._category, self._inventory))

    def getName(self):
        return self._name
    
    def getPrice(self):
        return self._price

    def setPrice(self, price):
        if type(price) != float and type(price) != int :
            raise ValueError("Price must be an integer or float.")
        self._price = price
    
    def getDescription(self):
        return self._description
    
    def setDescription(self, description):
        if type(description) != str:
            raise ValueError("The description must be a string.")
        self._description = description
        
    def getCategory(self):
        return self._category
    
    def setCategory(self, category):
        if type(category) != str:
            raise ValueError("Category must be a string.")
        self._category = category

    def getInventory(self):
        return self._inventory
    
    def setInventory(self, inventory):
        if type(inventory) != int or inventory < 0:
            raise ValueError("Inventory must be a non-negative integer.")
        self._inventory = inventory  # Set the value
        
    name = property(getName)
    price = property(getPrice, setPrice)
    description = property(getDescription, setDescription)
    category = property(getCategory, setCategory)
    inventory = property(getInventory, setInventory)


# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self._products = []

    def addProduct(self, product, quantity=1):
        if product._inventory >= quantity:
            for _ in range(quantity):
                self._products.append(product)
                product._inventory -= 1
        else:
            print("%s does not have sufficient stock. Only %s available." % (product._name, product._inventory))

    def removeProduct(self, product, quantity=1):
        productCountInCart = self._products.count(product)

        if productCountInCart == 0:
            print("%s was not found in the cart." % product._name)
            return
        
        # If the desired quantity to remove is more than available
        if quantity > productCountInCart:
            raise ValueError("You're trying to remove more %s's than what's available in the cart." % product._name)
        
        for item in range(quantity):
            self._products.remove(product)
            product._inventory += 1


    def viewCart(self):
        if not self._products:
            return "Your cart is empty."

        product_counter = {}
        for product in self._products:
            if product._name in product_counter:
                product_counter[product._name] += 1
            else:
                product_counter[product._name] = 1

        cart_view = "\nItems in your cart:\n"
        cart_view += "-" * 40 + "\n"
        
        for product_name, count in product_counter.items():
            product_obj = next(x for x in self._products if x._name == product_name)
            cart_view += "%s (Quantity: %s) - €%s\n" % (product_name, count, product_obj._price * count)
        
        cart_view += "-" * 40 + "\n"
        cart_view += "Total: €%s\n" % self.calculateTotal()
        
        return cart_view
    
    def listProducts(self):
        if not self._products:
            print("Your cart is empty.")
            return
        unique_products = set(self._products) 
        for product in unique_products:
            print(str(product)) 
            print("Quantity in cart:", self._products.count(product))
            print("-" * 50)


    def calculateTotal(self):
        total = sum(product._price for product in self._products)
        return total

# Testing the Online Shopping System
if __name__ == "__main__":
    try:
        # Testing Product class
        product1 = Product("Laptop", 1000, "High-performance laptop", "Electronics", 10)
        product2 = Product("T-shirt", 20, "Cotton T-shirt", "Clothing", 10)
        product3 = Product("Headphones", 50, "Noise-canceling headphones", "Electronics", 8)
        
        # Testing Customer class
        customer = Customer("John Doe", "123 Main St", "0865554321")
        
        # Add products to the cart
        customer.addToCart(product1, 2)
        customer.addToCart(product2, 6)
        
        # Remove a product from the cart
        customer.removeFromCart(product1, 1)

        
        customer.viewMyCart()
        customer.viewCart()
        customer.checkout()

    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    print("\nTrying out invalid inputs:")

    # Examples of things that will raise errors:

    # Incorrect product price type
    try:
        product_error = Product("Toy", "Twenty", "A nice toy", "Toys", 10)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    # Incorrect customer address type
    try:
        customer_error = Customer("Alice", 12345, "0865554321")
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    # Negative inventory
    try:
        product_error2 = Product("Book", 20, "A good book", "Books", -5)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    # Incorrect phone number type
    try:
        customer_error2 = Customer("Bob", "123 Elm St", 9999999)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)