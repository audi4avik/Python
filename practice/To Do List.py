"""
Create a To Do List. Continue to prompt for new item unless user enters a blank. Display the final To Do List.
"""
todolist = []
new_item = "cat"
while new_item != "":
    new_item = input("Enter items for To Do List: ")
    todolist.append(new_item)
    print("item added")
print(todolist[0:-1])