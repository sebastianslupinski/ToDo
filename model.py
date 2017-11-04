class TodoItem():

    id = 0

    def __init__(self, name, description, is_done=False):

        self.name = name
        self.description = description
        self.is_done = is_done
        self.id = TodoItem.id
        TodoItem.id += 1
        

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

    def __str__(self):

        to_do_list = ''

        for item in items:

            to_do_list += item.__str__() + '\n'

        return to_do_list


# item1 = TodoItem("pranie", "dzisiaj o 5 pranie", False)
# print(item1)