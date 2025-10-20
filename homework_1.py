from datetime import datetime; import random; import re
#Завдання 1
def get_days_from_today(date):
    try:
    #Обробка дати та віднімання одна від одної
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - given_date
        return delta.days
    except ValueError:
        # Якщо формат дати неправильний, виводимо повідомлення
        print("Помилка: неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'.")
        return None

#Завдання 2
def get_numbers_ticket(min, max, quantity):
    try:
        final_list=[]
        for i in range(quantity+1):
            number = random.randint(min,max)
            if number not in final_list:
                final_list.extend({number})
        return final_list
    except ValueError:
    # Якщо дані були введені не коректно
        return 'Something went wrong. Try again using criteria -> min, max, quanity.'

#Завдання 3
def normalize_phone(phone_number):
    # Видаляємо усе не потрібне
    normalize_phone_1 = re.sub(r'[ -()]', '', phone_number); ab=None # АБ це такий собі буфер.
    # Добавляємо + якщо треба
    if normalize_phone_1[0] != '+':
        normalize_phone_1 = '+'+normalize_phone_1
    # Добавляємо 38 якщо треба
    if normalize_phone_1[1] != '3':
        ab = re.split(r'(.)(050\d*)',normalize_phone_1)
        normalize_phone_1 = ab[1]+'38'+ab[2]
    return normalize_phone_1
#Завдання 4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо день народження зі строки у дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Змінюємо рік на поточний
        birthday_this_year = birthday.replace(year=today.year)
        # Якщо день народження вже минув переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        # Різниця в днях
        delta_days = (birthday_this_year - today).days
        # Якщо день народження протягом наступних 7 днів
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year
            # Якщо день народження припадає на вихідний переносимо на понеділок
            if congratulation_date.weekday() == 5:      # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # неділя
                congratulation_date += timedelta(days=1)

            # Додаємо результат до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
