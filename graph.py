from matplotlib import pyplot as pl
import numpy as np


data=np.loadtxt('/home/b03-401/Gleps/8/data.txt')
settings=np.loadtxt('/home/b03-401/Gleps/8/settings.txt')

Ulabel=(data/255)*3.3
Ulabel=np.round(Ulabel,2)

time=np.arange(0,len(Ulabel)*settings[0],settings[0])

fig,axs=pl.subplots(dpi=250)
pl.title('Процесс зарядки и разрядки конденсатора в RC-цепи',wrap=True)
pl.ylabel('Напряжение U')
pl.xlabel('Время t')


pl.xticks(np.arange(0,15,step=1))
pl.yticks(np.arange(0,3.5,step=0.25))



tzarad='Время зарядки: '+str(time[np.argmax(Ulabel)])+' c'
pl.text(8,3,tzarad,fontsize=8,fontstyle='italic',color='b')
trazrad='Время разрядки: '+str(max(time) - time[np.argmax(Ulabel)])+' c'
pl.text(8,2.7,trazrad,fontsize=8,fontstyle='italic',color='r')

pl.minorticks_on()
pl.grid(visible=True,
         which='major',
         linestyle='--',
         linewidth=0.2,
         color='0.5')
pl.grid(visible=True,
         which='minor',
         linestyle='--',
         linewidth=0.1,
         color='0.4')


redkotime=np.arange(0,len(Ulabel)*settings[0],settings[0]*10)
redkoU=[float(Ulabel[i]) for i in range(0,len(Ulabel),10)]
pl.scatter(redkotime,redkoU,c='r',s=4,marker='.')

x=pl.plot(time,Ulabel,c='b',linewidth=0.7)
pl.legend(x,['Graph-1'],loc=2)
pl.show()

fig.savefig('/home/b03-401/Gleps/8/Grapg.svg')































#pl.figure(dpi=200)
##x=pl.plot(n,wn80,linewidth=2)
##y=pl.bar(m1,wn80bnew,color='black')
##pl.legend([x[0],y[0]],  
##            ["Теоретическое распределение","Практическое распределение"], 
##            loc=1) 
##pl.title('Частота Wn для t = 40')
##pl.xlabel('Число отсчётов - n')
##pl.ylabel('Wn')
###pl.minorticks_on()
##pl.grid(visible=True,
##         which='major',
##         linestyle='--',
##         linewidth=0.5,
##         color='0.4') # Формат основных линиий сетки
##pl.grid(visible=True,
##         which='minor',
##         linestyle='--',
##         linewidth=1,
##         color='0.4')# Формат побочных линий
##pl.show()

##pl.xticks(np.arange(0,0.6,step=0.05))
###pl.yticks(np.arange(0,5,step=0.25))