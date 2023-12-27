import math
import random
import openpyxl


def lerArquivo():
    arq = open("entrada.txt")
    linhas = arq.readlines()
    qntdCidades = linhas[0].count(" ") + 1

    coordenadasX = linhas[0].split()
    coordenadasY = linhas[1].split()

    cidades = []
    letra = 'A'
    for i in range(qntdCidades):
        coordenadaX = coordenadasX[i]
        coordenadaY = coordenadasY[i]
        cidades.append([letra, coordenadaX, coordenadaY])
        letra = chr(ord(letra) + 1)

    return qntdCidades, cidades


def matrizDeDistancias(qntdCidades, cidades):
    matrizAdj = []
    for i in range(qntdCidades):
        matrizAdj.append([0] * qntdCidades)

    for i in range(qntdCidades):
        for j in range(qntdCidades):
            if i != j:
                matrizAdj[i][j] = math.sqrt(
                    math.pow(float(cidades[i][1]) - float(cidades[j][1]), 2)
                    + math.pow(float(cidades[i][2]) - float(cidades[j][2]), 2))

    return matrizAdj


def calcularCusto(circuito, matrizAdj):
    custo = 0
    for i in range(len(circuito) - 1):
        # o cirucito é uma lista de cidades, e cada cidade é representada por uma letra
        # então, para acessar a matriz de adjacência, é necessário converter a letra para um número
        custo += matrizAdj[ord(circuito[i]) - 65][ord(circuito[i + 1]) - 65]

    return custo


def operador1(circuito, randomizacao):
    ultimoValor = circuito.pop()

    circuitos = []

    for i in range(len(circuito)):
        for j in range(i + 1, len(circuito)):
            circuitoAux = circuito.copy()
            circuitoAux[i], circuitoAux[j] = circuitoAux[j], circuitoAux[i]
            circuitos.append(circuitoAux)

    for circuitoAdd in circuitos:
        circuitoAdd.append(circuitoAdd[0])

    if randomizacao == 1:
        random.shuffle(circuitos)

    circuito.append(ultimoValor)
    return circuitos


def operador2(circuito, randomizacao):
    ultimoValor = circuito.pop()
    circuitos = []

    for i in range(len(circuito)):
        for j in range(i + 1, len(circuito)):
            circuitoAux = circuito.copy()
            circuitoAux[i:j+1] = circuitoAux[i:j+1][::-1]
            circuitos.append(circuitoAux)

    for circuitoAdd in circuitos:
        circuitoAdd.append(circuitoAdd[0])

    if randomizacao == 1:
        random.shuffle(circuitos)

    circuito.append(ultimoValor)
    return circuitos


def recursiva(circuitosGerados, matrizAdj, custo, circuito, inicial, operador, randomizacao, passos, circuitoOriginal):
    for circuitoGerado in circuitosGerados:
        passos += 1
        custoGerado = calcularCusto(circuitoGerado, matrizAdj)
        print(circuitoGerado, " -> ", custoGerado)
        if custoGerado < custo:
            print("---------------------------------------------------------")
            print("Circuito melhorou")
            print(circuitoGerado, " -> ", custoGerado)
            print("---------------------------------------------------------")
            custo = custoGerado
            circuito = circuitoGerado
            if operador == 1:
                recursiva(operador1(circuito, randomizacao), matrizAdj,
                          custo, circuito, inicial, operador, randomizacao, passos, circuitoOriginal)
            else:
                recursiva(operador2(circuito, randomizacao), matrizAdj,
                          custo, circuito, inicial, operador, randomizacao, passos, circuitoOriginal)

            return
        if circuitosGerados.index(circuitoGerado) == len(circuitosGerados) - 1:
            print("---------------------------------------------------------")
            print("Melhor Circuito :D")
            # melhorCircuito = circuito
            # melhorCircuito.append(melhorCircuito[0])
            print(circuito, " -> ", custo)
            print("Passos: ", passos)
            # Adiciona os resultados no arquivo de saida
            dados = [inicial, operador, randomizacao, custo, passos]
            global sheet
            global workbook

            sheet.append(dados)
            workbook.save("saida.xlsx")

            # arquivo = open("saida.xlsx", "a")
            # O padrão é o seguinte: (inicial, Operador, Randomização), Custo, Passos
            # arquivo.write(str(inicial) + ", " + str(operador) + ", " +
            #   str(randomizacao) + ", " + str(custo) + ", " + str(passos) + "\n")
            passos = 0
            print("---------------------------------------------------------")
            return circuitoOriginal


def solver(estadoInical, operador, randomizacao, circuitoIncial, matrizAdj, passos):

    if (estadoInical == 1):
        circuito = circuitoIncial
    else:
        circuito = circuitoIncial
        circuito.pop()
        random.shuffle(circuito)
        circuito.append(circuito[0])

    custo = calcularCusto(circuito, matrizAdj)

    if (operador == 1):
        circuitosGerados = operador1(circuito, randomizacao)
    else:
        circuitosGerados = operador2(circuito, randomizacao)

    recursiva(circuitosGerados, matrizAdj, custo,
              circuito, estadoInical, operador, randomizacao, passos, circuito)


workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(["Estado Inicial", "Operador",
              "Randomização", "Custo", "Passos"])


def main():

    qntdCidades, cidades = lerArquivo()
    print("Quantidade de cidades: ", qntdCidades)
    print("Cidades: ", cidades)
    matrizAdj = matrizDeDistancias(qntdCidades, cidades)
    print("Matriz de Adjacência: ", matrizAdj)
    # passos = 0
    # variacoes = [
    #     (1, 1, 0, "Estado Inicial 1 com Operador 1 sem randomização da vizinhança."),
    #     (1, 1, 1, "Estado Inicial 1 com Operador 1 com randomização da vizinhança."),
    #     (1, 2, 0, "Estado Inicial 1 com Operador 2 sem randomização da vizinhança."),
    #     (1, 2, 1, "Estado Inicial 1 com Operador 2 com randomização da vizinhança."),
    #     (2, 1, 0, "Estado Inicial 2 com Operador 1 sem randomização da vizinhança."),
    #     (2, 1, 1, "Estado Inicial 2 com Operador 1 com randomização da vizinhança."),
    #     (2, 2, 0, "Estado Inicial 2 com Operador 2 sem randomização da vizinhança."),
    #     (2, 2, 1, "Estado Inicial 2 com Operador 2 com randomização da vizinhança.")
    # ]
    # for variacao in variacoes:

    #     circuito = []
    #     for cidade in cidades:
    #         circuito.append(cidade[0])

    #     circuito.append(circuito[0])
    #     estadoInicial, operador, randomizacao, variacaoDescricao = variacao
    #     print("")
    #     print("")
    #     print("---------------------------------------------------------")
    #     print(variacaoDescricao)
    #     print("---------------------------------------------------------")
    #     print("")
    #     print("")
    #     for i in range(2):
    #         solver(estadoInicial, operador, randomizacao,
    #                circuito, matrizAdj, passos)


main()
