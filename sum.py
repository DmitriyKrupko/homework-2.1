print("Введите сумму заказа")
a = int(input())
tea = a * 0.15
tax = a * 0.04
print("Сумма вашего заказа: ", a,"\n" "Чаевые официанту: ", tea,"\n" "Налог: ", tax, sep=" ")