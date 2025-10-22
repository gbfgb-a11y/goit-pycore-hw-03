from datetime import datetime; import random; import re;import sys
from pathlib import Path
from colorama import Fore, Style, init
#Завдання 1
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                #прибираємо пробіли та символи переносу рядка
                line = line.strip()
                if not line:
                    continue  #пропускаємо порожні рядки
                #розділяємо на ім'я та зарплату
                parts = line.split(',')
                if len(parts) != 2:
                    continue  #пропускаємо некоректні рядки
                name, salary_str = parts
                try:
                    salary = int(salary_str)
                except ValueError:
                    continue  #якщо зарплата не число
                total += salary
                count += 1
            if count == 0:
                return 0, 0  #якщо у файлі немає валідних рядків
            average = total / count
            return total, average
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0
#Завданя 2
def get_cats_info(path):
    with open(path, 'r', encoding='utf-8') as f:
        count=0; cats_inf=[]; set_3=[]
        for line in f:
            line=line.strip()
            line=re.sub(r'\\n','',line)
            list_text = line.split(',')
            cats_inf.append({'id':list_text[0],'name':list_text[1], 'age':list_text[2]})
        return cats_inf


#Завданя 3
init(autoreset=True)

def print_dir_tree(path: Path, prefix=""):
    #Рекурсивно печатает структуру директорий.
    #Папки — синим цветом, файлы — зелёным.
    if not path.exists():
        print(Fore.RED + f"Ошибка: путь {path} не существует.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Ошибка: {path} не является директорией.")
        return
    # Получаем список всех элементов в директории
    entries = list(path.iterdir())
    entries_count = len(entries)
    for i, entry in enumerate(entries):
        connector = "┗── " if i == entries_count - 1 else "┣── "
        if entry.is_dir():
            print(prefix + connector + Fore.BLUE + f"{entry.name}/")
            # Рекурсивно печатаем содержимое
            new_prefix = prefix + ("    " if i == entries_count - 1 else "┃   ")
            print_dir_tree(entry, new_prefix)
        else:
            print(prefix + connector + Fore.GREEN + entry.name)
def main():
    # Получаем путь из аргументов командной строки
    if len(sys.argv) < 2:
        print("Использование: python hw03.py <путь_к_директории>")
        sys.exit(1)
    root_path = Path(sys.argv[1])
    print(Fore.MAGENTA + f" {root_path.name}")
    print_dir_tree(root_path)
if __name__ == "__main__":
    main()
# Завданя 4
def command_spliting(user_inp):
    cmd, *args = user_inp.split( )
    cmd = cmd.strip().lower()
    return cmd, args
def adding_inf(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def get_phonenum(name, contacts):
    phone = contacts.get(name)
    if phone:
        return f"{name}: {phone}"
    else:
        return f"No contact named {name}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_inp = input("Enter a command: ")
        command, args = command_spliting(user_inp)
        if command == 'hello':
            print('"How can I help you?"')
        elif command in ['close','exit']:
            print("Good bye!")
            break
        elif command == 'add':
            print(adding_inf(args, contacts))
        elif command == 'phone':
            print(get_phonenum(args[0],contacts))
        elif command == 'all':
            print(contacts)
        else:
            print("Invalid command.")
if __name__ == '__main__':
    main()
