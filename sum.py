print("Введите сумму заказа")
a = int(input())
waiter = a * 0.18
tax = a * 0.04
print("Сумма вашего заказа: ", a,"\n" "Чаевые официанту: ", waiter,"\n" "Налог: ", tax, sep=" ")