import math
class DoubleTranspCipher:
  def set_pos(self, txt):
    for cif in range(len(txt)):
      first = 'яяя'
      index = 999
      for ind, el in enumerate(txt):
        if len(el) < 2:
          if el < first:
            first = el
            index = ind

      txt[index] = [first, cif]
    return txt

  def check(self, pas1, pas2, text):
    while (len(pas1) * len(pas2)) < len(text):
      print(f'Пароль 2 слишком маленький, нужен другой. Минимум - {math.ceil(len(text) / len(pas1))} символов')
      pas2 = list(input('Пароль 2: ').upper())
    return pas2

  def encrypt(self, pas1, pas2, text):
    tab = []
    pas2= self.check(pas1, pas2, text)
    if (len(pas1) * len(pas2)) > len(text):
      text += ' ' * ((len(pas1) * len(pas2)) - len(text))

    row = []
    for el in list(text):
      row.append(el.upper())
      if len(row) == len(pas1):
        tab.append(row)
        row = []

    pas1 = self.set_pos(pas1)
    pas2 = self.set_pos(pas2)
    sort1 = [c for c in ' ' * len(pas1)]
    sort2 = [c for c in ' ' * len(pas2)]
    for ind, row in enumerate(tab):
      for i, cell in enumerate(row):
        sort1[pas1[i][1]] = cell
      sort2[pas2[ind][1]] = sort1
      sort1 = [c for c in ' ' * len(pas1)]
    sorted_tab = sort2
    return ''.join(''.join(e) for e in sorted_tab)

  def decrypt(self, pas1, pas2, text):
    tab = []
    self.check(pas1, pas2, text)

    row = []
    for el in list(text):
      row.append(el.upper())
      if len(row) == len(pas1):
        tab.append(row)
        row = []

    pas1 = self.set_pos(pas1)
    pas2 = self.set_pos(pas2)

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
    for ind, res in enumerate(sorted_tab):
      if res == ([c for c in ' ' * len(pas1)]):
        sorted_tab = sorted_tab[:ind]
    return ''.join(''.join(e) for e in sorted_tab).capitalize()
