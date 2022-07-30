import random
def rolldice(min,max):
    while True:
            print('rolling the dice....')
            no=random.randint(min,max)
            print(f'your number:{no}')
            choice= input('Do you want to  roll dice again?(y/n)')
            if choice.lower()=='n':
                break
rolldice(1,6)
