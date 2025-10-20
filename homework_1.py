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
        # Перевірка коректності вхідних даних
        if not (isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)):
            return []
        if min < 1 or max > 1000 or min >= max:
            return []
        if quantity < 1 or quantity > (max - min + 1):
            return []
        final_list = random.sample(range(min, max + 1), quantity)
        final_list.sort()
        return final_list
    except ValueError:
        # Якщо дані були введені некоректно
        return []
#Завдання 3
def normalize_phone(phone_number):
    # Видаляємо все зайве: пробіли, дужки, дефіси, символи табуляції та переводу рядка
    cleaned = re.sub(r'[\s\-\(\)\\n\\t]', '', phone_number.strip())
    # Якщо немає + на початку — додаємо
    if not cleaned.startswith('+'):
        cleaned = '+' + cleaned
    # Якщо немає 38 після + — додаємо
    if not cleaned.startswith('+38'):
        # Видаляємо всі нецифрові символи після +
        digits = re.sub(r'\D', '', cleaned)
        # Якщо після + вже є 380..., залишаємо
        if digits.startswith('380'):
            cleaned = '+' + digits
        # Якщо номер починається з 0, додаємо 38 перед ним
        elif digits.startswith('0'):
            cleaned = '+38' + digits
        # Якщо нічого не підходить — повертаємо як є
        else:
            cleaned = '+' + digits
    else:
        # Якщо вже є +38 — просто залишаємо тільки цифри після +
        digits = re.sub(r'\D', '', cleaned)
        cleaned = '+' + digits
    return cleaned
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
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    return upcoming_birthdays
