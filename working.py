# from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List, Dict
import bisect
# from player import *

# def hello():
#     return 'Hello'

# print(hello())

# def do_sleep():
#     print('Z-z-z')
    
# def do_eat():
#     print('Eating...')

# def order(action):
#     print('Холоп начал делать действие...')
#     action()
#     print('Холоп закончил...')
    
    
# def sum(a, b):
#     print('Программа начала считать...')
#     print(a + b)
#     print('Программа удачно завершила вычисление')
    # return a + b
    
# do_eat()
# do_sleep()

# order(do_eat)
# order(do_sleep)
    

# action - сходить погулять
# Холоп начал делать действие... сходить погулять
# def sum(4, 5):
#     return a + b
# sum(4, 5)
# do_sleep()
# do_eat()


# def calculate_force(m, a):
#     return  m * a

# F = calculate_force(5, 3)

# print('F = %d' % (m * a))

# def get_distance(x1, y1, x2, y2):
#     return Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)



# def print_100():
#     for i in range(1, 101):
#         print(i)

# print_100()

# 1. del -
        # 2. self.cards -
        # 3. [start:stop]
        #     3.1. start
        #     3.2. stop
        #     3.3. step
        
        # list = [1, 2, 3, 4] - List
        # list[0:2] => [3, 4] - List
        
   
   # list = [1, 2, 3, 4]
   # del list[0]
   #  del list[0:2]

# a = [3, 4, 5, 6, 7, 8] # - колода
# b = [7, 8] # - то что у игрока в руках
# a = [3, 4, 5, 6] # - колода после раздачи
# b = []

# b += a
# print(a)
# print(b)

# array = [1, 2, 3, 4, 5]
# reverse = array[::-1]
# print(reverse)


# array = [1, 25, 32, 43, 100, 105]

# #! range(n) создает массив [0, 1, 2, ..., n - 1]
# #! range работает включительно от нижней границы и НЕ включительно до верхней границы
# # for i in range(len(array) // 2):
# #     array[i], array[-1-i] = array[-1-i], array[i]



# print(array)

#     array[0], array[-1] = array[-1], array[0]
#     array[1], array[-2] = array[-2], array[1]
#     print(array)
    # print(array)


# Artyom [3, 10] -- 13

# array = ['1', '2', '3']

# sum(map(lambda e: int(e), array)) =>
# total = 0
# for elem in array:
#     total += int(elem)


# print(total)


# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]




# array = [input('Введите список: ')]
# value = int(input('Введите значение: '))



# class Person:
#     def __init__(self, name, balance):
#        self.name = name
#        self.balance = balance
    
#     def transfer(self, person, amount):
#         self.balance -= amount
#         person.balance += amount
        
#     # def transfer(self, destination, count):
#     #     self.cards -= self.cards[count:]
#     #     destination.cards += self.cards[count:]
        

# class Policeman(Person):
#     def __init__(self, name, balance, gun):
#         super().__init__(name, balance)
#         self.gun = gun
    
#     def arrest(self, person):
#         person.balance -= 30
        
        

    
# class FBI(Policeman):
#     def __init__(self, name, balance, gun, info):
#         super().__init__(name, balance, gun)
#         self.info = info
        
#     # def arrest(self, person):
#     #     person.balance - 30


# artyom = FBI('Artyom', 1000, 'pistol', 'america')
# igor = Person('Igor', 100)
# artyom.arrest(igor)
# print(igor.balance)

# artyom.transfer(self=artyom, person=igor, amount=250)
# artyom.transfer(person=igor, amount=250)
# print(artyom.balance, igor.balance)



# a = [1, 2, 3, 4, 5, 6]
# b = []

# b += a[-2:]

# # print(a)
# print(b)

# #TODO: Призыв в армию
# # 1. Зрение (не берут, если зрение -6.25 и меньше)  -> float
# 2. Плоскостопие (есть - не берут) -> bool
# 3. Ожирение (вес более 135 кг) -> float

# def check_army(vision, flat_feet, obesity, psy, disabled):
#     return vision > -6.25 and not flat_feet and \
#         obesity < 135 and not psy and not disabled

# vision = float(input('Какое у тебя зрение? '))
# flat_feet = input('У тебя есть плоскостопия? (y/n): ')
# obesity = float(input('Сколько вы весите? '))
# psy = input('Ты псих? (y/n): ')
# disabled = input('Ты инвалид? (y/n): ')


# if check_army(vision, flat_feet == 'y', obesity, psy == 'y', disabled == 'y'):
#     print('Мы берем вас в армию')
# else:
#     print('Мы не берем вас в армию')
    
    
# def foo(array=[]):
#     array.append(1)
#     print(array)
    
# mas = [4, 4, 5]
# foo(mas)
# foo()
# foo()

# def foo(array=None):
#     if array is None:
#         array = []
#     array.append(1)
#     print(array)

# foo([4, 4, 5])

# foo()
# foo()
# foo()

# def foo(a, b, c=4, d=5):
#     print(a, b, c, d)


# foo(1, 2)

#                     a   b   c   d
# foo(1, 2) =>        1   2   4   5
# foo(1, 2, 6) =>     1   2   6   5
# foo(1, 2, 6, 7) =>  1   2   6   7


# def new_player(name, cards=[]):
#     return cards
    
# art = new_player('artyom')
# ig = new_player('igor')

# art.append(1)
# art.append(2)

# ig.append(3)
# ig.append(4)

# print('Карты Артема: ', art)
# print('Карты Игоря: ', ig)

# def new_player(name, cards=None):
#     if cards is None:
#         cards = []
#     return cards
    
# art = new_player('artyom')
# ig = new_player('igor')

# art.append(1)
# art.append(2)

# ig.append(3)
# ig.append(4)

# print('Карты Артема: ', art)
# print('Карты Игоря: ', ig)


# class Observer(ABC):
#     """
#     Интерфейс Наблюдателя объявляет метод уведомления, который издатели
#     используют для оповещения своих подписчиков.
#     """

#     @abstractmethod
#     def update(self, subject: str, data: any) -> None:
#         """
#         Получить обновление от субъекта.
#         """
#         pass


# class Publisher:
#     """
#     Интерфейс издателя объявляет набор методов для управлениями подписчиками.
#     """

#     @abstractmethod
#     def attach(self, subject: str, observer: Observer) -> None:
#         """
#         Присоединяет наблюдателя к издателю.
#         """
#         pass

#     @abstractmethod
#     def detach(self, observer: Observer, subject: str) -> None:
#         """
#         Отсоединяет наблюдателя от издателя.
#         """
#         pass

#     @abstractmethod
#     def notify(self, subject: str, data: any) -> None:
#         """
#         Уведомляет всех наблюдателей о событии.
#         """
#         pass


# class University(Publisher):
#     # {
#     #     'graduation': [mother, military, student],
#     #     'closed': [student],   
#     # }
    
#     _observers: Dict[str, List[Observer]] = {}
    
#     def attach(self, subject: str, observer: Observer) -> None:
#         if subject not in self._observers:
#             self._observers[subject] = []
#         self._observers[subject].append(observer)

#     def detach(self, observer: Observer, subject: str) -> None:
#         self._observers[subject].remove(observer)

#     def notify(self, subject: str, data: any) -> None:
#        for observer in self._observers[subject]:
#            observer.update(subject, data)


# class Mother(Observer):
#     def update(self, subject: str, data: any):
#         if data == 5:
#             print('Я куплю тебе машину')
#         elif data == 4:
#             print('Куплю тебе новый айфон')
#         else:
#             print('Будешь убирать говно!')


# class Military(Observer):
#     def update(self, subject: str, data: any):
#         if subject == 'graduation':
#             print('Иди в армию!')
        

# class Student(Observer):
#     def update(self, subject: str, data: any):
#         if data == 5:
#             print('У меня будет новая машина')
#         elif data == 4:
#             print('Мне купят новый айфон')
#         else:
#             print('Мне пизда!')
        



# # ....

# harvard = University()

# mother = Mother()
# harvard.attach('graduation', mother)

# military = Military()
# harvard.attach('graduation', military)

# student = Student()
# harvard.attach('graduation', student)

# import time

# # Waiting for 4 years
# time.sleep(4)

# harvard.notify('graduation', 5)

# rejects = {}

# def reject(player):
#     for player in players:
#         # if player == 'n':
#         rejects[str(player.cards)] = 'reject' 


# artyom = Player('artyom')
# igor = Player('igor')
# players = [artyom, igor]
# for player in players:
#     take_card = input("%s's Хотите взять еще одну карту? (y/n) " % player.name)

# reject(player)


# print(rejects)


# def benchmark(func):
#     import time
    
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end-start))
#         return return_value
#     return wrapper

# # @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text

# benchmark

# def ready(func):
#     print('Игрок готов взять карту')
#     def wrapper():
#         func()
#     return wrapper

# def take_card():
#     print('Карта взята')
    
# # take_card()
# ready(take_card(t(h())))

# @ready
# def take_card():
#     print('Карта взята')

# take_card()

# ready(take_card)

# turn = 2

# players = [1, 2, 3, 4, 5]


# for index in range(len(players)):
#     if turn == index:
#         print(index)
#     else:
#         print('Ошибка')
    
# array = [1, 2, 3, 4]

# for i in range(len(array)): #= 0, 1, 2, 3:
#     print(array[i])
    
# turn == array[]
# print(array[turn])

# def maxProfit(prices: List[int]) -> int:
#     buy = prices[0]
#     for price in prices:
#         if price < buy:
#             buy = price
#         elif price > buy:
#             max_profit = max(price - buy, max_profit)
#         else:
#             max_profit = 0
#     return max_profit
    


# prices = [7,6,4,3,1]

# profit = maxProfit(prices)

# print(profit)

# a=[52, 25, 23, 41, 32] # smallest number 
# smallest = a[0] if a else None 
# for i in a: 
#     if i > smallest: 
#         smallest=i

# for i in range(5):
#   if i % 2 == 0:
#     continue
#   print(i)

# arr = {1, 2, 3}
# players = {Player('Artyom'), Player('Igor' )}
# CardWeight.get_weight_cards(p.cards)
# set(pp)


# aaa = [1, 2, 3 , 4]

# multip = list(map(lambda x: x * 2, aaa))

# print(multip)

# sp = [1]

# if [i for i in sp if i != sp[0]] == []:
#     print("ОДИНАКОВЫЕ!!!")
# else:
#     print('НЕОДИНАКОВЫ')


# def searchInsert(nums: List[int], target: int) -> int:
#     if target in nums:
#         return nums.index(target)
#     bisect.insort(nums, target)
#     return nums.index(target)

# def searchInsert(nums: List[int], target: int) -> int:
#     if not target in nums:
#         bisect.insort(nums, target)
#     return nums.index(target)

# nums = [1, 3, 5, 6]
# aa = searchInsert(nums, 8)
# print(aa)


# def removeElement(nums: List[int], val: int) -> int:
#     for i in range(len(nums)):
#         if val in nums:
#             nums.remove(val)
#     return len(nums)

# nums = [3, 2, 2, 3]
# delete = removeElement(nums, 3)
# print(delete)

# def removeDuplicates(nums: List[int]) -> int:
#     return list(set(nums))
    
# nums = [1,1,2]
# duplicate = removeDuplicates(nums)
# print(duplicate)



# digits = [1,9,9,9]  digits[-1] = [9,9,9,1]
# len(digits) - 1

# дИджит

# 9440 => 0440
# 1) Проходя цикл из конца, находя цифру   9 -- 0   
# 2) Перед индексом 

# 4899 => 4890
# 1) Прибавляем единицу к последней цифре, если она не 9
#     если 9, то заменяем её на 0 и установить флаг переноса
    
# 1234 + 1 =  5
# 9949 => 9950
# 9999 -- 0000

# [9] => [0]
# [0] => [1]
# [9, 9, 9, 9] => [0, 0, 0, 0]
# [8, 9, 9, 9] = [9, 0, 0, 0]

# def plusOne(digits: List[int]) -> List[int]:
#     for i in range(len(digits)-1, 0-1, -1):
#         if digits[i] == 9:
#             digits[i] = 0
#         else:
#             digits[i] += 1
#             break
#     if digits[0] == 0:
#         # digits = [1] + digits
#         digits.insert(0, 1)
#     return digits

# digits = [1, 0, 0, 0, 0]
# plus_one = plusOne(digits)
# print(plus_one)





# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     while True:
#         if len(nums1) == m:
#             break
#         nums1.pop()
    
#     while True:
#         if len(nums2) == n:
#             break    
#         nums2.pop()

#     nums1.extend(nums2)
#     nums1.sort()


# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# aa = merge(nums1, 3, nums2, 3)
# print(aa)

# def removeDuplicates(nums: List[int]) -> int:
#         return set(nums)


# nums = [1,1,2]
# aa = removeDuplicates(nums)
# print(aa)

# a = [1,9,9]
# for i in range(len(a)-1, 0-1, -1):
#     print(a[i])

# def maxProfit(prices: List[int]) -> int:
#     buy = prices[0]
#     max_profit = 0
#     for price in prices:
#         if price < buy:
#             buy = price
#         elif price > buy:
#             max_profit = max(price - buy, max_profit)
#     return max_profit


# prices = [7,1,5,3,6,4]
# aa = maxProfit(prices)
# print(aa)

# def summator(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i]
#     return sum

# arr = [5, 3, 0, 0, -5, 3]
# print(summator(arr))

# open_list = ["[","{","("]
# close_list = ["]","}",")"]
  
# # Function to check parentheses
# def check(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack) - 1])):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#     if len(stack) == 0:
#         return "Balanced"
#     else:
#         return "Unbalanced"
  
# Driver code
string = "{[]{()}}" 
print(string,"-", check(string))
  
string = "[{}{})(]"
print(string,"-", check(string))
  
string = "((()"
print(string,"-",check(string))

string = "((([])))"
print(string,"-",check(string))

# import math

# def is_prime(n): 
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# def print_primes(n):
#     for num in range(2, n):
#         if is_prime(num):
#             print(num)

# n = int(input())
# print_primes(n)

# def reverseList(A, start, end):
#     while start <= end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1
# # Driver function to test above function
# A = [1, 2, 3, 4, 7]
# print(A)
# reverseList(A, 0, len(A)-1) 
# print("Reversed list is")
# print(A)