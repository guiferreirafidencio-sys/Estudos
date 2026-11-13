class Produto:
    def __init__(self,nome,preço,quantidade = 0):
        self._nome = nome
        self._preço  = float(preço)
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @property
    def preço(self):
        return self._preço

    @property
    def quantidade(self):
        return self._quantidade

    def adicionar_estoque(self,valor):
        if valor > 0:
            self._quantidade += valor
        else:
            print("Valor errado")
    def tirar_estoque(self,valor):
        if valor > 0:
            if valor <= self.quantidade:
                self._quantidade -= valor
                return True
            print("Valor maior que a quantidae")
            return False
        else:
            print("apenas coloque o quanto deseja tirar")
            return False
    def exibir(self):
        print(f"{self.nome} R${self.preço:.2f}")




class Pedido:

    def __init__(self):             
        self.historico = []
        self.numero_pd = 1

    def add_historico(self,p1,qtdc):
        dic = {"item": p1, "Quantidade": qtdc , "Status": "PENDENTE", "NUPEDIDO": self.numero_pd}
        self.historico.append(dic)
        

    def calculo_Pedido(self,produto,quantidade_cliente):
        if quantidade_cliente <= produto.quantidade:
            self.resu = produto.preço * quantidade_cliente
            res = produto.tirar_estoque(quantidade_cliente)
            if res :
                
                print("Calculado")
                self.exibir_total(produto,quantidade_cliente)
                self.add_historico(produto,quantidade_cliente)
                self.numero_pd += 1 
                return
        else:
            print("Nao foi Possivel realizar seu pedido Estoque insuficiente\nEstoque ATUAl-",produto.quantidade)

    def exibir_total(self,produto,quantidade_cliente):

        print(f"-----------------------\n{'PEDIDO'.center(23)}\n-----------------------")
        
        print(f"item -{produto.nome}\nQuantidade - {quantidade_cliente}\nPreço R${self.resu:.2f}\nStatus: Pendente NUPEDIDO: {self.numero_pd}")

    def cancelar(self):
        print("------------------------------")
        digite = int(input("digite numero do seu pedido:"))
        digite = digite - 1
        if self.historico[digite]["Status"] == "Cancelado":
            print("Ja foi cancelado o pedido")
            return
        
        self.historico[digite]["Status"] = "Cancelado"

        a = self.historico[digite]["item"]
        a.adicionar_estoque(self.historico[digite-1]["Quantidade"])
        print("------------------------------\nPedido Cancelado")






        
item = Produto("HOT DOG",20,9000)
Loja = Pedido()
Loja.calculo_Pedido(item,12)

item2 = Produto("PIZZA", 45, 100)

Loja.calculo_Pedido(item, 12)
Loja.calculo_Pedido(item2, 3)
Loja.calculo_Pedido(item, 5)

Loja.cancelar()
print(Loja.historico)