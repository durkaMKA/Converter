import time



def timer(b):
        for i in range(0,b):
            m,i = divmod(i,60)
            secondomer = '{:02d}:{:02d}'.format(m,i)
            print(secondomer, end = '\r')
            time.sleep(1)
        print(time.strftime('%H:%M:%S'))
        print(secondomer)
inp = int(input('Введите время для секундомера:'))                 
timer(inp)






