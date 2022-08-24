import random
def rolldice(min,max):
    while True:
            print('rolling the dice....')
            no=random.randint(min,max)
            print(f'your number:{no}')
                      
            if no==1:
                print('[------]')
                print('[------]')
                print('[   0  ]')
                print('[------]')
                print('[------]')
            elif no==2:
                print('[------]')
                print('[      ]')  
                print('[  0 0 ]')
                print('[      ]')   
                print('[------]')
            elif no==3:
                print('[------]')
                print('[      ]')
                print('[ 0 0 0]')
                print('[      ]')
                print('[------]')
            elif no==4:
                print('[------]')
                print('[ 0  0 ]')
                print('[      ]')
                print('[ 0  0 ]') 
                print('[------]')
            else:
                 no==5
                 print('[------]')
                 print('[0    0]')
                 print('[   0  ]')
                 print('[0    0]')
                 print('[------]')
            choice= input('Do you want to  roll dice again?(y/n)')
            if choice.lower()=='y':
                continue
            else:
                break

rolldice(1,6)
