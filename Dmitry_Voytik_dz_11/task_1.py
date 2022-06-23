# 1.Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data:
    def __init__(self, date):
        self.date = str(date)

    def __str__(self):
        return f"Current date is {Data.int_data(self.date)}"

    @classmethod
    def int_data(cls, str_date):
        date_data = []
        for i in str_date.split():
            if i != "-":
                date_data.append(i)
        return int(date_data[0]), int(date_data[1]), int(date_data[2])

# Опустим учет високосных годов для Февраля
    @staticmethod
    def corrected(day, month, year):
        if month == 2:
            if day > 28:
                return f"Wrong day: {day}. In February only 28 days..."
        if 1 <= day <= 31:
            if 0 < month <= 12:
                if 1922 <= year <= 2022:
                    return f"Correct date: {day}-{month}-{year}"
                else:
                    return f"Wrong year: {year}. Years range is from 1990 to 2022"
            else:
                return f"Wrong month: {month}. Months range is from 1 to 12"
        else:
            return f"Wrong day: {day}. Days range is from 1 to 31"


date_today = Data('29 - 12 - 2021')
print('*' * 45)
print(date_today)
print('*' * 45)
print(date_today.corrected(29, 1, 2022))
print(Data.corrected(29, 2, 2021))
