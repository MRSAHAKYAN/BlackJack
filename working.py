
def hello():
    return 'Hello'

print(hello())

def do_sleep():
    print('Z-z-z')
    
def do_eat():
    print('Eating...')

def order(action):
    print('Холоп начал делать действие...')
    action()
    print('Холоп закончил...')
    
    
def sum(a, b):
    print('Программа начала считать...')
    print(a + b)
    print('Программа удачно завершила вычисление')
    # return a + b
    
# do_eat()
# do_sleep()

order(do_eat)
order(do_sleep)
    

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



