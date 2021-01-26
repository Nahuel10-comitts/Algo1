import unittest
# from practica_objetos import Persona
class Persona:
    
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def crecer_un_centimetro(self):
        self.altura += 0.01

persona = Persona("Nahuel Lescano", 21, 1.83)
persona.crecer_un_centimetro()
class Test_Persona(unittest.TestCase):

    def test_creo_una_persona_y_crece_una_vez(self):
        persona = Persona("Nahuel", 21, 1.83)

        persona.crecer_un_centimetro()

        self.assertEqual(persona.altura, 1.84)

if __name__ == "__main__":
    unittest.main()