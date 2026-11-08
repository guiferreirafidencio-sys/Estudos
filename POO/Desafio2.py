class Controle:
    def __init__(self):
        self.ligar = False
        self.volume = 0
        self.canal = ["1*","2","3","4","5"]
        self.gb = 0
    
    def ligar_tv(self):

        if self.ligar:
            self.ligar = False
        else:
            self.ligar = True

    def volumer(self):
        print("volume")
        volume = int(input("-"))
        if volume > 100:
            self.volume = 100
        elif volume < 0 :
            self.volume = 0

        else:
            self.volume = volume
    
    def canals_a (self):  
        self.gb += 1
        if self.gb > 4 :
            self.gb = 0
        elif self.gb < -4:
            self.gb = 0
            
        self.canal[self.gb] = self.canal[self.gb]+"*"
        a = self.gb -1
        self.canal[a] = self.canal[a].replace("*", "")
    
    def canals_b (self):  
        self.gb -= 1
        if self.gb > 4 :
            self.gb = 0
        elif self.gb < -4:
            self.gb = 0
            
        self.canal[self.gb] = self.canal[self.gb]+"*"

        
        a = self.gb + 1 
        
        
        self.canal[a] = self.canal[a].replace("*", "")
       

    def exbir(self):
        import os

        os.system("cls")
        if self.ligar:
            print(f"""
______________________________
Canal {self.canal[0]}  {self.canal[1]}  {self.canal[2]}  {self.canal[3]}  {self.canal[4]}
volume = {self.volume}
______________________________
< c >  vol+ @


            """)
        
        else:
                pass
    def fluxo(self):    
        self.exbir()
        digite = input("-")
        if digite == "@":
            self.ligar_tv()
        elif digite ==  "+" or digite == "-":
            self.volumer()
        elif digite == "<":
            self.canals_b()
        elif digite == ">":
            self.canals_a()
        elif digite == "0":
            return True

c1 = Controle()
while True:
    a = c1.fluxo()
    if a :
        break