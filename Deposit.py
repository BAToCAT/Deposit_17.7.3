per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = input('money = ')

deposit = []

deposit.append(int(per_cent.get('ТКБ') * int(money)/100))

deposit.append(int(per_cent.get('СКБ') * int(money)/100))

deposit.append(int(per_cent.get('ВТБ') * int(money)/100))

deposit.append(int(per_cent.get('СБЕР') * int(money)/100))

print('deposit =', deposit)

print('Максимальная сумма, которую вы можете заработать —', int(max(deposit)))
