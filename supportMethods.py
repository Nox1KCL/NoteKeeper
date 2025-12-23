import os
import json

# Очищення консолі
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Відкриває файл userNote.json
def open_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            note = json.load(file)
            return note
    except FileNotFoundError:
        note = [{"id": 1, "header": "Hello World!", "text": "Your first Note"}]
        print("File not found, created new one")
        

# Для збереження функції
def save(note, f_name):
    with open(f_name, 'w', encoding='utf-8') as file:
        json.dump(note, file, ensure_ascii=False, indent=4)


# Функція для швидкого запису у файл
def quick_save(file_name, note_header, lines):
    note = open_file(file_name)

    next_id = len(note) + 1
    note_text = "\n".join(lines)
    extra_save = {'id': next_id, 'header': note_header, 'text': note_text}
    note.append(extra_save)

    save(note, file_name)