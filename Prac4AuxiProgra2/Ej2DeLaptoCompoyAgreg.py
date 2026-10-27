MAX_APPS = 50

class Pantalla:
    def __init__(self, tipo, ancho, alto):
        self.__tipo = tipo
        self.__ancho = ancho
        self.__alto = alto

    def get_tipo(self):
        return self.__tipo

    def get_ancho(self):
        return self.__ancho

    def get_alto(self):
        return self.__alto

    def __str__(self):
        return f"Pantalla({self.__tipo}, {self.__ancho}x{self.__alto})"

class Aplicacion:
    def __init__(self, nombre, tamanio):
        self.__nombre = nombre
        self.__tamanio = tamanio

    def get_nombre(self):
        return self.__nombre

    def get_tamanio(self):
        return self.__tamanio

    def __str__(self):
        return f"{self.__nombre} ({self.__tamanio} MB)"

class Laptop:
    def __init__(self, modelo, tipo_pantalla, ancho, alto):
        self.__modelo = modelo
        self.__cantApps = 0
        self.__apps = [None] * MAX_APPS
        # Composición: la Laptop crea su propia Pantalla
        self.__pantalla = Pantalla(tipo_pantalla, ancho, alto)

    def get_modelo(self):
        return self.__modelo

    def get_cantApps(self):
        return self.__cantApps

    def get_pantalla(self):
        return self.__pantalla
    # Agregación: la Aplicacion existe fuera de la Laptop y se le pasa
    def agregar_app(self, app):
        if self.__cantApps < MAX_APPS:
            self.__apps[self.__cantApps] = app
            self.__cantApps += 1
            return True
        return False

    def eliminar_apps(self):
        self.__apps = [None] * MAX_APPS
        self.__cantApps = 0

    def ordenar_apps(self):
        """Peso decreciente; si empatan, por nombre (A-Z)."""
        n = self.__cantApps
        for i in range(n - 1):
            for j in range(n - 1 - i):
                a, b = self.__apps[j], self.__apps[j + 1]
                if (a.get_tamanio() < b.get_tamanio() or
                        (a.get_tamanio() == b.get_tamanio()
                        and a.get_nombre() > b.get_nombre())):
                    self.__apps[j], self.__apps[j + 1] = b, a
    def __str__(self):
        texto = f"Laptop {self.__modelo} - {self.__pantalla} - {self.__cantApps} apps"
        for i in range(self.__cantApps):
            texto += f"\n    - {self.__apps[i]}"
        return texto

# ---------------- Funciones para los incisos ----------------
# a. Instanciar N laptops en un vector
def crear_laptops(n):
    laptops = []
    for i in range(n):
        print(f"\nLaptop {i + 1}")
        modelo = input("Modelo: ")
        tipo = input("Tipo de pantalla: ")
        ancho = int(input("Ancho: "))
        alto = int(input("Alto: "))
        laptops.append(Laptop(modelo, tipo, ancho, alto))
    return laptops

# b / e. Laptop con más aplicaciones
def laptop_con_mas_apps(laptops):
    mayor = laptops[0]
    for l in laptops:
        if l.get_cantApps() > mayor.get_cantApps():
            mayor = l
    return mayor

# c. Agregar una aplicación a la laptop de modelo X
def agregar_app_a_modelo(laptops, modelo, app):
    for l in laptops:
        if l.get_modelo() == modelo:
            return l.agregar_app(app)
    return False

# d. Eliminar todas las apps de las laptops con pantalla de ancho Y
def eliminar_apps_por_ancho(laptops, ancho):
    for l in laptops:
        if l.get_pantalla().get_ancho() == ancho:
            l.eliminar_apps()

# f. Ordenar las apps de cada laptop
def ordenar_apps_de_todas(laptops):
    for l in laptops:
        l.ordenar_apps()

# ---------------- Programa principal ----------------
if __name__ == "__main__":
    n = int(input("Cantidad de laptops: "))
    laptops = crear_laptops(n)

    # Ejemplo: cargar algunas apps (c)
    modelo = input("\nModelo al que agregar una app: ")
    nombre = input("Nombre de la app: ")
    tam = int(input("Tamaño de la app: "))
    if agregar_app_a_modelo(laptops, modelo, Aplicacion(nombre, tam)):
        print("App agregada.")
    else:
        print("No se encontró el modelo o la laptop está llena.")

    # b / e
    print("\nLaptop con más aplicaciones:")
    print(laptop_con_mas_apps(laptops))

    # d
    y = int(input("\nAncho Y para eliminar apps: "))
    eliminar_apps_por_ancho(laptops, y)

    # f
    ordenar_apps_de_todas(laptops)
    print("\nLaptops finales:")
    for l in laptops:
        print(l)