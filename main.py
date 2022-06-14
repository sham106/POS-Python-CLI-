from customer import*
from product import*
from purchase import*


def menu():
    while True:
        print("@@@@ welcome to the best online store @@@")
        print("chose your operation")
        print("1 = customer* ")
        print("2 = purchase* ")
        print("3 = product* ")

        # options for the customer to choose
        option = int(input("Enter your choice: "))
        if option == 1:
            customer_menu()
        elif option == 2:
            purchase_operations()
        elif option == 3:
            product_menu()
        else:
            print("Try another option!")
            # return


menu()

