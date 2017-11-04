from model import TodoItem, TodoItems


def print_welcome_screen():

    print("                               ===Welcome in ToDo App===")

def print_program_menu():

    menu_commands = ("Add item", "Mark item", "Unmark item", 
                "Show all items", "Remove item",
                "Change item name", "Change item description", "Exit")

    for option in menu_commands:
        print(str(menu_commands.index(option)) + "----->" + option)

def print_items_list(items):

    print(items)

def print_item(item):

    print(item)

