import time
def remit(a):
    while a:
        m,s= divmod(a,60)
        h,m = divmod(m,60)
        d,h = divmod(h,24)
        minsec= 'День: {:d},Время:{:d}:{:02d}:{:02d}'.format(d,h,m,s)
        print(minsec, end='\r')
        time.sleep(1)
        a-=1
    print(time.strftime('День:%a , %H : %M : %S'))
inp = int(input('Введите время для таймера:'))
remit(inp) 
