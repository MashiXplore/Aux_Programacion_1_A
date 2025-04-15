class Animal:
    def __init__(self,nombre,raza,color):
        self.nombre = nombre
        self.raza = raza 
        self.color = color
    
    def imprime(self):
        print(f"Su nombre es: {self.nombre}",end = " ")
        print(f"Su raza es: {self.raza}")
        print(f"Su color es: {self.color}")
        
    def sonido():
        print("genera sonido..........")
        
    def morder():
        print("Muerde......")
    
    def comer():
        None

animal1 = Animal("Tayzn","Felin  a","Verde panda")
animal2 = Animal("Boby","pitbull","Negro")
animal3 = Animal("Chapi","Cachuchines","Banco y Negro")

animal1.imprime()
animal2.imprime()
animal3.imprime()



    

        