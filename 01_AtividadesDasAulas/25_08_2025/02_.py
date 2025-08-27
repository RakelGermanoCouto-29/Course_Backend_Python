#-------- Atividade 1 --------

#Gerenciamento de lojas


produtos = []
encontrado = False


while True:
    print("\nSelecione a opção desejada:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Calcular")
    print("5 - Exibir categorias únicas")
    print("6 - Atualizar")
    print("7 - sair")

    option = int(input())

    if option == 1 :
        Ultima_Posicao_Lista = len(produtos)
        print("\nCadastrar produto:")

        nome = input(f"Digite o nome do produto:")
        codigo = int(input(f"Digite o código do produto '{nome}':"))
        descricao = input(f"Digite a descrição do produto '{nome}':")
        quantidade = int(input(f"Digite a quantidade do produto '{nome}':"))
        preco = float(input(f"Digite o valor do produto '{nome}':"))

        item = {
            "Nome": nome,
            "Codigo": codigo,
            "Descrição" : descricao,
            "Quantidade" : quantidade,
            "Preço" : preco
        }

        produtos.insert(Ultima_Posicao_Lista, item)
        print(f"\nO Dicionario é: {item}\n")
        print(f"A lista é:{produtos}")

    elif option == 2:

        for produto in produtos:
            for chave, value in produto.items():
                print(f"{chave} : {value}")
                
            print("-"*20)
    elif option == 3:
        busca = input(f"\nDigite o nome do produto: ")
        for i in produtos:
            if i["Nome"] == busca:
                print(i)
                encontrado = True
            elif not encontrado:
                print(f"{busca} não encontrado")

    elif option == 4:
        print("\n")
        total = 0

        while True:
            busca = input(f"\nDigite o nome do produto ou fim para encerrar ")
            
            if busca.lower() == "fim":
                if total > 10 :
                    total *= 0.9
                    print(f"Pague {total} reais")
                    break
                else: 
                    break
            else:
                for i in produtos:
                    if i["Nome"] == busca:
                        print(i)
                        encontrado = True
                        if i["Quantidade"] == 0:
                            print("Produto sem estoque.")
                        else:
                            total += i["Preço"]
                            print(f"Valor: {total}")
                            i["Quantidade"] -= 1
                    elif not encontrado:
                        print(f"{busca} não encontrado")


    elif option == 5:
        print("\nNomes:\n")
        for i in produtos:
            print(i["Nome"])

    elif option == 6 :
        print("\nAtualizar produto:")

        busca = input("\nDigite o nome do produto: ")
        encontrado = False  # resetar antes de cada busca

        for i in produtos:
            if i["Nome"] == busca:
                print("Produto encontrado:", i)

                # Atualiza os valores
                i["Quantidade"] = int(input(f"Digite a nova quantidade do produto '{busca}': "))
                i["Preço"] = float(input(f"Digite o novo valor do produto '{busca}': "))

                print("\nProduto atualizado com sucesso!")
                print(i)
                encontrado = True
                break  # sai do loop depois de atualizar

        if not encontrado:
            print(f"{busca} não encontrado.")

    elif option == 7:
        break

    


    
    