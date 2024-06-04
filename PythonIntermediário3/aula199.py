from threading import Thread
from threading import Lock
from time import sleep
"""
class MyThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MyThread('Thread 1', 2)
t1.start()
t2 = MyThread('Thread 2', 3)
t2.start()
t3 = MyThread('Thread 3', 5)
t3.start()

for i in range(20):
    print(i)
    sleep(1)"""

"""def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar,args=('Hello World 1!', 5))
t1.start()
t2 = Thread(target=vai_demorar,args=('Hello World 2!', 3))
t2.start()
t3 = Thread(target=vai_demorar,args=('Hello World 3!', 2))
t3.start()

for i in range(10):
    print(i)
    sleep(.5)"""

"""def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar,args=('Hello World 1!', 6))
t1.start()

while t1.is_alive():
    print('Esperando a Thread!')
    sleep(2.5)

print('Thread Finalizada!!!')"""

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()


        if self.estoque < quantidade:
            print('Não temos ingressos o suficiente.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). ' 
              f'Ainda temos {self.estoque} em estoque')
        
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)
    
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)