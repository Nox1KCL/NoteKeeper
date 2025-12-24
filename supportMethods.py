import os
import json

# Очищення консолі
def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


# Відкриває файл userNote.json
def open_file(f_name: str) -> list:
    try:
        if not os.path.exists(f_name) or os.stat(f_name).st_size == 0:
            raise FileNotFoundError

        with open(f_name, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    except FileNotFoundError:
        print("File not found, created new one")
        return []


# Для збереження функції
def save(notes: list, f_name: str) -> None:
    with open(f_name, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)


# Функція для швидкого запису у файл
def quick_save(f_name: str, note_header: str, lines: list) -> None:
    notes = open_file(f_name)

    next_id = len(notes) + 1
    note_text = "\n".join(lines)
    extra_save = {'id': next_id, 'header': note_header, 'text': note_text}
    notes.append(extra_save)

    save(notes, f_name)