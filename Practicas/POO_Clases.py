"1"

class Estudiante:
    def __init__(self, nombre, nota1, nota2, nota_promedio):
        self.__nombre = nombre
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota_promedio = nota_promedio
        
    def mostrar_informacion(self):
        return (f"Nombre: {self.__nombre}, Nota 1: {self.__nota1}, Nota 2:  {self.__nota2}, Nota Promedio: {self.__nota_promedio}")
    
    def obtener_nota_promedio(self, ):
        self.__nota_promedio = (self.__nota1 + self.__nota2) / 2
        return self.__nota_promedio
        
juan = Estudiante("Juan",35,40, 0)
juan.obtener_nota_promedio()
print (juan.mostrar_informacion())

"2"

class Estudiante:
        
    def __init__(self, nombre, nota1, nota2, nota_promedio=0):
        if not (0 <= nota1 <= 5) or not (0 <= nota2 <= 5):
            raise ValueError("Las notas deben estar entre 0 y 5")
        self.__nombre = nombre
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota_promedio = nota_promedio  
                
    def mostrar_informacion(self):
        return (f"Nombre: {self.__nombre}, Nota 1: {self.__nota1}, Nota 2:  {self.__nota2}, Nota Promedio: {self.__nota_promedio}")
    
    def obtener_nota_promedio(self, ):
        self.__nota_promedio = (self.__nota1 + self.__nota2) / 2
        return self.__nota_promedio
        
juan = Estudiante("Esteban",3,4, 0)
juan.obtener_nota_promedio()
print (juan.mostrar_informacion())

"3"