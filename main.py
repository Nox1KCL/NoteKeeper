from supportMethods import clear_screen
from noteMethods import new_note, delete_note, display_notes, edit_note, open_file, save


# region Main
file_name = "userNotes.json"

while True:
    try:
        notes = open_file(file_name)

        clear_screen()
        print("-" * 23)
        print("\tNotes")
        print("-" * 23)

        while True:
            try:
                user_option = int(input("Choose option"
                                        "\n1 - Take new Note"
                                        "\n2 - Delete Note"
                                        "\n3 - View all notes"
                                        "\n4 - Edit note"
                                        "\n5 - Break"
                                        "\nYour answer: "))
                break
            except ValueError:
                print("Write a digit.\n")
        match user_option:
            case 1:
                new_note(file_name)
            case 2:
                delete_note(file_name)
            case 3:
                display_notes(notes, "all_info")
            case 4:
                edit_note(file_name)
            case 5:
                print("Turning off..")
                break
    except KeyboardInterrupt:
        clear_screen()
        print("Suddenly break.. Turning Off")
    finally:
        notes = open_file(file_name)
        save(notes, file_name)
# endregion