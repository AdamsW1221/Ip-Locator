import sys, time
from colorama import Style, Fore, init
init()
import json
import requests

class localizadorIP:
    def __init__(self) -> int:
        
        self.ip = self.obtener_ip_publica()
        self.autenticacion = '06bdbdff-2e70-48b9-8b33-4e8565bfddac'
        self.urlApi = 'https://ipfind.co/?auth=' + self.autenticacion + '&ip=' + self.ip;
        self.peticion = requests.get(self.urlApi)
        self.respuesta = json.loads(self.peticion.content)
    
    def menu(self):
        
        primera_opcion = Fore.GREEN + '\n1. ~Localizar persona~ \n'
        segunda_opcion = Fore.RED + '2. ~Ver mis Datos~ \n'
        self.control_flujo(primera_opcion, tiempo=0.05)
        self.control_flujo(segunda_opcion, tiempo=0.05)
        
        elegir_opcion = int(input(Fore.BLUE + '\n--> '))       
        
        if elegir_opcion == 1:
            self.ip = input(str(Style.BRIGHT + Fore.RED + "Ingresa la Ip: " + Fore.GREEN ))
            self.ejecutar_operacion()
            
        elif elegir_opcion == 2:
            self.ejecutar_operacion()
    
    def ejecutar_operacion(self):  
        try:
            self.manejo_datos('-La Victima Es De: ', 'country')
            self.manejo_datos('-Continente: ', 'continent')
            self.manejo_datos('-De La Ciudad De: ', 'city')
            self.localizacion()
            self.manejo_datos('-Codigo de Region: ', 'region_code')
            self.manejo_datos('-Codigo Postal: ', 'postal_code')
            self.manejo_datos('-Idioma: ', 'languages')
            self.manejo_datos('-Moneda: ', 'currency')
        except:
            self.control_flujo('Error en la operación...')
    
    def obtener_ip_publica(self):
        try:
            response = requests.get("https://httpbin.org/ip")
            data = response.json()
            ip_publica = data['origin']
            return ip_publica
        except Exception as e:
            return str(e)

    def manejo_datos(self, respuesta, dato):
        
        if dato == 'languages':
            datos = Style.BRIGHT + Fore.BLUE + f"{respuesta}" + Fore.GREEN,  self.respuesta[dato]
        else:
            datos = Style.BRIGHT + Fore.BLUE + f"{respuesta}" + Fore.GREEN + self.respuesta[dato]
            
        self.control_flujo(datos)
        print('\n')
        time.sleep(0.1)
        
    def localizacion(self):
        
        latitud = self.respuesta['latitude']
        longitud =self.respuesta['longitude']
        coordenadas = Style.BRIGHT , Fore.BLUE, "Latitud " , Fore.GREEN , latitud , Fore.BLUE , " Longitud " , Fore.GREEN , longitud
        
        print(Style.BRIGHT + Fore.RED + 'La ultima Localización GPS Fue')
        self.control_flujo(coordenadas)
        print('\n')
        print(Style.BRIGHT + Fore.BLUE + "Localización --> " , Fore.GREEN , latitud ,  longitud)
        print('\n')
        
    def control_flujo(self, datos, tiempo=0.1):
        for iterar in datos:
            sys.stdout.flush()
            print(iterar, end='')
            time.sleep(tiempo)
    
    def mostrar_logo(self):
        logo = Fore.RED +'''
          ▄    ▄▄▄▄▄▄▄    ▄
         ▀▀▄─▄█████████▄─▄▀▀
             ██─▀███▀─██
           ▄─▀████▀████▀─▄
         ▀█    ██▀█▀██    █▀
        \n
        '''
        nombre = Style.BRIGHT + Fore.WHITE +'~IP-LOCATOR~ \n'
    
        self.control_flujo(logo, tiempo=0.01)
        self.control_flujo(nombre, tiempo=0.03)
        

localizador = localizadorIP()
localizador.mostrar_logo()
localizador.menu()