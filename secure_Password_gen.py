import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

num = int(input('Введите количество паролей которые хотели бы получить:'))
n = int(input('Введите длину предполагаемого пароля:'))
dig = input('Включать ли цифры (0123456789)?')
low = input('Включать ли прописные буквы (abcdefghijklmnopqrstuvwxyz)?')
upp = input('Включать ли заглавные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)?')
sym = input('Включать ли символы (!#$%&*+-=?@^_)?')

if dig == 'Да' or dig == 'да':
    chars += digits
if low == 'Да' or low == 'да':
    chars += lowercase_letters
if upp == 'Да' or upp == 'да':
    chars += uppercase_letters
if sym == 'Да' or sym == 'да':
    chars += punctuation


def sec_pas(dlinа, chars):
    s = []
    for i in range(dlinа):
        s.append(random.choice(chars))
    print(*s, sep='')


for i in range(num):
    sec_pas(n, chars)
