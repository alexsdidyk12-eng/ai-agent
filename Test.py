# 🟢 ЧАСТЬ 1. Условия + циклы

## 1️⃣ Таблица умножения

# Пользователь вводит число.
# Выведи таблицу умножения от 1 до 10.

# Пример для 3:
#chislo=int(input("vvedite chislo"))
#for i in range(1,11):
#   print(f"{chislo}*{i}={chislo * i}")
    
    
#text id="of0qgm"
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30

# ---

# ## 2️⃣ Найди все четные числа

# Выведи все четные числа от 1 до 100.
#for i in range(1,101):
# if i %2==0:
  #   print(i)
# ---

# ## 3️⃣ Пароль

# Пользователь должен ввести пароль.

# Пока пароль не равен:
#pas=int(input("vvedite parol"))
#while True:
  #  if pas=="python123":
   #     print("vu uspeshno voshli")
    #    break
  #  else:
    #    print("dostup zaprechen")
# python id="20zz9l"
# python123

# программа просит снова.

# После правильного ввода:

# Доступ открыт

# ---

# # 🟡 ЧАСТЬ 2. Строки

# ## 4️⃣ Подсчёт букв

# Пользователь вводит текст.
# Посчитай сколько там:

# * букв a
# * букв o
#summa=0
#text=int(input("vvedite text"))
#if text "a":
 #   summa=summa+1
#print(summa)
# ---

# ## 5️⃣ Переворот строки

# Ввод:

# text id="d6f7w5"
# python
#vvod=input("vvedite slovo")
#print(vvod[::-1])


# Вывод:

# text id="okq2lu"
# nohtyp

# ---

# ## 6️⃣ Проверка палиндрома

# Проверить, является ли слово палиндромом.

# Примеры:

# text id="vhq79r"
# level → True
# anna → True
# python → False
#text=input("vvedite slovo")
#if text[::-1]==text:
 # print("true")
#else:
 # print("False")
# ---

# # 🟠 ЧАСТЬ 3. Списки

# ## 7️⃣ Найти максимум

# Дан список:

#python id="1p1b5m"
#numbers = [5, 2, 9, 1, 7]

#maxx=numbers[0]
#for n in numbers:
  #if n > maxx:
  #  maxx=n
#print(maxx)
  

# Найти максимальное число без max().

# ---

# ## 8️⃣ Удалить дубликаты

# Дан список:

# python id="ml0i3q"
#text=[1, 2, 2, 3, 4, 4, 5]
#newlist=[]
#for n in text:
 # if  n not in newlist:
  #  newlist.append(n)
#print(newlist)

# Сделать новый список без повторений.

# ---

# ## 9️⃣ Среднее значение

# Найти среднее число списка.
#text=[1, 2, 2, 3, 4, 4, 5]
#summa=0
#for n in text:
#  summa=summa+n
#f=len(text)
#s=summa/f
#print(s)
  
# ---

# # 🔵 ЧАСТЬ 4. Функции

# ## 🔟 Калькулятор

# Создай функцию:

# python id="xk6yv2"
#def calc():
  #a=int(input("vvedite chislo 1: "))
 # b=int(input("vvedite chislo 2: "))
  #operation=input("vvedite operaciu: ")
 # if operation=="+":
  #  print(a+b)
  #if operation=="-":
  #  print(a-b)
 # if operation=="/":
 #   print(a/b)
 # if operation=="*":
 #   print(a*b)
#calc()

# Примеры:

# python id="8w14a8"
# calc(2, 3, "+") → 5
# calc(10, 2, "/") → 5

# ---

# ## 1️⃣1️⃣ Проверка email

# Функция получает строку.
#def stroka(text):
 # for n in text:
   # if "@" in n or "." in n:
    #  print("True")
   # else:
   #   print("False")
#stroka("privet.")
  
# Если есть:

# * @
# * .

# то вернуть True, иначе False.

# ---

# ## 1️⃣2️⃣ Генератор пароля

# Функция получает длину пароля и создаёт случайный пароль.

#def parol(dlina):
 # for n in dlina:
   # if dlina==1:
     # n=="p"
     # print(n)
   # elif dlina==2:
    #  n=="py"
   #   print(n)
   # elif dlina==3:
   #   n=="pyt"
   #   print(n)
   # elif dlina==4:
   #   n=="pyth"
   #   print(n)
   # elif dlina==5:
   #   n=="pytho"
   #   print(n)
   # elif dlina==6:
   #   n=="python"
   #   print(n)
      
#parol(4)


    
    
# ---

# # 🟣 ЧАСТЬ 5. Словари (очень важно)

# ## 1️⃣3️⃣ Телефонная книга

# Создай словарь:

# python id="6e2o04"
#n=input("vvedite imia")
#contacts = {
   #  "Max": "123",
   # "Anna": "555"
 #}
#if n=="Anna":
#   print(555)
#if n=="Max":
#  print(123)
#else:
#  print("ne naideno takpe imia")
# Пользователь вводит имя → вывести номер.

# ---

# ## 1️⃣4️⃣ Подсчёт слов

# Текст:

# text id="dh9jri"
#text="python is good and python is easy"
#words=text.split()
#count={}
#for word in words:
#  count[word]=count.get(word,0)+1
#print(count)

# Посчитать сколько раз встречается каждое слово.

# ---

# # 🔴 ЧАСТЬ 6. Mini Agent Logic

# ## 1️⃣5️⃣ Текстовый помощник

# Сделай программу:

# Команды:

# * time → текущее время
# * hello → привет
# * calc → попросить 2 числа
# * exit → выход

# ---

# ## 1️⃣6️⃣ Expense Mini Bot

# Команды:

# * add 200 food
# * show
# * total

# Храни расходы в списке.

# Пример:

# python id="9g67r1"
# [
#     {"amount": 200, "category": "food"},
#     {"amount": 100, "category": "taxi"}
# ]

# ---

# # ⚫️ ЧАСТЬ 7. Для сильных

# ## 1️⃣7️⃣ Сортировка вручную

# Отсортируй список чисел по возрастанию без sort().
#nums=[9,99,555,66666,21,24]
#n=len(nums)
#for i in range(n):
#  for j in range(0,n-i-1):
#    if nums[j]>nums[j+1]:
#      nums[j],nums[j+1]=nums[j+1],nums[j]
#print(nums)
# ---

# ## 1️⃣8️⃣ Угадай число

# Компьютер загадывает число от 1 до 100.
# Пользователь угадывает.
#computer=24
#while True:
 #n=int(input("ugadai chislo"))
 #if n<24:
 #  print("bolche")
# elif n>24:
#   print("menshe")
# else:
 #  print("ugadal")
 #  break

# Подсказки:

# * больше
# * меньше

# ---

# ## 1️⃣9️⃣ Анализ текста

# Введи текст и выведи:

# * количество слов
# * количество букв
# * самое длинное слово'
