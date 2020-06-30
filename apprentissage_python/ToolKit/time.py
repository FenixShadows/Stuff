import threading 
import time
# Définition des processus 
def process_one():
    i = 0
    while i < 10 :
        print('oooooooo')
        time.sleep(1)
        i += 1

def process_two():
    i = 0
    while i < 10 :
        print('xxxxxxx')
        time.sleep(1.5)
        i += 1

th1 = threading.Thread(target = process_one)
th2 = threading.Thread(target = process_two)

th1.start()
th2.start()
th1.join()
th2.join()

print('Fin du programme...')