from particulas import Particula
import json

class administrador:
    def __init__(self):
        self.__particles = []

    def agregar_final(self, particle:Particula):
        self.__particles.append(particle)
    
    def agregar_incio(self, particle:Particula):
        self.__particles.insert(0,particle)

    def mostrar(self):
        for particle in self.__particles:
            print(particle)
    
    def __str__(self):
        return "".join(
            str(particle) + '\n' for particle in self.__particles
        )
    def guardar(self, ubicacion):
        try:

            with open(ubicacion, 'w') as file:
                lista = [particle.to_dict() for particle in self.__particles]
                print(lista)
                json.dump(lista, file, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as file:
                lista = json.load(file)
                self.__particles = [Particula(**particle)for particle in lista] 
            return 1
        except:
            return 0
        

# P01 = Particula(1,35,40,20,10,15,20,15,10)
# P02 = Particula(2,84,115,35,3,15,20,15,10)
# administrator = administrador()

# administrator.agregar_incio(P02)
# administrator.agregar_final(P01)

# administrator.mostrar()
