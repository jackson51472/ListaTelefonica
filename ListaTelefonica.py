def exec():
    telList = {}
    while True:
        resp = int(input("O que você deseja fazer?\n (1)Incluir Novo Nome\n  (2)Incluir Telefone\n   (3)Excluir Telefone\n>>"))
        while resp < 1 or resp > 4:
            resp = int(input("NÃO EXISTE ESSA FUNÇÃO\nO que você deseja fazer?\n (1)Incluir Novo Nome\n  (2)Incluir Telefone\n   (3)Excluir Telefone\n>>"))


        if resp == 1:
            nome = input("Digite o nome: ")
            telList[nome.lower()] = incluirNovoNome(nome)
        else:
            if resp == 2:
                incluirTelefone(telList)
            else:
                if resp == 3:
                    excluirTelefone(telList)
                else:
                    excluirNome(telList)

        print("Lista Telefônica")
        for pessoa in telList:
            print(f'NOME: {telList[pessoa]["nome"]} / TELEFONE: {telList[pessoa]}' )
        print("===" * 30)



    print(telList)
def incluirNovoNome(nome):

    dic = {}
    dic["nome"] = nome
    dic["telefone"] = [0]
    return dic

def incluirTelefone(telList):

    resp = input("Qual o nome da pessoa que você quer adicionar um numero? ")
    telefoneAdicionado = input("Digite o numéro que deseja adicionar: ")
    for i in telList[resp]["telefone"]:
        if i == 0:
            telList[resp]["telefone"].remove(0)

        if i == telefoneAdicionado:
            print("ESSA PESSOA JÁ TEM ESSE NUMERO ADICONADO\nNÃO SERA ADICIONADO OUTRO NUMERO IGUAL: ")
            break
        else:
            for i in telList:
                if i == resp.lower():
                    telList[resp]["telefone"].append(telefoneAdicionado)
                    

    return telList

def excluirTelefone(telList):
    numExcluido = input("Digite o nome da pessoa que você deseja excluir o NUMERO: ")
    numero = input("Digite o numero excluido: ")

    for pessoa in telList:
        if pessoa == numExcluido.lower():
            telList[numExcluido]["telefone"].remove(numero)


def excluirNome(telList):
    nomeExcluido = input("Digite o NOME da pessoa que você deseja excuir dos contatos: ")

    telList.pop(nomeExcluido)

    return 0



exec()