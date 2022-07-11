class Publicacao:
    def __init__(self, id, data_pub):
        self.id = id
        self.data_pub = data_pub
    def info(self):
        print(f"ID: {self.id} | DATA PUBLICAÇÂO: {self.data_pub}")

class Livro(Publicacao):
    def __init__(self, id, data_pub, titulo, __autor):
        Publicacao.__init__(self, id, data_pub)
        self.__autor = __autor
        self.titulo = titulo
    def info(self):
        print(f"ID: {self.id} | DATA PUBLICAÇÂO: {self.data_pub} | TITULO: {self.titulo} | AUTOR: {self.__autor}")

class Revista(Publicacao):
    def __init__(self, id, data_pub, __preco):
        Publicacao.__init__(self, id, data_pub)
        self.__preco = __preco
    def info(self):
        print(f"ID: {self.id} | DATA PUBLICAÇÂO: {self.data_pub} | PREÇO: R${self.__preco}")

lista_livros = []
lista_revistas = []

def adicionar_livro():
    id = int(input("Qual o ID do livro: "))
    data_pub = input("Qual a data de publicação do livro: ")
    titulo = input("Qual o titulo do livro: ")
    autor = input("Qual o autor do livro: ")
    livro = Livro(id, data_pub, titulo, autor)
    lista_livros.append(livro)

def remover_livro():
    id = int(input("Qual o ID do livro que deseja remover: "))
    for livro in lista_livros:
        if livro.id == id:
            lista_livros.remove(livro)

def adicionar_revista():
    id = int(input("Qual o ID da revista: "))
    data_pub = input("Qual a data de publicação da revista: ")
    preco = input("Qual o preço da revista: ")
    revista = Revista(id, data_pub, preco)
    lista_revistas.append(revista)

def remover_revista():
    id = int(input("Qual o ID da revista que deseja remover: "))
    for revista in lista_revistas:
        if revista.id == id:
            lista_revistas.remove(revista)

def listar_livros():
    for livro in lista_livros:
        livro.info()

def listar_revistas():
    for revista in lista_revistas:
        revista.info()

def menu():
    opcao = 0
    print("0: Ajuda\n1: Adicionar Livro\n2: Remover Livro\n3: Adicionar Revista\n4: Remover Revista\n5: Lista de Livros\n6: Lista de Revistas\n7: Sair")
    while opcao != 7:
        opcao = int(input("Qual opcao: "))
        if opcao == 1:
            adicionar_livro()
        elif opcao == 2:
            remover_livro()
        elif opcao == 3:
            adicionar_revista()
        elif opcao == 4:
            remover_revista()
        elif opcao == 5:
            listar_livros()
        elif opcao == 6:
            listar_revistas()
        elif opcao == 7:
            break
        elif opcao == 0:
            print("1: Adicionar Livro\n2: Remover Livro\n3: Adicionar Revista\n4: Remover Revista\n5: Lista de Livros\n6: Lista de Revistas\n7: Sair")

if __name__ == "__main__":
    menu()
