money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0
budget = money_capital
expenses = spend

while budget >= expenses:
    budget = budget - expenses + salary
    expenses = spend + spend * ((count) * increase)
    count = count + 1
else:
    print("Количество месяцев, которое можно протянуть без долгов:", count)


