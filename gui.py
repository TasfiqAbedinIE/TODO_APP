import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("BlueMono")

label = sg.Text("Type in a TODO")
current_time = sg.Text(key="clock")
input_box = sg.InputText(tooltip="Enter TODO", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My TODO",
                   layout=[[label, current_time],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],

                   font=("Calibri", 12))

while True:
    event, values = window.read(timeout=200)
    now = time.strftime("%b %d, %Y %H:%M:%S")
    window["clock"].update(now)
    print(event, values)

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)

        window["todos"].update(values=todos)
        window["todo"].update(value="")

    elif event == "Edit":
        try:
            todo_to_edit= values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            window["todos"].update(values=todos)
        except IndexError:
            sg.popup("Please select any TODO", font=("calibri", 14), title="Warning")

    elif event == "Complete":
        try:
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)

            functions.write_todos(todos)

            window["todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("Please select any TODO", font=("calibri", 14), title="Warning")

    elif event == "Exit":
        break

    elif event == "todos":
        window["todo"].update(value=values["todos"][0])

    elif event == sg.WIN_CLOSED:
        break

window.close()

# ================== BONUS EXAMPLE - LECTURE - 154 ====================== #

# import PySimpleGUI as sg
# import zipfile, pathlib
#
# label1 = sg.Text("Select Files to compress.")
# input1 = sg.Input()
# choose_button1 = sg.FilesBrowse("Choose", key="file")
#
# label2 = sg.Text("Select destination folder.")
# input2 = sg.Input()
# choose_button2 = sg.FolderBrowse("Choose", key="folder")
#
# compress_button = sg.Button("Compress")
# output_lebel = sg.Text(key="output")
#
# window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1], [label2, input2, choose_button2], [compress_button, output_lebel]])
#
# def make_archive(filepath, destination):
#     with zipfile.ZipFile(pathlib.Path(destination, "compressed.zip"), "w") as archive:
#         for filepath in filepath:
#             filepath = pathlib.Path(filepath)
#             archive.write(filepath, arcname=filepath.name)
#
#
#
# while True:
#     event, values = window.read()
#     print(event, values)
#     filepath = values["file"].split(";")
#     folder = values["folder"]
#     make_archive(filepath, folder)
#     window["output"].update(value="compression completed")
#
# window.close()
