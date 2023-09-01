# todos = []
# importing modules
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now} & have a good day!")

while True:
    user_action = input("What do you want to do (add, show, edit, exit): ").lower().strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        ### With function
        todos = get_todos()

        todos.append(todo)

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        ### With context manager
        # with open('todos.txt', 'w') as file:
        #     file.writelines(todos)

        ###With function
        write_todos(todos)

    elif user_action.startswith('show'):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        ### With function
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1} - {item}')


    elif user_action.startswith('edit'):
        try:
            edit_num = int(user_action[5:])
            edit_num = edit_num - 1

            ### With function
            todos = get_todos()

            new_todo = input("Enter new TODO: ") + "\n"
            todos[edit_num] = new_todo

            write_todos(todos, "todos.txt")

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            complete = int(user_action[9:])

            ### With function
            todos = get_todos()

            todo_to_remove = todos[complete - 1].strip('\n')
            todos.pop(complete - 1)

            write_todos(todos)

            print(f'Todo {todo_to_remove} was removed from the list')
        except IndexError and ValueError:
            print('Your item does not exist')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid.")






# ======================= TODO APP - COMPLETE ========================= #


################# BONUS EXAMPLE - LECTURE 109 ##################

# def get_average ():
#     with open("data.txt", 'r') as file:
#         data = file.readlines()
#     values = data[1:]
#     values = [float(i) for i in values]
#
#     average = sum(values) / len(values)
#     return average
#
# average = get_average()
# print(average)

################# BONUS EXAMPLE - LECTURE 118 ###################

# from functions import parse, convert
#
# feet_inches = input("Enter feet and inches: ")
#
#
# parsed = parse(feet_inches)
# result = convert(parsed['feet'], parsed['inches'])
#
# print(f"{parsed['feet']} feet and {parsed['inches']} inches = {result} meters")
#
# if result < 1:
#     print("The kid can not use this ride.")
# else:
#     print("The kid can use the ride.")
