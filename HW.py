per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#per_cent = "," .join(per_cent)
deposit = []
money = int(input("Введите сумму: "))
for key in per_cent:
    deposit.append(per_cent[key] * money * 0.01)
print(deposit)
max_deposit = max(deposit)
print("Наибольший процент за год: ", max_deposit)