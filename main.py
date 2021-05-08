import config
from shifr import DoubleTranspCipher


def main():
  choose = input('Выберите:\n1) Зашифровать\n2) Расшифровать\nВаш ответ: ')
  while choose != '1' and choose != '2':
    choose = input('Ошибка! Выберите:\n1) Зашифровать\n2) Расшифровать\nВаш ответ: ')

  first_pas = list(config.FIRST_PASSWORD.upper())  # input('Пароль 1: ')
  second_pas = list(config.SECOND_PASSWORD.upper())  # input('Пароль 2: ')
  info = config.TEXT  # input('Ваш текст: ')

  cipher = DoubleTranspCipher()
  if choose == '1':
    result = cipher.encrypt(first_pas, second_pas, info)
  else:
    result = cipher.decrypt(first_pas, second_pas, info)

  print(result)

  ask = 0
  while ask != 'ДА' and ask != 'НЕТ':
    ask = input('Сохранить результат в файл?(Да или Нет): ').upper()

  if ask == 'ДА':
    f = open('out.txt', 'w')
    f.write(result)


if __name__ == '__main__':
  main()
