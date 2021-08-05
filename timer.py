import linecache
from time import time, ctime, sleep


mpath='C:/ptst/'
filename='profile.txt'
path=mpath+filename
profile_file = open(path,'r')
content=profile_file.readlines()
len_f=len(content)
profile_file.close()
global_time_step=1


def param_gen(n,path):#wyciaga dane z pliku profilu do testow
    y=linecache.getline(path, n)
    y=y.strip().split(',')
    param = [' t=' + y[0], ' rh=' + y[1], y[2]]
    return param


def logger(param):
    t=time()
    stamp=ctime(t).split(' ')
    stamp=[stamp[3],stamp[2],' ',stamp[1],' ',stamp[4]]
    out_name='wynik.txt'
    file_out=open(mpath+out_name,'a')
    file_out.writelines(stamp+[param[1]]+['\r\n'])#param do input
    file_out.close()


def timex(x,time_step):
    t_start = time()
    test_multipler = 0.1 #zmniejsza faktyczny czas wykonywania dla potrzeb testów
    while (t_start+float(param_gen(x,path)[2])*test_multipler)>time():
        logger(param_gen(x,path))
        sleep(time_step)


for l in range(1, len_f):
    timex(l,global_time_step)




