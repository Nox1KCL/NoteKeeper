import json
from supportMethods import clear_screen, open_file, save, quick_save


# Для створення нового елементу(нотатки)
def new_note(file_name):

    clear_screen()
    lines = []
    note_header = ""

    try:
        
        note_header = input("Enter a note header: ")

        print("\nWrite a text:")
        print("(Enter for end)")
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        note_text = "\n".join(lines)

        note = open_file(file_name)
        next_id = len(note) + 1
        new_note = {"id": next_id, "header": note_header, "text": note_text}

        note.append(new_note)

        save(note, file_name)

        clear_screen()
        print("Збережено файл")
        print("Notes: ")

        for item in note:
            print("-" * 23)
            print(f"Header: {item['header']}\nText:\n{item['text']}")
            print("-" * 23)
        input("Please press Enter...")

    except KeyboardInterrupt:
        clear_screen()
        print("Suddenly break.. Turning Off")

        if note_header == "" and lines == []:
            print("Empty note.. deleted")
            input("Press Enter to continue.")
        else:
            print("Detected some not finished note, saving..")
            quick_save(file_name, note_header, lines)
            input("Press Enter to continue..")


# для видалення елементу(Нотатки)
def delete_note(file_name):
    clear_screen()

    note = open_file(file_name)
    showing_notes(note)

    while True:
        try:
            user_choice = int(input("Enter note\'s ID to delete: "))
            current_id = len(note)
            if user_choice < 1 or user_choice > current_id:
                print("ID Error, please enter valid ID")
                continue

            note = [item for item in note if item['id'] != user_choice]
            for index, item in enumerate(note):
                item['id'] = index + 1

            break
        except ValueError:
            print("Enter a digit.\n")

    save(note, file_name)

    print()
    print("Notes: ")
    for item in note:
        print("-" * 23)
        print(f"Header: {item['header']}\nText:\n{item['text']}")
        print("-" * 23)
    input("Please press Enter...")


# Для редагування нотаток
def edit_note(file_name):
    clear_screen()

    note = open_file(file_name)
    showing_notes(note)

    lines = []
    founded_id = 0

    while True:
        try:
            user_choice = int(input("Enter note\'s ID to edit: "))
            note_id = [item['id'] for item in note if user_choice == item['id']]
            if len(note_id) != 1:
                print("Incorrect ID.")
                continue

            founded_id = note_id[0] - 1
            break
        except ValueError:
            print("Enter a digit.\n")
            continue

    new_note_header = input("Write new header(Enter for skip): ").strip()
    print("\nWrite new text:")
    print("(Enter for end (first Enter will leave same text)")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    new_note_text = "\n".join(lines)

    if new_note_header != "":
        note[founded_id]['header'] = new_note_header

    if new_note_text != "":
        note[founded_id]['text'] = new_note_text

    save(note, file_name)
    input("Note edited, Press Enter.")


# Для перегляду вмісту файлу userNotes.json
def view_notes(file_name):
    clear_screen()

    with open(file_name, 'r', encoding='utf-8') as file:
        notes = json.load(file)

    if not notes:
        input("You don't have any note.\nPress enter to Continue..")
        return

    json_notes = json.dumps(notes, ensure_ascii=False, indent=4)
    print("Your notes: ")
    print(json_notes)

    input("Press Enter to continue..")


# Вивід нотаток
def showing_notes(note):
    print("-----------------------")
    for item in note:
        # Тепер користувач бачить лише ID та Header
        print(f"[ID: {item['id']}] Header: {item['header']}")
    print("-----------------------")