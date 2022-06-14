from product import*
import product
import customer
from customer import*

purchase_data = []


def purchase_operations():
    print(" ")


# search and make a purchase

class Purchase:
    def __init__(self,customer_id, customer_name, product_id,product_quantity,):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.product_id = product_id
        self.product_quantity = product_quantity

    def __str__(self):
        return f"{self.customer_id} {self.customer_name} { self.product_id} {self.product_quantity}"


def make_a_purchase():
    customer.show_customer()
    product.show_product()
    customer_id = input("Enter your customer ID: ")
    customer_name = input("Enter your first name: ")
    product_id = input("choose the id of product to purchase: ")
    quantity_to_purchase = input("Enter the quantity: ")
    purchase = Purchase(customer_id, customer_name, product_id, quantity_to_purchase)


    # check if the customer is available
    customer_exists = False
    product_exists = False
    for c in customer.customers_data:
        if customer_id == c.customer_id:
            customer_exists = True
            print("customer is available")
        else:
            print(" Customer Not available")
            break
# check if product is available
        for p in product.product_data:
            if product_id == p.product_id:
                product_exists = True
                print("product available")
            else:
                print("product is not available now")

        # Update purchase made
            if customer_exists and product_exists:
                purchase_file = open("purchase.txt", "a")
                purchase_data.append(purchase)
                purchase_file.write(str(purchase) + "\n")

         #print(product_quantity)



make_a_purchase()








