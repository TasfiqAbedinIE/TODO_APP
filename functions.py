FILEPATH = "todos.txt"

def get_todos(file_path = FILEPATH):
    """Collect lists from the text file"""
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path = FILEPATH):
    """write new lines into text file"""
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)

# To avoid something to import to other file when importing
# print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())

# ==================== BONUS EXAMPLE - LECTURE 118 ====================== #

# def parse(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     return {"feet": feet, "inches":inches}
#
# def convert(feet, inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters