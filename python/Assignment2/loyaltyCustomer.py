from customer import Customer, Product

# LoyaltyCustomer class
class LoyaltyCustomer(Customer):
    def __init__(self, name, address, phoneNumber, loyaltyNumber):
        super().__init__(name, address, phoneNumber)

        if type(loyaltyNumber) != str:
            raise ValueError("Loyalty number must be a string.")
        elif not loyaltyNumber:
            raise ValueError("Loyalty number must not be empty.")
        
        self._loyaltyNumber = loyaltyNumber
        self._loyaltyPoints = 0
        self._loyaltyDiscount = 0.15 

    def getLoyaltyNumber(self):
        return self._loyaltyNumber
    
    def setLoyaltyNumber(self, loyaltyNumber):
        if not loyaltyNumber:
            raise ValueError("Loyalty number must not be empty.")
        elif type(loyaltyNumber) != str:
            raise ValueError("Loyalty number must be a string.")
        self._loyaltyNumber = loyaltyNumber

    loyaltyNumber = property(getLoyaltyNumber, setLoyaltyNumber)

    def earnLoyaltyPoints(self, points):
        if not isinstance(points, int):
            raise ValueError("Points must be an integer.")
        elif points > 0:
            self._loyaltyPoints += points
        else:
            raise ValueError("Loyalty points cannot be less than zero.")

    def applyLoyaltyDiscount(self, totalAmount):
        if totalAmount < 0:
            raise ValueError("Total amount must be a positive value.")
        discount = totalAmount * self._loyaltyDiscount
        return totalAmount - discount

    # Override the checkout method to apply loyalty discount
    def checkout(self):
        totalPrice = self._shoppingCart.calculateTotal()
        discountedPrice = self.applyLoyaltyDiscount(totalPrice)
        print("Checkout complete for Loyalty Customer %s (Loyalty Number: %s)." % (self._name, self._loyaltyNumber))
        print("Total amount before discount: €%s." % (totalPrice))
        print("Loyalty discount applied: €%s." % (totalPrice - discountedPrice))
        print("Total amount after discount: €%s." % (discountedPrice))
        print("Your order will be delivered to the following address: \n%s" % (self._address))

if __name__ == "__main__":
    try:
        # Testing products
        product1 = Product("Laptop", 1000, "High-performance laptop", "Electronics", 10)
        product2 = Product("T-shirt", 20, "Cotton T-shirt", "Clothing", 5)
        product3 = Product("Headphones", 50, "Noise-canceling headphones", "Electronics", 8)

        # Change the price
        product1._price = 50

        # Testing Customer class
        customer1 = Customer("John Doe", "123 Main St", "0865554321")
        customer1.addToCart(product1)
        customer1.addToCart(product2)
        customer1.removeFromCart(product2)
        customer1.checkout()

        print("\n")

        # Testing LoyaltyCustomer class
        loyaltyCustomer = LoyaltyCustomer("Alice Smith", "456 Elm St", "0871234567", "LC123")
        loyaltyCustomer.addToCart(product1)
        loyaltyCustomer.addToCart(product3)
        loyaltyCustomer.earnLoyaltyPoints(50)
        loyaltyCustomer.checkout()

    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    print("\nTrying out invalid inputs:")

    # Examples of things that will raise errors:

    # Incorrect loyalty number type for LoyaltyCustomer
    try:
        loyaltyCustomerError = LoyaltyCustomer("Bob", "789 Pine St", "0879876543", 45678)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    # Incorrect phone number type for regular Customer
    try:
        customerError = Customer("Charlie", "101 Maple St", 1010101010)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    # Negative loyalty points
    try:
        loyaltyCustomer2 = LoyaltyCustomer("David", "112 Oak St", "0881122334", "LC456")
        loyaltyCustomer2.earnLoyaltyPoints(-20)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)