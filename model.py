class TodoItem():

    id = 0

    def __init__(self, name, description, is_done=False):

        self.name = name
        self.description = description
        self.is_done = is_done
        self.id = TodoItem.id
        TodoItem.id += 1

    def change_name(self, new_name):

        self.name = new_name

    def change_description(self, new_description):

        self.description = description

    def mark(self):
        self.is_done = True

    def unmark(self):
        self.is_done = False

    def __str__(self):

        info = ''

        if self.is_done == True:
            info += '[x] '

        elif self.is_done == False:
            info += '[ ] '

        info += str(self.id) + " - " + str(self.name) + " - " + str(self.description)

        return info

class TodoItems():

    def __init__(self):

        self.items = []

    def add_item(self, name, description, is_done = False):

        #if type(deadline) is not datetime:
            #raise ValueError

        self.items.append(TodoItem(name, description, is_done))

    def get_item(self, index):

        return self.items[index]

    def remove_item(self, index):

        self.items.pop(index)

    def __str__(self):

        to_do_list = ''
        counter = 0

        for item in self.items:

            to_do_list += str(counter)

            if item.is_done == True:
                to_do_list += ' [x] '

            elif item.is_done == False:
                to_do_list += ' [ ] '

            to_do_list += item.name + '\n'

            counter += 1

        return to_do_list


# itemslist = TodoItems()
# itemslist.add_item("pranie1", "dwa")
# itemslist.add_item("pranie2", "trzy", True)
# print(itemslist)
# itemslist.get_item(0).change_name("dupa")
# print(itemslist)