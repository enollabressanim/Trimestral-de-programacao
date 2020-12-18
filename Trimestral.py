class LivroQualquer():     
    def __init__(self, titulo = str, autor= str, editora= str, lancamento= str,  paginas= str, isbn= str):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.lancamento = lancamento
        self.paginas = paginas
        self.isbn = isbn

    @staticmethod
    def verificar_isbn(isbn= str):
        b = list(isbn)
        k = []
        for val in b:
            k.append(int(val))
        c, d, item = k[:12:2], k[1::2], k[12]
        g, h = list(map(lambda x: x * 1, c)), list(map(lambda x: x * 3, d))
        lista = g + h
        soma = sum(lista)
        porc = soma % 10
        result = 10 - porc
        if result == item:
            return True
        else:
            return None  
        
class LivroFisico(LivroQualquer):
    def __init__(self, capa= str, localizacao= str, livros_cadastrados= str):
        super().__init__(titulo = str, autor= str, editora= str, lancamento= str,  paginas= str, isbn= str) 
        self.capa = capa
        self.localizacao = localizacao
        self.livros_cadastrados = []
    
    def buscar_livro(self, livros_cadastrados= str, titulo= str):
        for livro in self.livros_cadastrados:
                if livro["titulo"] == titulo:
                    return livro
        return None
    
    def cadastrar_livro(self, titulo= str, capa= str, autor= str, lancamento= str, editora= str, isbn= str, paginas= str, localizacao= str):
        if self.verificar_isbn(isbn) is True:
            if self.buscar_livro(self.livros_cadastrados, titulo) is None:
                livro = {"titulo":titulo,    
                        "capa":capa,
                        "autor": autor,
                        "lançamento": lancamento,
                        "editora": editora,
                        "isbn": isbn,
                        "paginas": paginas,
                        "localizacao":localizacao}
                self.livros_cadastrados.append(livro)
                print('Livro cadastrado com sucesso!')
                return True
            else:
                print('Livro já cadastrado!')
                return False
        else:
            print('ISBN é inválido!')
            return None

class LivroDigital(LivroQualquer):    
    def __init__(self, url= str, tamanho= str, livros_cadastrados= str):
        super().__init__(titulo = str, autor= str, editora= str, lancamento= str,  paginas= str, isbn= str,)
        self.url = url
        self.tamanho = tamanho
        self.livros_cadastrados = []
    
    def buscar_livro(self, livros_cadastrados= str, titulo= str):
        for livro in self.livros_cadastrados:
                if livro["titulo"] == titulo:
                    return livro
        return None
    
    def cadastrar_livro(self, titulo= str, url= str, autor= str, lancamento= str, editora= str, isbn= str, paginas= str, tamanho= str):
        if self.verificar_isbn(isbn) is True:
            if self.buscar_livro(self.livros_cadastrados, titulo) is None:
                livro = {"titulo":titulo,    
                        "url": url,
                        "autor": autor,
                        "lançamento": lancamento,
                        "editora": editora,
                        "isbn": isbn,
                        "paginas": paginas,
                        "tamanho": tamanho}
                self.livros_cadastrados.append(livro)
                print('Livro cadastrado com sucesso!')
                return True
            else:
                print('Livro já cadastrado!')
                return False
        else:
            print('ISBN-13 inválido!')
            return None

class Menu():
    def __init__(self):
        self.isbn = LivroQualquer()
        self.livrofisico = LivroFisico(LivroQualquer)
        self.livrodigital = LivroDigital(LivroQualquer)

    def imprimir_commandos(self):
        print("1 - Livro físico")
        print("2 - livro digital")
        print("")

    def main(self):
        self.imprimir_commandos()
        opcao = int(input("Digite uma opção acima: "))
        while opcao in [1, 2]:
            if opcao == 1:
                titulo = input("titulo: ")
                autor = input("autor: ")
                editora = input("editora: ")
                lancamento = input("lançamento: ")
                paginas = input("paginas: ")
                isbn = input("isbn: ")
                capa = input("tipo de capa: ")
                localizacao = input("localização:")
                self.livrofisico.cadastrar_livro(titulo, autor, editora, lancamento, paginas, isbn, capa, localizacao)
                self.isbn.verificar_isbn(isbn)
            
            elif opcao == 2:
                titulo = input("titulo: ")
                autor = input("autor: ")
                editora = input("editora: ")
                lancamento = input("lançamento: ")
                paginas = input("paginas: ")
                isbn = input("isbn: ")
                url = input("url: ")
                tamanho = input("tamanho:")
                self.livrodigital.cadastrar_livro(titulo, autor, editora, lancamento, paginas, isbn, url,tamanho)
                self.isbn.verificar_isbn(isbn)

            self.imprimir_commandos()
            opcao = int(input("Digite uma opção acima: "))

if __name__ == "__main__":
    g = Menu()
    g.main()