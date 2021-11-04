# 3. Comandos Básicos
## Unit Testing
Realizar pruebas unitaras en tus automatizaciones es una gran ayuda, ya que de esta forma puedes saber que está 
ocurriendo en cada paso (caso de prueba/test case), obtener un resultado de cada una y tomar decisiones al respecto.

En esta ocasión te apoyarás de Unittest y PyUnitReport.

### Unittest
Unittest, también conocido cómo PyUnit, es un módulo de testing para pruebas unitarias inspirado en JUnit y es común encontrar este tipo de frameworks en otros lenguajes donde comparten características similares. Este es un gran complemento, considerando que Selenium no brinda información adicional sobre lo que hacemos.

Con Unittest podemos crear pruebas que se componen las siguientes partes:
- Método `setUp`: Definimos instrucciones que se realizarán antes de nuestras pruebas. Aquí es donde prepararemos nuestro entorno, generalmente configurar y crear la instancia de nuestro navegador "limpia".
- Métodos de prueba: Será la parte del código que evualará Unittest, debemos definirla cómo métodos, llevarán el prefijo `test` y dentro de esta las acciones que queremos evaluar. Por ejemplo `def test_sending_text(self):`
- Método `tearDown`: Definimos instrucciones que se realizarán después de nuestras pruebas. Cómo puede ser un mensaje para comunicar que hemos terminado con las pruebas y cerrar la instancia del navegador.
- `unittest.main()` - Esta es una interfaz de de línea de comandos que nos mostrará detalles cómo la cantidad de tests ejecutados y el tiempo de evaluación. Se coloca al final de nuestro código cómo si llamáramos al método `main`.

Al final lizar las pruebas obtenemos un reporte de resultados.
Los resultados de las pruebas pueden ser tres distintos:
- **OK** - La prueba terminó de forma satisfactoria.
- **FAIL** - La prueba no terminó de forma satisfactoria, se levantará la excepción que hayamos asignado.
- **ERROR** - La prueba no terminó exitosamente y está fuera de nuestras excepciones.

#### Implementando Unittest
Llamaremos a Unittest por medio de una clase en la cual colocaremos la subclase `unittest.TestCase`.
Suponiendo que nuestra clase de prueba se llame `UsingUnittest` quedaría así: `class UsingUnittest(unittest.TestCase):`.

Ahora definiremos nuestro `método setUp` con el ejemplo que hemos trabajado:
```
def setUp(self):
    s = Service('./chromedriver')
    self.driver = webdriver.Chrome(service = s)
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
  self.driver.quit()
  
if __name__ == '__main__':
  unittest.main(verbosity = 2)
```

Siempre es buena idea comunicar a través de algún medio que estás terminando la prueba, tomar una pausa y después cerrar la instancia del navegador para evitar exceso en el uso de recursos de tu equipo. 
Por otro lado la bandera `verbosity` con el parámetro `2` nos otorgará más detalles en el reporte de Unittest.

#### Caso de prueba listo
Hasta este punto tu código debe de verse así:
```
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class UsingUnnittest(unittest.TestCase):

    def setUp(self):
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = s)

    def test_get_ptyhon_website(self):
        driver = self.driver
        driver.get("https://www.python.org")

    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2)
```

### PyUnitReport
Este es un test runner, el cual se encargará de analizar nuestra clase y casos de prueba para ensamblarlos en un reporte escrito en HTML. Mostrará los resultados con datos relevantes cómo fecha en que se generó, tiempo de ejecución, status de los casos de prueba, códigos de colores para su fácil identificación y también detalles de los mismos.

#### Implementando PyUnitReport
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
    unittest.main(
        verbosity = 2,
        testRunner = HTMLTestRunner(
            output = 'report',
            report_name = 'python_org_report',
            failfast = True))
```

# Localizar elementos
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
- XPath

### XPath
XPath es el lenguaje utilizado para identificar nodos en XML, extendiendo su uso a identificar elementos en HTML. Estos pueden ser absolutos o relativos.

Hay una discusión entre si esta debería ser nuestra última opción para ubicar a los elementos, por ejemplo cuando no hay una forma explícita de identificarlos por medio de alguna de las opciones anteriores, o si debería ser la primera por cuestiones de seguridad ya que no está exponiendo algún dato de la aplicación web.

Una forma rápida de obtenerlo es haciendo click en el elemento dentro del inspector de elementos y elegir copiar su XPath absoluto o relativo.

## Encontrar elementos

Al ver el botón "About" de https://www.python.org con el inspector de elementos vemos que tiene la siguiente estructura:
`<a href="/about/" title="" class="">About</a>`

Y su XPath es el siguiente:
- Absoluto
`/html/body/div/header/div/nav/ul/li[1]/a`
- Relativo
`//*[@id="about"]/a`

Podemos apreciar el tipo de etiqueta HTML, sus atributos y valores de los atributos.

La forma en que procedemos acceder a los elementos es con el método `find_element(By.SELECTOR)` y contamos con distintas opciones:
- class_name
- css_selector
- id
- link_text
- name
- partial_link_name
- tag_name
- xpath

Este botón podemos seleccionarlo escribiendo `find_element(By.LINK_TEXT, "About")` y lo almacenaremos en la variable `about_link` en caso de que deseemos usarlo.

Si queremos hacer click en el podemos usar el método `click()`

Nuestro código ahora ser verá así:
```
import unittest
from time import sleep
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class UsingUnnittest(unittest.TestCase):

    def setUp(self):
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = s)

    def test_get_ptyhon_website(self):
        driver = self.driver
        driver.get('https://www.python.org')
        button_about = driver.find_element(By.LINK_TEXT, 'About')
        button_about.click()

    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(
        verbosity = 2,
        testRunner = HTMLTestRunner(
            output = 'report',
            report_name = 'python_org_report',
            failfast = True))
```
### Probando más selectores
Ahora ubiquemos más elemenos del home utilizando otros selectores de manera que tu método `test_get_python()` debe quedar así:
```
def test_get_ptyhon_website(self):
        driver = self.driver
        driver.get('https://www.python.org')
        driver.find_element(By.CLASS_NAME, 'tier-1')
        driver.find_element(By.CSS_SELECTOR, '#community')
        driver.find_element(By.ID, 'downloads')
        driver.find_element(By.LINK_TEXT, 'About')
        driver.find_element(By.NAME, 'q')
        driver.find_element(By.TAG_NAME, 'h1')
        driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[1]/a')
```

## Poniendo en práctica lo aprendido
¿Funcionó tu script? ¡Genial! Ya sabes ubicar elementos por sus distintos selectores, hacer click en ellos y recuerda que puedes almacenarlos en variables.
Tu siguiente reto será practicar con un sitio diseñado para automatizaciones, es MUY IMPORTANTE que siempre lo hagas en aplicaciones designadas para ello pues el hacer automatizaciones en producción trae sus consecuencias.

### Madison Island, tu e-commerce de práctica
[Madison Island](http://demo-store.seleniumacademy.com) es un sitio demo con el que puedes experimentar libremente, notarás que se trata de un e-commerce y tiene todos los elementos de uno real. Si por algún motivo no puedes acceder al sitio puedes probar con los siguientes que, aunque tengan distinta estructura, siguen siendo e-commerces:
- [Madison Island, sitio alternativo 1](http://magento-demo.lexiconn.com)
- [Madison Island, sitio alternativo 2](http://ecommerce-solution.info)
- [Madison Island, sitio alternativo 3](http://demo.onestepcheckout.com)
- [MyStore](http://automationpractice.com/index.php)
- [Swag Labs](https://www.saucedemo.com)

¡Recuerda que cuando ingreses información procura que sea información falsa/dummy y no datos verdaderos!

### El reto
Crea un script de pruebas donde tengas los métodos `setUp` y `tearDown`que ya hemos utilizado pero además los siguientes:
- `test_search_text_field' que ubique el campo de búsqueda a través de su id.
- `test_search_text_field_by_name' que ubique el campo de búsqueda a través de su atributo `name`.
- `test_search_text_field_by_class_name' que ubique el campo de búsqueda a través de su nombre de clase.
- `test_search_text_field_button' que ubique el botón de la barra de búsqueda con forma de 🔍 por su nombre clase.
- `test_count_promo_banners` que ubique el elemento que contiene los 3 cuadros de promociones ("Home & Decor", "Shop Private Sales" y "Travel Gear") por su nombre de clase. Después ubica las 3 imágenes que representa cada banner en solo localizador, deberás utilizar `find_elements` (en plural).
- `test_vip_promo`que ubique una de las imágenes del carrusel por su XPath.
- `test_shopping_cart_icon` que ubique el ícono del carrito de compras por su selector de CSS.

¿Cómo te fue? En los archivos de esta rama encontrarás una propuesta de solución, si lo hiciste de una forma diferente también está bien.
En la siguiente sección prepararás assertions y una test suite.
