def set_pos(txt):
    for cif in range(len(txt)):
        first = 'яяя'
        index = 999
        for ind, el in enumerate(txt):
            if len(el) < 2:
                if el < first:
                    first = el
                    index = ind

        txt[index] = [first, cif]


def encrypt(pas1, pas2, text):
    tab = []

    row = []
    text += ' ' * (len(pas1) - (len(text) % len(pas1)))
    for el in list(text):
        # if el == ' ':
        #     continue

        row.append(el.upper())
        if len(row) == len(pas1):
            tab.append(row)
            row = []

    while len(tab) > len(pas2):
        print(f'Пароль 2 слишком маленький, нужен другой. Минимум - {len(tab)} символов')
        pas2 = list(input('Пароль 2: ').upper())

    set_pos(pas1)
    set_pos(pas2)

    sort1 = [c for c in ' ' * len(pas1)]
    sort2 = [c for c in ' ' * len(pas2)]
    for ind, row in enumerate(tab):
        for i, cell in enumerate(row):
            sort1[pas1[i][1]] = cell

        sort2[pas2[ind][1]] = sort1
        sort1 = [c for c in ' ' * len(pas1)]

    sorted_tab = sort2
    return ''.join(''.join(e) for e in sorted_tab)


def decrypt(pas1, pas2, text):
    tab = []

    row = []
    for el in list(text):
        # if el == ' ':
        #     continue
        row.append(el.upper())

        if len(row) == len(pas1):
            tab.append(row)
            row = []

    while len(tab) > len(pas2):
        print(f'Пароль 2 слишком маленький, нужен другой. Минимум - {len(tab)} символов')
        pas2 = list(input('Пароль 2: ').upper())

    set_pos(pas1)
    set_pos(pas2)

    row_adr = [c for c in ' ' * len(pas1)]
    for i, num in enumerate(pas1):
        row_adr[num[1]] = str(i)

    tab_adr = [c for c in ' ' * len(pas2)]
    for i, num in enumerate(pas2):
        tab_adr[num[1]] = str(i)

    sort1 = [c for c in ' ' * len(pas1)]
    sort2 = [c for c in ' ' * len(pas2)]
    for ind, row in enumerate(tab):
        for i, cell in enumerate(row):
            sort1[int(row_adr[i])] = cell

        sort2[int(tab_adr[ind])] = sort1
        sort1 = [c for c in ' ' * len(pas1)]

    sorted_tab = sort2
    return ''.join(''.join(e) for e in sorted_tab).capitalize()


choose = input('Выберите:\n1) Зашифровать\n2) Расшифровать\nВаш ответ: ')
while choose != '1' and choose != '2':
    choose = input('Ошибка! Выберите:\n1) Зашифровать\n2) Расшифровать\nВаш ответ: ')

first_pas = list('1324572634'.upper())  # input('Пароль 1: ')
second_pas = list('abcefrbdayruin'.upper())  # input('Пароль 2: ')

info = 'ЯВЛ БАИСЮ ВСЛАШ ЕБЬОЛ О:ЬЛ ЮВБОС ВОЕ МН;ЕЁЫЩЬ,  ТБПСОУАТ ЬН МЖ О ЕДТВ,УЕЕШ  УМЙОТ  ЬИВЧАНСЕ. М      ГСНА ЛСАЕ И;НТ  ХЯЕ ОУЧЧЛ ИПАЕ ЕЕНО ЖТВР'  # input('Ваш текст: ')


if choose == '1':
    result = encrypt(first_pas, second_pas, info)
else:
    result = decrypt(first_pas, second_pas, info)

print(result)

ask = 0
while ask != 'ДА' and ask != 'НЕТ':
    ask = input('Сохранить результат в файл?(Да или Нет): ').upper()

if ask == 'ДА':
    f = open('out.txt', 'w')
    f.write(result)

# Я помню чудное мгновенье: Передо мной явилась ты, Как мимолетное веденье, Как гений чистой красоты.
# У лукоморья дуб зелёный; Златая цепь на дубе том: И днём и ночью кот учёный Всё ходит по цепи кругом;
# Скажи-ка, дядя, ведь не даром Москва, спаленная пожаром, Французу отдана?
# Я вас любил: любовь ещё, быть может, В душе моей угасла не совсем; Но пусть она вас больше не тревожит; Я не хочу печалить вас ничем.
# Жди меня, и я вернусь. Только очень жди, Жди, когда наводят грусть Желтые дожди
# Я пришел к тебе с приветом, Рассказать, что солнце встало, Что оно горячим светом По листам затрепетало;
