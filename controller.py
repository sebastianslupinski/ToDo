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
                view.print_name_too_long()
                continue

            item_description = input("Please write description for item: ")

            if check_if_descr_too_long(item_description):
                view.print_description_too_long()
                continue

            itemslist.add_item(item_name, item_description)

        elif option == "1":

            view.print_items_list(itemslist)

            item_position = input("Which position you want to mark ?: ")

            if check_if_index_is_good(item_position, itemslist) is True:
                view.print_wrong_index()
                continue

            index = check_if_index_is_good(item_position, itemslist)

            itemslist.get_item(index).mark()
            
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

def check_if_index_is_good(index, itemslist):

    try:
        index = int(index)
    except ValueError:
        return True

    if (index) >= len(itemslist.items):
        return True

    return index

main()
