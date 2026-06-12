from datetime import datetime, date

# -------- 1. Ввод данных --------
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))

birth_date = date(year, month, day)

# -------- 2. День недели --------
def get_weekday(birth_date):
    return birth_date.strftime("%A")  # Monday, Tuesday...

# -------- 3. Проверка високосного года --------
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# -------- 4. Возраст --------
def get_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year

    # если день рождения ещё не был в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

# -------- 5. "Электронное табло" --------
digits = {
    "0": [" * ", "*   ", "   ", "   ", " ** "],
    "1": ["  *  ", " *  ", "  *  ", "  *  ", "**"],
    "2": [" * ", "*   ", "   * ", "  *  ", "**"],
    "3": [" * ", "    ", "  * ", "    ", " ** "],
    "4": ["*   ", "   ", "**", "    *", "    *"],
    "5": ["**", "    ", "** ", "    ", "* "],
    "6": [" * ", "*    ", "** ", "*   ", " ** "],
    "7": ["***", "    *",   "   * ", "  *  ", "  *  "],
    "8": [" * ", "*   ", " ** ", "*   ", " ** "],
    "9": [" *", "   ", " **", "    *", " ** "],
}

def print_big_date(day, month, year):
    s = f"{day:02d}{month:02d}{year}"
    for i in range(5):
        line = ""
        for ch in s:
            line += digits[ch][i] + "  "
        print(line)

# -------- Вывод --------
print("\n--- РЕЗУЛЬТАТ ---")
print("Дата рождения:", birth_date)
print("День недели:", get_weekday(birth_date))

print("Високосный год:", "Да" if is_leap_year(year) else "Нет")

print("Возраст:", get_age(birth_date))

print("\nДата в виде табло:")
print_big_date(day, month, year)
