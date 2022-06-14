import fileinput
import sys
import os
import random
product_data = []


class Product:
    def __init__(self, product_id, product_name, price, product_type, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self. price = price
        self.product_type = product_type
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_id} {self.product_name} {self.price} {self.product_type} {self.quantity}"


def product_menu():
    print("chose your operation")
    print("1 = add_product* ")
    print("2 = Readfile(to load data into array* ")
    print("3 = insert new product* ")
    print("4 = delete product* ")
    print("5 = update_product* ")

    # options for the customer to choose
    option = int(input("Enter your choice: "))

    while True:
        if option == 1:
            add_product()
        elif option == 2:
            readfile()
        elif option == 3:
            insert_new_product()
        elif option == 4:
            delete_product()
        elif option == 5:
            update_product()
        else:
            print("Try another option!")
            return


def add_product():
    # Write product data into a file
    while True:
        product_id = input("Enter product id: ")
        product_name = input("enter product name: ")
        price = input("Enter price of the product: ")
        product_type = input("Enter the type of the product: ")
        product_quantity = input("Enter the quantity: ")
        product = Product(product_id, product_name, price, product_type, product_quantity)
        product_file = open("product.txt", "a")
        product_data.append(product)
        product_file.write(str(product) + "\n")
        print("Product added successfully.")



# Loading product data into array
def readfile():
    product_file = open("product.txt", "r")
    words = product_file.read().splitlines()  # puts the file into array
    product_file.close()
    return words


# Inserting new product
def insert_new_product():
    print("enter the details of new product")
    add_product()


# deleting a product
def delete_product():
    with open("product.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        pro_to_delete = input("Enter the product id to delete: ")
        for line in new_f:
            if pro_to_delete not in line:
                f.write(line)
        f.truncate()
        print("successfully deleted:")


# Updating a product
def update_product():
    with open("product.txt", "r+") as f:
        file = f.readlines()
        prod_to_update = input("Enter the id of product to update: ")
        new_product_name = input("Enter new /retain name of the product: ")

        new_price = input("Enter the new price: ")

        type_of_product = input("Enter type of the product: ")

        new_quantity = input("Enter the update quantity: ")

        up_product = f'{prod_to_update} {new_product_name} {new_price} {type_of_product} {new_quantity}'
        for line in file:
            if prod_to_update in line:
                index = file.index(line)

    file[index] = up_product
    with open("product.txt", "w") as fw:
        for line in file:
            fw.write(line + "\n")


def show_product():
    file = open("product.txt", "r")
    for i in file:
        pro_detail = i.split()
        product_id = pro_detail[0]
        product_name = pro_detail[1]
        price = pro_detail[2]
        product_type = pro_detail[3]
        product_quantity = pro_detail[4]
        product = Product(product_id, product_name, price, product_type, product_quantity)
        product_data.append(product)
        print(product_id)

    # delete_product()
#show_product()

#update_product()