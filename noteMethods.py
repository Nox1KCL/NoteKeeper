from supportMethods import clear_screen, open_file, save, quick_save


# Для створення нового елементу(нотатки)
def new_note(f_name: str) -> None:

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

        notes = open_file(f_name)
        next_id = len(notes) + 1
        new_note = {"id": next_id, "header": note_header, "text": note_text}

        notes.append(new_note)

        save(notes, f_name)

        clear_screen()
        print("Збережено файл")
        
        display_notes(notes, "info_without_id")


    except KeyboardInterrupt:
        clear_screen()
        print("Suddenly break.. Turning Off")

        if note_header == "" and lines == []:
            print("Empty note.. deleted")
            input("Press Enter to continue.")
        else:
            print("Detected some not finished note, saving..")
            quick_save(f_name, note_header, lines)
            input("Press Enter to continue..")


# для видалення елементу(Нотатки)
def delete_note(f_name: str) -> None:
    clear_screen()

    notes = open_file(f_name)
    display_notes(notes, "info_without_text")

    while True:
        try:
            user_choice = int(input("Enter note\'s ID to delete: "))
            current_id = len(notes)
            if user_choice < 1 or user_choice > current_id:
                print("ID Error, please enter valid ID")
                continue

            notes = [item for item in notes if item['id'] != user_choice] # type: ignore
            for index, item in enumerate(notes):
                item['id'] = index + 1

            break
        except ValueError:
            print("Enter a digit.\n")

    save(notes, f_name)
    display_notes(notes, "info_without_id")


# Для редагування нотаток
def edit_note(f_name: str) -> None:
    clear_screen()

    notes = open_file(f_name)
    display_notes(notes, "info_without_id")

    lines = []
    founded_id = 0

    while True:
        try:
            user_choice = int(input("Enter note\'s ID to edit: "))
            note_id = [item['id'] for item in notes if user_choice == item['id']]
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
        notes[founded_id]['header'] = new_note_header

    if new_note_text != "":
        notes[founded_id]['text'] = new_note_text

    save(notes, f_name)
    input("Note edited, Press Enter.")


# Видображує нотатки в різному вигляді
def display_notes(notes: list, view_mode: str) -> None:
    clear_screen()

    if not notes:
        input("You don't have any note.\nPress enter to Continue..")
        return
    
    if not view_mode:
        input("View mode error.")
        return
    

    prettier_notes = []
    pretty_sep = "- " * 10
    print("Your notes: ")
    print("-" * 20)
    
    if view_mode == "all_info":
        for item in notes:
            block = f"[ID: {item['id']}]\nHeader: {item['header']}\nText:\n{item['text']}"
            prettier_notes.append(block)
        print(f"\n{pretty_sep}\n".join(prettier_notes))
            

    elif view_mode == "info_without_id":
        for item in notes:
            block = f"Header: {item['header']}\nText:\n{item['text']}"
            prettier_notes.append(block)
        print(f"\n{pretty_sep}\n".join(prettier_notes))

    elif view_mode == "info_without_text":
        for item in notes:
            print(f"[ID: {item['id']}] Header: {item['header']}")
    
    else:
        print("Unknown view mode..")

    print("-" * 20)
    input("Press Enter to continue..")