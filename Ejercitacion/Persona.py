class Persona:
#     nombre = "Nahuel Lescano"
#     edad = 21
#     altura = 1.90
#     def __init__(self, nombre, edad, altura):
#         self.nombre = nombre
#         self.edad = edad
#         self.altura = altura
# 
#     def crecer_un_centimetro(self):
#         self.altura += 0.01
    def __init__(self, nombre, edad, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        
    def crecer_un_centimetro(self):
        self.__altura += 0.01

        
persona = Persona("Nahuel Lescano", 21, 1.83)
# persona.crecer_un_centimetro()
print(persona.__dict__)
print(persona._Persona__altura)