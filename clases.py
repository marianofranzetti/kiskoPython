class Cerveza:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    def __repr__(self):
        return "cerveza: " + str(self.nombre) + " y su precio es: " + str(self.precio)


class Gaseosa:
    def __init__(self,nombre,sabor,precio):
        self.nombre = nombre
        self.sabor = sabor
        self.precio = precio
    def __repr__(self):
        return "gaseosa: " + str(self.nombre) + " con sabor a: " + str(self.sabor) + " y su precio " + str(self.precio)


class Kiosko:
    def __init__(self,nombre):
        self.nombreKiosko = nombre
        self.cervezas = list[Cerveza]
        self.gaseosas = list[Gaseosa]



def crearKiosko():
    #creo primero las cervezas
    brahma = Cerveza('brahma', 10)
    quilmes = Cerveza('quilmes',15)
    stella = Cerveza('stella artois',20)

    #creo despues las gaseosas
    cocaCola = Gaseosa('coca-cola','cola',30)
    manaos = Gaseosa('manaos','cola',15)

    #creo lista de gaseosas y las agrego
    gaseosas = []
    gaseosas.append(cocaCola)
    gaseosas.append(manaos)

    #creo lista de cervezas y las agrego
    cervezas = []
    cervezas.append(brahma)
    cervezas.append(quilmes)
    cervezas.append(stella)

    #creo un kiosko con la lista de gaseosas y cervezas
    kiosko = []
    kiosko.append(cervezas)
    kiosko.append(gaseosas)

    #retorno el kisko creado
    return kiosko



def mostrarKioskoClaudio():
    kioskoNuevo = crearKiosko()

    print('bienvenido a mi kosko chileno')
    for x in kioskoNuevo:
        for y in x:
            print(y)



print(mostrarKioskoClaudio())




    