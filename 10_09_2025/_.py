class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
    
    def aplicar_desconto(self, desconto):
        if 0 < desconto < 100:
            desconto = desconto / 100
            self.__preco -= self.__preco * desconto
        else:
            print("⚠️ Digite um valor entre 0 e 100.")
    
    def __str__(self):
        return (
            f"📄 Dados do Produto\n"
            f"Produto: {self.__nome}\n"
            f"Preço: R$ {self.__preco:.2f}\n"
            f"Estoque: {self.__estoque} un"
        )

def exibir_menu():
    print("\n===== CADASTRO DE PRODUTO =====")
    print("1 - 📝 Cadastrar Produto")
    print("2 - 💵 Adicionar desconto por nome")
    print("3 - 📄 Consultar dados por nome")
    print("4 - ❌ Sair")

# Dicionário para armazenar os produtos
produtos = {}

while True:
    exibir_menu()
    try:
        comando = int(input("Escolha uma opção: "))
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número de 1 a 4.")
        continue

    match comando:
        case 1:
            nome_input = input("Informe o nome do produto: ").strip()
            nome = nome_input.lower()  # armazena o nome em minúsculas
            if nome in produtos:
                print("⚠️ Produto já cadastrado. Deseja sobrescrever? (s/n)")
                if input().lower() != 's':
                    continue
            try:
                preco = float(input("Informe o preço do produto: ").strip())
                estoque = int(input("Informe a quantidade do produto: ").strip())
            except ValueError:
                print("⚠️ Dados inválidos. Tente novamente.")
                continue

            produtos[nome] = Produto(nome_input, preco, estoque)  # mantém nome original para exibição
            print(f"✅ Produto '{nome_input}' cadastrado com sucesso!")

        case 2:
            if not produtos:
                print("⚠️ Nenhum produto cadastrado ainda.")
                continue
            nome = input("Informe o nome do produto para aplicar desconto: ").strip().lower()
            if nome not in produtos:
                print("⚠️ Produto não encontrado.")
                continue
            try:
                desconto = float(input("Digite o desconto a ser aplicado (%): "))
                produtos[nome].aplicar_desconto(desconto)
                print("✅ Desconto aplicado com sucesso!")
            except ValueError:
                print("⚠️ Entrada inválida. Digite um número válido.")

        case 3:
            if not produtos:
                print("⚠️ Nenhum produto cadastrado ainda.")
                continue
            nome = input("Informe o nome do produto para consultar: ").strip().lower()
            if nome in produtos:
                print(produtos[nome])
            else:
                print("⚠️ Produto não encontrado.")

        case 4:
            print("👋 Encerrando o sistema. Obrigado!")
            break

        case _:
            print("⚠️ Opção inválida. Escolha entre 1 e 4.")
