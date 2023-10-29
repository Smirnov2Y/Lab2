salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
debt = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
count = 1

while count <= months:
    money_capital = money_capital - spend + salary
    spend = spend + spend * increase
    count = count + 1

debt = round(money_capital, 2)
print(f"Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", -debt)

