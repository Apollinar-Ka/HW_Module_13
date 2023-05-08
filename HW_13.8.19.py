visitor_count = int(input('Сколько билетов вы хотите приобрести? '))
age_list = [int(input(f'Укажите возраст посетителя № {i}: ')) for i in range(1, visitor_count+1)]
summa = 0
for age in age_list:
    if 18 <= age < 25:
        summa += 990
    elif age >= 25:
        summa += 1390
if visitor_count > 3 and summa > 0:
    print(f"""Полная стоимость заказа: {summa} руб.
СКИДКА 10%
ИТОГО СУММА К ОПЛАТЕ: {int(summa * 0.9)} руб.""")
else:
    print(f'СУММА К ОПЛАТЕ: {int(summa)} руб.')