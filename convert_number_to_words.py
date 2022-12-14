def number_to_words(num):
    numbers_0_20 = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать']
    numbers_20_90 = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num <= 20:
        return numbers_0_20[num]
    elif num % 10 == 0:
        return numbers_20_90[num // 10]
    else:
        result = ''.join(numbers_20_90[num // 10]) + ' ' + ''.join(numbers_0_20[num % 10])
        return result
    
# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))