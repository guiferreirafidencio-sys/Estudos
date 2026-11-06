

class Produto():
    def __init__(self,nome,preço,qtd = 0):
        self.nome = nome
        self.preço = preço
        self.estoque = Estoque(qtd)

 
    def exibir(self):
        return self.nome ,f'R${self.preço}  qtd{self.estoque.qtd}'


    
class Estoque():
    def __init__(self,qtd = 0):
        self.qtd = qtd
    def venda(self):
        if self.qtd == 0:
            print("Não é possivel comprar")
            return False
        
        self.qtd -= 1
        return True


class Loja():
    def __init__(self):
        self.vitrine = []
        self.cod = 0
    def adicionar_itens(self,item):
        self.vitrine.append(item)

    def exibir(self):
        for x in self.vitrine:
            print(x.exibir())

    def numero_pedido(self):
        self.cod += 1
        
    
    def compra(self,info,produto,clie):
        a = produto.estoque.venda()
        if a:
            self.numero_pedido()
            info.dado(produto,self.cod,clie,"Pendete")
            return
        print("Não foi possivel realizar a compra nao possui no estoque")

class Cliente():
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = int(idade)
        self.cpf = cpf
        self.pedido = []
    def ver_meu_pedido(self,a):
        for x in a.historico:
            if x["Cliente"].cpf == self.cpf:
                print("_______________________")
                print("Seu pedido\n",x["produto"].exibir(),x["Status"])
    def cancelar(self,a):
        for x in a.historico:
            if x["Cliente"].cpf == self.cpf:
                x["Status"] = "Cancelado"

class Pedidos():
    def __init__(self):
        self.historico = []

    def dado(self,produto,nu,clie,status):
        dict = {"produto": produto, "Numero do pedido": nu, "Cliente": clie, "Status": status}
        self.historico.append(dict)

    
a = Pedidos()
produto1 = Produto("Iphone8",80,1)
produto2 = Produto("Iphone9",100,15)
Cliente1 = Cliente("Guilherme",18,'553520')
loja = Loja()
loja.adicionar_itens(produto1)
loja.adicionar_itens(produto2)
loja.compra(a,produto1,Cliente1)
Cliente1.cancelar(a)
Cliente1.ver_meu_pedido(a)