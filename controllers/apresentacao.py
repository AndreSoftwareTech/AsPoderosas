from datetime import datetime
from time import sleep

def cabecalho():
    for i in range(10):
        sleep(0.1)
        print("*")
    sleep(0.5)
    print("Bem vindo a Techmaster")

def saudacao():
    hora = datetime.now(tz= None)
    
    if hora.hour >= 5 and hora.hour <13:
        print(f"Agora é {hora.hour}:{hora.minute}")
    
    elif hora.hour >= 13 and hora.hour <18:
        print(f"Agora é {hora.hour}:{hora.minute}")
    
    else:
        print(f"Agora é {hora.hour}:{hora.minute}")
