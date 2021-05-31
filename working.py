
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





