#esta função calcula centimetros para polegadas.
def cmtopol(n):
    pol = n/2.54
    tratamento = "{:.2f}".format(pol)
    return tratamento

#esta função calcula polegadas para centimetros.
def poltocm(n):
    cm = n*2.54
    tratamento = "{:.2f}".format(cm)
    return tratamento

#esta função calcula pés para metros
def fttom(n):
    f = n/3.281
    tratamento = "{:.2f}".format(f)
    return tratamento

#esta função calcula metros para pés
def mtoft(n):
    m = n*3.281
    tratamento = "{:.2f}".format(m)
    return tratamento

#esta função calcula farenheit para celcius
def fatoc(n):
    c = (n-32)/1.8
    tratamento = "{:.2f}".format(c)
    return tratamento

#esta função calcula celcius para farenheit
def ctofa(n):
    fa = (n*1.8)+32
    tratamento = "{:.2f}".format(fa)
    return tratamento

op = 0
#interface
def main():
    print("escolha uma opção para converter uma medida")
    print("1. para converter centimetros para polegadas")
    print("2. para converter de polegadas para centimetros")
    print("3. para converter pés para metros")
    print("4. para converter metros para pés")
    print("5. para converter farenheit para celcius")
    print("6. para converter celcius para farenheit")
    print("7. para encerrar a aplicação")
    op = int(input('digite agora o numero da opção'))
    #centimetros para polegadas
    if op == 1:
        print("centimetros para polegadas")
        print("a seguir digite o valor a ser convertido para polegadas")
        cm = float(input("insira agora um valor:"))
        print(cm, "centimetros em polegadas é igual a", cmtopol(cm), "polegadas")
        print(repetir())

    elif op == 2:
        print("polegadas para centimetros")
        print("a seguir digite o valor a ser convertido para centimetros")
        pol = float(input("insira agora um valor:"))
        print(pol, "polegadas em centimetros é igual a", poltocm(pol), "centimetros")
        print(repetir())

    elif op == 3:
        print("pés para metros")
        print("a seguir digite um valor a ser convertido para metros")
        f = float(input("insira agora um valor:"))
        print(f, "pés é igual a", fttom(f), "metros")
        print(repetir())

    elif op == 4:
        print("metros para pés")
        print("a seguir digite um valor a ser convertido para pés")
        m = float(input("insira agora um valor:"))
        print(m, "metros é igual a", mtoft(m), "pés")
        print(repetir())

    elif op == 5:
        print("farenheit para celcius")
        print("a seguir digite um valor a ser convertido para celcius")
        fa = float(input("insira agora um valor:"))
        print(fa, "Fº é igual a", fatoc(fa), "celcius")
        print(repetir())

    elif op == 6:
        print("celcius para farenheit")
        print("a seguir digite um valor a ser convertido para farenheit")
        ce = float(input("insira agora um valor:"))
        print(ce, "Cº é igual a", ctofa(ce), "farenheit")
        print(repetir())

    elif op == 7:
        print("encerrando o aplicativo...")
        exit()

    else:
        print("função não implementada")
        print(repetir())

def repetir():
    repetir = input("deseja executar alguma tarefa? Sim ou Não").lower()
    if repetir == "sim":
        main()
    elif repetir == "não":
        exit()
    else:
        print("erro: selecione uma opção válida.")
        return




if __name__ == "__main__":
    main()