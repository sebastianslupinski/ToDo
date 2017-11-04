from model import TodoItem, TodoItems


def print_welcome_screen():

    print("                               ===Welcome in ToDo App===")

def print_program_menu():

    menu_commands = ("Add item", "Mark item", "Unmark item", 
                "Show all items", "Remove item",
                "Change item name", "Change item description", "Show exact item details", "Exit")

    for option in menu_commands:
        print(str(menu_commands.index(option)) + "----->" + option)

def print_items_list(TodoItems):

    print(TodoItems)

def print_item(item):

    print(item)

def print_name_too_long():

    print("Name too long !")

def print_description_too_long():

    print("Description too long !")

def print_wrong_index():

    print("Wrong index !")

