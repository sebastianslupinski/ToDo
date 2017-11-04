from model import TodoItem, TodoItems
import view


def main():

    itemslist = TodoItems()

    while True:

        view.print_program_menu()
        option = input("Please select an option:")

        if option == "0":

            item_name = input("Please enter a name of action to do: ")

            if check_if_name_too_long(item_name):
                print("Name too long !")
                continue

def check_if_name_too_long(name):

    if len(name) > 20:
        return True
    else:
        return False

def check_if_descr_too_long(desc):

    if len(desc) > 50:
        return True
    else:
        return False

main()
