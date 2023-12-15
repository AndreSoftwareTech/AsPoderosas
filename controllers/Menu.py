from .apresentacao import cabecalho, saudacao
def menu():
    var = "Sim"
    while var.capitalize() == "Sim":
        cabecalho()
        saudacao()
        
        var = input("Deseja continuar no sistema?\nSim\nNao\n>> ")
    print("Voce saiu do sistema\nVolte sempre!")