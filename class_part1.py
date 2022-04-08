###Class
'''___EJEMPLOS____'''


'''class Teclado:
 def __init__(self,Marca, precio, calidad):
   self.marca = Marca
   self.precio = precio
   self.calidad = calidad
class Reseña(Teclado):
 def __init__(self, Review):
    self.klo = Review
reseña1 = Reseña("_____Reseña____")
print(reseña1.klo)

keyboard1 = Teclado('Razer Huntsman mini Tkl', 'el precio es de unos 12.000','Es uno de los mejor calidad precio en el mercado. ')
keyboard2 = Teclado('Hyperx Origins 60 %', 'el precio es de unos 10.000', 'Es un buen teclado pero es mejor ahorrar 2000 pesos y comprar el Razer')
print(f'El teclado es: {keyboard1.marca}')
print(f'El Precio  es:  {keyboard1.precio}')

print(f'El teclado es: {keyboard2.marca}')
print(f'El precios es: {keyboard2.precio}')
print(f'Reseña / Recomendacion:  {keyboard1.calidad}')
print(f'Reseña / Recomendacion:  {keyboard2.calidad}')'''





###Class2 con variable###
'''class Perro:
    ##Atributos de la clase##
    especie = "Mamifero"
    #constructor#
    def __init__(self,nombre,raza): #esto es una instancia# 
#atributos de la instancia##
     self.nombre = nombre
     self.raza = raza

perro1 = Perro('sammy','Caniche')
print(F'Su nombre es :{perro1.nombre}')
print(f'Su raza es: {perro1.raza}')
print(f'Es un : {perro1.especie}')''' 

#Metodos modoficados
''''
class Perro:
    #ATRIBUTOS DE LA CLASE#
    especie = "Mamiferos"
    #Constructor = Contruye el Objeto #
    def __init__(self, nombre, raza):
        print(f'Creando perro:  {nombre} , {raza}')
        #ATRIBUTOS DE LA INSTANCIA
        self.nombre = nombre
        self.raza = raza
    def ladra(self):
        print('Guau!')
    def camina(self, pasos):
            print(f'caminando {pasos} pasos')
mi_Perro1 = Perro('Tyrone '  ,  ' Pinscher')
mi_Perro1.ladra()
mi_Perro1.camina(200)'''

#Desafio 1
'''class Personas:
    ojos = 2
    manos = 2
    piernas = 2
    def __init__(self,nombre,color_pelo,color_ojos):
      self.nombre = nombre
      self.color_pelo = color_pelo
      self.color_ojos = color_ojos
    def Saludar(self):
        print (f'hola {Persona1.nombre}, como estas?')
    def Presentacion(self, Presentar):
      print(f'hola, me llamo {Presentar}')
Persona1 = Personas('javier','rubio','marron')
persona2 = Personas('Mara','gris','azules')
Persona1.Presentacion(Persona1.nombre)
persona2.Saludar()
print(persona2.color_ojos , Persona1.color_ojos)'''

##__str__ & __len__ & __getitem__ & __setitem__ & iter


class Vector():
    def __init__(self,data):
        self._data = data
    def __str__(self):
        return f'the values are : {self._data}'
    def __len__(self):
        return len(self._data)
    def __getitem__(self,pos):
        return self._data[pos]
    def __setitem__(self,pos, value):
        self._data[pos] = value
    def __iter__(self):
        #for pos in range (0, len(self._data)):
            #yield f'value[{pos}] : {self._data[pos]}'
        for pos in range(0, len(self._data)):
            yield f'value[{pos}]:{self._data[pos]}'

v = Vector([1,2])
for vec in v:
    print(vec)  