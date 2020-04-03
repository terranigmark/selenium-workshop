![](https://img.shields.io/badge/Python-v3.7-yellow) ![](https://img.shields.io/badge/Selenium-WebDriver-brightgreen) ![](https://img.shields.io/badge/PyUnitReport-Unit%20Testing-brightgreen)

# Selenium Workshop (Work In Progress)
Este repositorio se mantiene en actualizacion.
Repositorio utilizado durante el taller presencial en Platzi Bogotá como tutorial para iniciarse en el uso de Selenium con Python y PyUnitReport.

## ¿Quieres más ejemplos de Selenium?
Si ya hiciste este tutorial y quieres ver más ejemplos aplicados de Selenium + Python, te invito que visites este repositorio: https://github.com/linnk99/the-internet

## Requisitos
Cualquiera de los siguientes navegadores instalados:
- Firefox
- Internet Explorer
- Safari
- Opera
- Chrome
- Edge

## Descripción
Selenium es un framework que nos permite automatizar acciones en nuestro navegador, dando pie crear scripts que ayuden a realizar un proceso específico en forma automática o hacer pruebas en el frontend de un sitio web. Actualmente Selenium puede ser utilizado con distintos lenguajes, sin embargo la mayor parte de la documentación se encuentra hecha para Java y mi deseo es que otras personas que gustan del lenguaje Python comiencen a utilizarlo también PyUnitReport cómo librería para generar reportes de pruebas en HTML.

### Agenda
Durante este taller abordaremos los siguientes temas:
- Presentación
- ¿Qué es Selenium?
- Ventajas y desventajas de Selenium
- Instalación y Descargas
- "Hola, mundo!" en Selenium
- Unittest
- Selectores
- Encontrar elementos
- TextBox, Submit Button, SendKeys() y click()

## Presentación
Mi nombre es Héctor Vega, soy un apasionado a los videojuegos, las artes marciales y la cerverza artesanal. Aprendí a programar mientras trabajaba en Recursos humanos de TI, fue cuando descubrí Python y no tenía la menor idea de a donde me llevaría esto.

## ¿Qué es Selenium?
Selenium es un framework open source de automatización para el navegador web, compatible con diversos lenguajes de programación:
- Java
- C# 
- PHP
- Perl
- Ruby
- Python

La suite de Selenium consta de 4 herramientas diferentes:
- Selenium Integrated Development Environment (IDE)
- Selenium Remote Control (RC)
- WebDriver
- Selenium Grid

Durante su evolución el proyecto Selenium Remote Control se fusionó al de WebDriver.
A partir de este momento nos referiremos a WebDriver cómo "Selenium".

## Ventajas y Desventajas
### Ventajas
- Fácil instalación
- Comunicación directa con el navegador
- Interacción realista y precisa con el navegador
- No necesita de componentes externos
- Compatible con diversos navegadores
- Posee una comunidad robusta
- Cuenta con estándares de buenas prácticas

### Desventajas
- Requiere de cierto conocimiento en programación
- No soporta nuevos navegadores tan rápido
- No posee algún mecanismo de reportes
- Debe generar una nueva instancia de navegador en cada uso
- Es lento comparado con otros frameworks de testing
- La mayoría de los recursos se limitan a Java

## Instalación y Descargas
### Instalación de Python
#### Windows
1. Dirigirse a la [sección de descargas en el sitio oficial de Python](https://www.python.org/downloads/)
2. Descargar la versión 3.6 de Python o superior.
3. Abrir el ejecutable de instalación.
4. En la primer pantalla marcar la opción "Add Python 3.x to PATH.
5. Elegir "Install now".
6. Marcar todas las casillas en la opción "Optional features".
7. Abrimos el cmd de windows, escribimos `python`y presionamos la tecla `ENTER`
8. En caso de mostrarse el intérprete de Python, entonces estamos listos para continuar 🎉

#### Linux y Mac OS
Python suele estar instalado en estos sistemas operativos y podemos validarlo de la siguiente forma:
1. Abrimos la terminal de comandos.
2. Escribimos `python3 --version` y presionamos la tecla ´ENTER´
3. Si obtenemos como respuesta un mensaje cómo `Python 3.7.3` tenemos Python 3 instalado.

En caso contrario debemos seguir los siguientes pasos:
1. Dirigirse a la [sección de descargas en el sitio oficial de Python](https://www.python.org/downloads/)
2. Ejecutamos el archivo de instalación, dejando las selecciones por defecto y continuado con los pasos de instalación.
3. Validamos si Python está instalado.

### Instalación de Selenium
Los pasos para Windows, Linux y Mac OS son los mismos.
1. Abrimos nuestra terminal.
2. Ejecutamos el comando `pip3 install selenium`.
3. Esto comenzará la instalación del paquete y nos indicará cuando haya finalizado.

### Instalación de PyUnitReport
PyUnitReport es un test runner de pruebas unitarias que genera reportes en HTML. Esto lo hace más fácil de compartir y visualizar para que otras personas puedan analizar nuestros reportes de pruebas.
Los pasos para Windows, Linux y Mac OS son los mismos.
1. Abrimos nuestra terminal.
2. Ejecutamos el comando `pip3 install PyUnitReport`.
3. Esto comenzará la instalación del paquete y nos indicará cuando haya finalizado.

### Descarga de browser drivers
Cada uno de los navegadores compatibles con Selenium tiene su propio driver que le permite comunicarse con el navegador y debemos descargar el correspondiente según el navegador que utilicemos.
Esta es una lista que redirige a sus sitios de descarga:
- [Firefox](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0) - Se ubican al final de la página.
- [Internet Explorer](https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver#required-configuration) - Se puede descargar del vínculo con nombre  `Downloads` y seguir las instrucciones de configuración.
- [Safari](https://developer.apple.com/documentation/webkit/about_webdriver_for_safari) - La página indica las instrucciones para utilizar WebDriver.
- [Opera](https://github.com/operasoftware/operachromiumdriver/releases) - La documentación de Opera incluye la descarga correspondiente.
- [Chrome](https://sites.google.com/a/chromium.org/chromedriver/) - La documentación de Chrome incluye la descarga correspondiente.
- [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads) - La documentación de Chrome incluye la descarga correspondiente.

## "Hola, mundo!" en Selenium
Estamos listos para hacer nuestra primer prueba con Selenium y validar que funciona correctamente.
Para ello debemos colocar el siguiente código en nuestro editor de texto preferido si estamos utilizando Opera.

**NOTA:**
- Si estás utilizando un navegador distinto deberás cambiar el nombre del mismo después de `webdriver.Opera`
- La ruta entre comillas de `excecutable_path =`indica la ruta donde se encuentra el driver de tu navegador. Tenerlo en la misma carpeta que tu script es buena ieda.

```
from selenium import webdriver

driver = webdriver.Opera(executable_path = "./operadriver")
driver.get("https://www.python.org")

driver.close()
```

Seguro notaste como se abrio una ventana de navegador, cargó el sitio web que le indicamos y se cerró una vez cumplida esta tarea. Esto es porque Selenium tratará de ejecutar las instrucciones asignadas una a una tan rápido como nuestra computadora y conexión a internet lo logre.

Podemos utilizar la librería `time`para colocar pausas explícitas, procurando no abusar de las mismas ya que esto haría nuestra tarea más lenta.

```
from selenium import webdriver
from time import sleep

driver = webdriver.Opera(executable_path = "./operadriver")
driver.get("https://www.python.org")

sleep(3)

driver.close()
```

El módulo `sleep` de la librería `time`incluirá estas pausas indicando cuantos segundos durará.

## Unit Testing
Realizar pruebas unitaras en tus automatizaciones es una gran ayuda, ya que de esta forma puedes saber que está 
ocurriendo en cada paso (caso de prueba/test case), obtener un resultado de cada una y tomar decisiones al respecto.

En esta ocasión te apoyarás de Unittest y PyUnitReport.

### Unittest
Unittest, también conocido cómo PyUnit, es un framework de testing para pruebas unitarias inspirado en JUnit y es común encontrar este tipo de frameworks en otros lenguajes donde comparten características similares. Este es un gran complemento, considerando que Selenium no brinda información adicional sobre lo que hacemos.

Con Unittest podemos crear pruebas que se componen las siguientes partes:
- Método `setUp` - Definimos instrucciones que se realizarán antes de nuestras pruebas. Aquí es donde prepararemos nuestro entorno, generalmente configurar y crear la instancia de nuestro navegador.
- Métodos de prueba - Estas serán la parte del código que evualará Unittest, debemos definirla como funciones, llevarán el prefijo `test_` y dentro de esta las acciones que queremos evaluar. Por ejemplo `def test_sending_text(self):`
- Método `tearDown`- Definimos instrucciones que se realizarán después de nuestras pruebas. Cómo puede ser un mensaje para comunicar que hemos terminado con las pruebas y cerrar la instancia del navegador.
- `unittest.main()` - Esta es una interfaz de de línea de comandos que nos mostrará detalles cómo la cantidad de tests ejecutados y el tiempo de evaluación. Se coloca al final de nuestro código cómo si llamáramos al método `main`.

Al final lizar las pruebas obtenemos un reporte de resultados.
Los resultados de las pruebas pueden ser tres distintos:
- **OK** - La prueba terminó de forma satisfactoria.
- **FAIL** - La prueba no terminó de forma satisfactoria, se levantará la excepción que hayamos asignado.
- **ERROR** - La prueba no terminó exitosamente y está fuera de nuestras excepciones.

### Implementando Unittest
Llamaremos a Unittest por medio de una clase en la cual colocaremos la subclase `unittest.TestCase`.
Suponiendo que nuestra clase de prueba se llame `UsingUnittest` quedaría así: `class UsingUnittest(unittest.TestCase):`.

Ahora definiremos nuestro `método setUp` con el ejemplo que hemos trabajado:
```
def setUp(self):
    self.driver = webdriver.Opera(executable_path = "./operadriver")
    driver = self.driver
```

Continuamos con nuestro método de prueba donde evaluaremos la apertura del sitio web:
```
def test_get_ptyhon_website(self):
    driver = self.driver
    driver.get("https://www.python.org")
```

**NOTA:**
La variable `driver` del método `setUp` tiene un alcance dentro de si misma, por lo que debemos asignarla nuevamente a una variable dentro del método `test_get_ptyhon_website` para poderla utilizar.
De la misma forma todas las funciones de nuestro caso de prueba deben iniciar con la palabra `test` para ser reconocidas por Unittest

Terminamos llamando al método `tearDown` y nuestro método `main`:
```
def tearDown(self):
  print('Browser is about to close...')
  sleep(3)
  self.driver.close()
  
if __name__ == '__main__':
  unittest.main(verbosity = 2)
```

Siempre es buena idea comunicar a través de algún medio que estás terminando la prueba, tomar una pausa y después cerrar la instancia del navegador para evitar exceso en el uso de recursos de tu equipo. 
Por otro lado la bandera `verbosity` con el parámetro `2` nos otorgará más detalles en el reporte de Unittest.

### Caso de prueba listo
Hasta este punto tu código debe de verse así:
```
from selenium import webdriver
from time import sleep

class UsingUnnittest(unittest.Testcase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")
        driver = self.driver
        
    def test_get_ptyhon_website(self):
        driver = self.driver
        driver.get("https://www.python.org")
        
    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.close()
  
if __name__ == '__main__':
  unittest.main(verbosity = 2)
```

### PyUnitReport
Este es un test runner, el cual se encargará de analizar nuestra clase y casos de prueba para ensamblarlos en un reporte escrito en HTML. Este mostrará los resultados con datos relevantes cómo fecha en que se generó, tiempo de ejecución, status de los casos de prueba, códigos de colores para su fácil identificación y también detalles de los mismos.

### Implementando PyUnitReport
Primero debemos importar el test runner con el comando `from pyunitreport import HTMLTestRunner`.

Podemos implementar PyUnitReport fácilmente si lo colocamos en el método `unittest.main()` utilizando la palabra reservada `testRunner` de la siguiente forma:
`unittest.main(testRunner = HTMLTestRunner)`

Cuentas con tres parámetros, donde el único obligatorio es `output`, para especificar el directorio donde se guardará el reporte. También puedes utilizar el parámetro `report_name` para dar un nombre a tu reporte, o por defecto colocará la fecha y hora en que se generó. Si quieres utilizar el modo "failfast" puedes hacerlo colocando el parámetro `failfast` con valor `True`

La función main debe ser cómo esta entonces:
`unittest.main(testRunner = HTMLTestRunner(output = 'Reports', report_name = 'python-website-report', failfast = True))`

Si tu código es idéntico al siguiente entonces tendrás una carpeta llamada `Reports` con un archivo HTML de nombre `python-website-test` y toda la información de tu prueba hasta ahora:
```
from selenium import webdriver
from time import sleep
from pyunitreport import HTMLTestRunner

class UsingUnnittest(unittest.Testcase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")
        driver = self.driver
        
    def test_get_ptyhon_website(self):
        driver = self.driver
        driver.get("https://www.python.org")
        
    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.close()
  
if __name__ == '__main__':
  unittest.main(testRunner = HTMLTestRunner(output = 'Reports', report_name = 'python-website-report', failfast = True))
```

## Selectores
Dentro de una interfaz gráfica en la web podemos ubicar los elementos de la misma respecto a sus selectores como:
- ID
- Nombre
- Texto del link
- Selector de CSS
- Texto interior

También podemos ubicar a los elementos como parte del DOM por:
- ID del elemento
- Nombre del elemento

### XPath
XPath es el lenguaje utilizado para identificar nodos en XML, extendiendo su uso a identificar elementos en HTML. Estos pueden ser absolutos o relativos.

Cómo última opción deberíamos ubicar a los elementos por su XPath, por ejemplo cuando no hay una forma explícita de identificarlos por medio de alguna de las opciones anteriores.

Una forma rápida de obtenerlo es haciendo click en el elemento dentro del inspector de elementos y elegir copiar su XPath absoluto o relativo.

## Encontrar elementos

Al ver el botón "About" de https://www.python.org con el inspector de elementos vemos que tiene la siguiente estructura:
`<a href="/about/" title="" class=" current_item selected selected">About</a>`

Y su XPath es el siguiente:
- Absoluto
`/html/body/div/header/div/nav/ul/li[1]/a`
- Relativo
`//*[@id="about"]/a`

Podemos apreciar el tipo de etiqueta HTML, sus atributos y valores de los atributos.

La forma en que procedemos acceder a los elementos es con el método `find_element_by` y contamos con diversas opciones:
- class_name
- css_selector
- id
- link_text
- name
- partial_link_name
- tag_name
- xpath

Este botón podemos seleccionarlo escribiendo `find_element_by_link_text(¨About¨)` y lo almacenaremos en la variable `about_link` en caso de que deseemos usarlo.

Si queremos hacer click en el podemos usar el método `click()`

Nuestro código ahora ser verá así:
```
from selenium import webdriver
from time import sleep

driver = webdriver.Opera(executable_path = "./operadriver")
driver.get("https://www.python.org")

about_link = driver.find_element_by_link_text("About")
about_link.click()

sleep(3)

driver.close()
```

## click(), TextBox y send_keys()
Ahora que sabemos cómo identificar elementos y seleccionarlos podemos interactuar con ellos.

### click()
Si queremos hacer click en el botón `About` podemos usar el método `click()`.
Específicamente el método sería `about_link.click()`, nuestro código ahora se vería así e ingresaremos a donde nos lleve el botón:

```
from selenium import webdriver
from time import sleep

driver = webdriver.Opera(executable_path = "./operadriver")
driver.get("https://www.python.org")

about_link = driver.find_element_by_link_text("About")
about_link.click()

sleep(3)

driver.close()
```

### TextBox
¿Qué hacer si quiero hacer una búsqueda en el sitio de Python?
La respuesta lógica es colocar un texto en la barra buscadora para encontrar lo que queremos.

Esto es correcto, así que identificaremos ese TextBox, colocaremos un texto e iniciaremos la búsqueda.

Inspeccionando el elemento encontramos sus atributos y valores:
`<input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">`

Usaremos su `id` para ubicarlo:
`search_bar = driver.find_elements_by_id("id-search-field")`

En caso de que haya algún texto en el TextBox podemos borrarlo con el método `clear()`
`search_bar.clear()`

### send_keys()

Para ingresar texto a un Textbox debemos importar un módulo específico para ello:
`from selenium.webdriver.common.keys import Keys`

El método para enviar texto es `send_keys()` sobre un elemento en el que nos ubiquemos:
`search_bar.send_keys(¨dictionaries¨)`

También podemos "presionar" cualquier tecla con el método `send_keys(Keys.TECLA)`.
Solo debemos reemplazar la palabra `TECLA` por otra.
Por ejemplo `send_keys(Keys.ARROW_DOWN)`.

Nuestro código debe verse así ahora:

```
#Librerías y módulos que importamos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Crear una instancia del navegador almacenada en una variable para fácil uso
driver = webdriver.Opera(executable_path = "./operadriver")
#Dirigimos el navegador a https://www.python.org
driver.get("https://www.python.org")

#Identificamos el botón de 'About' por el texto del enlace y hacemos click en el
about_link = driver.find_element_by_link_text("About")
about_link.click()

#Identificamos la barra de búsqueda por su id, borramos lo que haya en la misma,
#escribimos la palabra 'dictionaries' y "presionamos" la tecla 'ENTER'
search_bar = driver.find_elements_by_id("id-search-field")
search_bar.clear()
search_bar.send_keys(¨dictionaries¨)
search_bar.send_keys(Keys.ENTER)

#Creamos una pausa por 3 segundos
sleep(3)

#Cerramos la instancia del navegador
driver.close()
```

Nuesto código cada vez va tomando forma y además incluimos comentarios para que podamos tener más claridad sobre lo que hacemos.

## Unittest
Unittest, también conocido cómo PyUnit, es un framework de testing para pruebas unitarias inspirado en JUnit y es común encontrar este tipo de frameworks en otros lenguajes donde comparten características similares. Este es un gran complemento, considerando que Selenium no brinda información adicional sobre lo que hacemos.

Con Unittest podemos crear pruebas que se componen las siguientes partes:
- Método `setUp` - Definimos instrucciones que se realizarán antes de nuestras pruebas. Aquí es donde prepararemos nuestro entorno, generalmente configurar y crear la instancia de nuestro navegador.
- Métodos de prueba - Estas serán la parte del código que evualará Unittest, debemos definirla como funciones, llevarán el prefijo `test_` y dentro de esta las acciones que queremos evaluar. Por ejemplo `def test_sending_text(self):`
- Método `tearDown`- Definimos instrucciones que se realizarán después de nuestras pruebas. Cómo puede ser un mensaje para comunicar que hemos terminado con las pruebas y cerrar la instancia del navegador.
- `unittest.main()` - Esta es una interfaz de de línea de comandos que nos mostrará detalles cómo la cantidad de tests ejecutados y el tiempo de evaluación. Se coloca al final de nuestro código cómo si llamáramos al método `main`.

Al final lizar las pruebas obtenemos un reporte de resultados.
Los resultados de las pruebas pueden ser tres distintos:
- **OK** - La prueba terminó de forma satisfactoria.
- **FAIL** - La prueba no terminó de forma satisfactoria, en caso de que lancemos alguna excepción.
- **ERROR** - La prueba no terminó exitosamente y está fuera de nuestras excepciones.

### Implementando Unittest
Llamaremos a Unittest por medio de una clase en la cual colocaremos la subclase `unittest.TestCase`.
Suponiendo que nuestra clase se llame `UsingUnittest` quedaría así: `class UsingUnittest(unittest.TestCase):`.

Ahora definiremos nuestro `método setUp` con el ejemplo que hemos trabajado:
```
def setUp(self):
    self.driver = webdriver.Opera(executable_path = "./operadriver")
```

Continuamos con nuestro método de prueba donde evaluaremos la apertura del sitio web y buscar el término "dictionaries":
```
def test_search_dictionaries(self):
    #Dirigimos el navegador a https://www.python.org 
    self.driver = driver
    driver.get("https://www.python.org")

    #Identificamos el botón de 'About' por el texto del enlace y hacemos click en el
    about_link = driver.find_element_by_link_text("About")
    about_link.click()

    #Identificamos la barra de búsqueda por su id, borramos lo que haya en la misma,
    #escribimos la palabra 'dictionaries' y "presionamos" la tecla 'ENTER'
    search_bar = driver.find_elements_by_id("id-search-field")
    search_bar.clear()
    search_bar.send_keys(¨dictionaries¨)
    search_bar.send_keys(Keys.ENTER)
```

**NOTA:** La variable `driver` del método `setUp` tiene un alcance dentro de si misma, por lo que debemos asignarla nuevamente a una variable dentro del método `test_search_dictionaries` para poderla utilizar.

Terminamos llamando al método `tearDown` y nuestro método `main`.

```
def tearDown(self):
  print('Browser is about to close...')
  sleep(3)
  self.driver.close()
  
if __name__ == '__main__':
  unittest.main()
```

## Código final
Llegado a este punto nuestro código debe verse de la siguiente forma:

WORK IN PROGRESS

## ¿Te funcionó el código?
Me encantaría que colocaras una estrella a este repositorio si te fue de utilidad 😄
