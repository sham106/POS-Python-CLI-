import os

customers_data = []


class Customer:
    def __init__(self, customer_id, first_name, second_name, phone_number, email, city ):
        self.customer_id = customer_id
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.email = email
        self.city = city

    def __str__(self):
        return f"{self.customer_id} {self.first_name}  {self.second_name} { self.phone_number} {self.email}  {self.city}"


def customer_menu():
    print("chose your operation")
    print("1 = add_customer* ")
    print("2 = delete_customer_features* ")
    print("3 = update_customer* ")

    # options for the customer to choose
    option = int(input("Enter your choice: "))

    while True:
        if option == 1:
            add_customer()
        elif option == 2:
            delete_customer_features()
        elif option == 3:
            update_customer()
        else:
            print("Try another option!")
            return


def add_customer():
    # Loading customer data into the file
    while True:
        customer_id = input("Enter  the customer id: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        phone = input("Enter phone number: ")
        email = input("Enter your e-mail address: ")
        city = input("Name of your city: ")
        customer = Customer(customer_id,first_name, last_name, phone, email, city)
        outfile = open("customer.txt", "a")
        customers_data.append(customer)
        outfile.write(str(customer) + "\n")

        print("added successfully")
        option = int(input("choose 1 to add more or 2 to stop: "))
        if option == 1:
            continue
        else:
            quit()


# Deleting customer features
def delete_customer_features():
    with open("customer.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        cust_to_delete = input("Enter the customer id to delete: ")
        for line in new_f:
            if cust_to_delete in line:
                f.write(line)
        f.truncate()
        print("deleted successfully")


def update_customer():
    with open("customer.txt", "r+") as f:
        file = f.readlines()
        cust_to_update = input("Enter the id of customer to update: ")
        first_name = input("Enter your first name: ")

        last_name = input("Enter your last name: ")

        phone = input("Enter phone number: ")

        email = input("Enter your e-mail address: ")
        city = input("Name of your city: ")
        up_customer = f'{cust_to_update} {first_name} {last_name} {phone} {email} {city}'
        for line in file:
            if cust_to_update in line:
                index = file.index(line)

    file[index] = up_customer
    with open ("customer.txt", "w") as fw:
        for line in file:
            fw.write(line + "\n")


            #     add_customer()
            #
            #     customer_id = input("Enter  the customer id :")
            #
            #
            #
            #
            #     #utfile = open("customer.txt", "a")
            #     customers_data.append(customer)
            #     outfile.write(str(customer) + "\n")
            #     f.seek(0)
            #     f.writelines(file)
            # f.close()


def show_customer():
    #customer_id = input("enter id: ")
    file = open("customer.txt", "r")
    for i in file:
        #if customer_id in i:
        cus_details = i.split()
        #print(cus_details[3])
        customer_id = cus_details[0]
        first_name = cus_details[1]
        last_name = cus_details[2]
        phone = cus_details[3]
        email = cus_details[4]
        city = cus_details[5]
        customer = Customer(customer_id, first_name, last_name, phone, email, city)
        customers_data.append(customer)
    print(cus_details)



show_customer()

#update_customer()
