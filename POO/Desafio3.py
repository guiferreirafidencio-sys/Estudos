class Livro:
    def __init__(self,titulo,autor):
        self._titulo = titulo
        self._autor = autor
        self.disponivel = True
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor

    def emprestar(self):
        self.disponivel = False
    def delvolvido(self):
        self.disponivel = True

    def exibir(self):
        if self.disponivel :
            print(f"{self.titulo} Autor:{self.autor}")
            return  
        
        print(f"{self.titulo} Autor:{self.autor}  \nNão Esta disponivel")

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.Usuarios = []

    def verificar_idade(self,usuario):
        if usuario.idade >= 18 :
            return True
        return False
    
    def adicionar_livro(self,livro):
        self.livros.append(livro)

    def listar_disponiveis(self):
        if self.livros :

            for x in self.livros:
                if x.disponivel :
                    x.exibir()
        else:
            print("Não possui livros Disponiveis")
            
    def emprestar(self,usuario,livro):
        
        if livro in self.livros and self.verificar_idade(usuario):
            if livro.disponivel:
                usuario.pegar_livro(livro)
                livro.emprestar()
                if not usuario in self.Usuarios:
                    self.Usuarios.append(usuario)
                    return
                print("Usuario existente")
                return
            
            print("Livro não esta disponivel")
            return
        print("Este livro não possui na biblioteca ou voce não possui idade minima")


    def devolver(self,usuario,livro):
        if livro in self.livros and self.verificar_idade(usuario):
            usuario.devolver_livro(livro)
            livro.delvolvido()
            if  not usuario.livros_emprestados:
                self.Usuarios.remove(usuario)
                return
        print("Este livro não possui na biblioteca ou voce não possui idade minima")
    
class Usuario:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.livros_emprestados = []
    
    def pegar_livro(self,livro):
        if len(self.livros_emprestados) <= 3:
            self.livros_emprestados.append(livro)
        else:
            print("voce nao pode pegar livro voce possui 3 livros")
            return
    def devolver_livro(self,livro):
        
        self.livros_emprestados.remove(livro)

    def __str__(self):
        return self.nome
    
B1 = Biblioteca()
Livro1 = Livro("Pequeno Principe","Monteiro lobato")

user1 = Usuario("Guilherme",29)


B1.adicionar_livro(Livro1)
B1.listar_disponiveis()
B1.emprestar(user1,Livro1)
print(B1.Usuarios)
B1.devolver(user1,Livro1)