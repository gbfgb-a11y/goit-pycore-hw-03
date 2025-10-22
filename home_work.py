from datetime import datetime; import random; import re
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
        print(cats_inf)
        #return cats_inf


#cats_info = get_cats_info(r"C:\Users\denke\Desktop\SOMETHING\tests.txt")
#print(cats_info)
get_cats_info(r"C:\Users\denke\Desktop\SOMETHING\tests.txt")