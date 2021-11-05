# 4. Interactúa con elementos
En las aplicaciones y sitios web podrás encontrar muchos elementos de diversos tipos, algunos están a la vista y otros no tanto, sin embargo lo importante es que ya sabes localizarlos. Ahora que sabemos cómo identificar elementos y seleccionarlos podemos interactuar con ellos.

Algunos elementos con los que vas a interactuar son:
- Form (text area, text field e input)
- Checkbox
- Radio button

## Hacer click
Recordarás que en nuestro "Hola, Mundo!" hicimos click a algunos botones, sabes que el método es bastante sencillo: `click().
Ahora inténtalo con el carrito de compras de Madison Island, no olvides que primero debes localizar el elemento y después enviar la interacción.
Tu código deberá quedar algo así:

```
shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")
shopping_cart_icon.click()
```

Esta interacción funciona para enlaces, botones, text fields, dropdowns y todo aquello en lo que haríamos click.

## Inputs
¿Qué hacer si quiero hacer una búsqueda en Madison Island?
La respuesta lógica es colocar un texto en la barra buscadora para encontrar lo que queremos.

Esto es correcto, así que identificaremos ese campo, lo limpiaremos (borrar cualquier contenido que pudiera haber), para después colocar un texto e iniciar la búsqueda.

Inspeccionando el elemento encontramos sus atributos y valores:
`<input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">`

Usaremos su `id` para ubicarlo:
`search_bar = driver.find_elements_by_id("id-search-field")`

En caso de que haya algún texto en el TextBox podemos borrarlo con el método `clear()`
`search_bar.clear()`

## Enviar texto
Para ingresar texto a un Textbox debemos importar un módulo específico para ello:
`from selenium.webdriver.common.keys import Keys`

El método para enviar texto es `send_keys()` sobre un elemento en el que nos ubiquemos:
`search_bar.send_keys("salt shaker")`

También podemos "presionar" cualquier tecla con el método `send_keys(Keys.TECLA)`.
Solo debemos reemplazar la palabra `TECLA` por otra.
Por ejemplo `send_keys(Keys.ARROW_DOWN)`.

El código de nuestro método debe verse así más o menos:

```
import unittest
from time import sleep
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UsingUnnittest(unittest.TestCase):

    def setUp(self):
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = s)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com')
        driver.implicitly_wait(10)

    def test_click_shopping_cart(self):
        driver = self.driver
        shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")
        shopping_cart_icon.click()
        sleep(2)

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        search_field.clear()
        search_field.send_keys("salt_shaker")
        search_field.send_keys(Keys.RETURN)
        sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity = 2)
```

## Llenando un formulario de registro de cuenta
Ok, las últimas interacciones que aprendiste te permitirán aplicarlas a un sin número de casos así que vamos a ponernos un poco más serios y automatizaremos la creación de una cuenta en el e-commerce, pues esto es algo que hacen los usuarios ¿cierto?

Prepara un nuevo archivo de pruebas, crea tus métodos ya conocidos más uno nuevo de prueba que llamaremos `test_new_user()` y las acciones a realizar son las siguientes:
1. Localizar el botón "ACCOUNT" y darle click.
2. Se abrirá menú desplegable donde haremos click al enlace que dice "Log In".
3. Verás una pantalla donde podemos iniciar sesión o crear una cuenta nueva. Haz click en el botón que dice "CREATE AN ACCOUNT".
4. Nos llevará a un formulario que pedirá algunos datos para crear una cuenta los cuales solo es cuestión de localizarlos y enviar texto.
5. ¿Ves ese checkbox para suscribirse al newsletter? También le daremos click. Inspecciona el elemento, indagando verás que hay una etiqueta `input` de tipo `checkbox` a la cual hay que hacer click.
6. Por último haremos click en el botón que dice "Register".

Utiliza los locators que desees mientras hayas logrado el objetivo: crear una cuenta nueva. El archivo `madison_new_user.py` te dará una idea de cómo puedes hacerlo.

¿Lo lograste? ¡Felicidades! Ahora podrás crear un ejercito de bots, pero eres buena persona y se que no lo harás... de verdad no haga eso.

Te habrás dado cuenta de que cada vez que corras la automatización se enviarán los mismos datos una y otra vez, por supuesto quieres utilizar datos distintos y es hora de que Faker entre a la acción.

## Simulando datos aleatorios con Faker
Ya tienes instalado este módulo y utilizarlo es muy sencillo pero aún así recomiendo que leas su [documentación](https://faker.readthedocs.io/en/master/).

Primeramente importaremos el módulo Faker de la siguiente forma:
`from faker import Faker`

Antes de nuestra clase de prueba haremos una instancia local de algún país, Estados Unidos y en inglés funciona bien para evitar inconvenientes con acentos y caracteres especiales:
`fake = Faker('en_US')`

Los métodos de Faker son bastante intuitivos y leer su documentación será de gran ayuda. Por ejemplo, así se vería el envío de un nombre falso:
`first_name.send_keys(fake.first_name_female())`

Espera... ¿`send_keys` puede enviar métodos, funciones o variables?
¡La respuesta es "Sí"! Así que ahora es tu turno para hacer lo mismo con el resto de envío de datos al formulario.

¿Has pensado en que pasaría si antes de enviar los datos intentas con otros diferentes? No lo pienses más y hagamos pruebas sobre las pruebas.

## Congela el tiempo e interactúa con ipdb
En este punto ipdb también ya está instalado y podemos importarlo pero ojo porque debemos llamarlo en una línea antes de donde queremos nuestro breakpoint. Por ahora hágamoslo una vez llegamos al formulario y antes de enviar cualquier dato quedando así:

```
...
create_account_button = driver.find_element(By.LINK_TEXT, 'CREATE AN ACCOUNT')
create_account_button.click()
import ipdb; ipdb.set_trace()
first_name = driver.find_element(By.ID, 'firstname')
first_name.send_keys(fake.first_name_female())
...
```

La forma en que llamamos a ipdb es algo diferente, comenzando porque el método `set_trace()` indica el breakpoint donde se lanzará el debugger. Corramos nuestra automatización y veamos que sucede al llegar a ese punto.

Veremos que en la terminal se a abierto el debugger de IPython. Acá existen distintos comandos pero nos centraremos en los esenciales:
- Continue: Si presionas la tecla `C` el programa seguirá avanzando con normalidad 
- Next: Si presionas la tecla `N` el programa ejecutará la línea que indica en el debugger, pausará y esperará la siguiente instrucción. Esto permite avanzar línea por línea.
- Interacciones "en vivo": Desde el debuger de IPython también puedes enviar cualquier comando de Python o Selenium. Por ejemplo localizar elementos e interactuar con ellos ¿por qué no intentas localizar el campo de email y enviar algún dato?

Con ipdb me encanta experimentar antes de escribir código en mis archivos, así puedo darme una idea de las posibilidades que tengo y seguir mi camino ¡Es simplemente genial!

## Interactuando con más elementos
Los sitios y aplicaciones web son más que simples formularios con campos y botones, así que veamos los siguientes elementos con los que podemos interactuar:
- Dropdown
- Alert
- Pop-up

### Dropdown
Los dropdowns son estos menús tan útiles que se pueden expander y colapsar en los que encontramos opciones para elegir una.

Crearemos un nuevo archivo donde para interactuar con ellos debemos importar un nuevo submódulo de Selenium:
`from selenium.webdriver.support.ui import Select`

Nos encargaremos de utilizar el dropdown para elegir un idioma distinto en nuestro e-commerce de prueba. Para identificar un elemento como dropdown debemos pasar su localizador como argumento dentro del método `Select()` de la siguiente forma:
`language_selector = Select(driver.find_element(By.ID, 'select-language'))`

Así tendremos 3 formas para elegir las opciones de nuestro dropdown:
- `select_by_visible_text()`: usando como argumento el texto tal cual se muestra en la lista de opciones.
- `select_by_index()`: usando como argumento el índice de los elementos en la lista, en este caso se inicia por el índice 0.
- `select_by_value()`: dentro de la etiqueta del elemento encontraremos un atributo `value`, su valor es el que podemos utilizar cómo argumento para seleccionar dicha opción

Para los primeros dos casos nuestro código sería así:
```
...
language_selector = Select(driver.find_element(By.ID, 'select-language'))
language_selector.select_by_visible_text('German')
sleep(1)
language_selector = Select(driver.find_element(By.ID, 'select-language'))
language_selector.select_by_index(1)
...
```

### Alert y Pop-Up
Hoy en día no es común que un sitio web utilice alerts o pop-ups directamente desde JavaScript, aún así puede suceder que hagas frente a un sitio que sí lo haga y mejor saber cómo manejarlos.

Creemos un nuevo archivo con la estructura que ya hemos estado manejando y un método de prueba llamado `test_compare_products_removal()` el cual tendrá las siguientes acciones:
1. Ubicar la barra de búsqueda y realizar la búsqueda por el término "tee".
2. Hacer click en el link "Add to compare" de alguno de los artículos.
3. Esto hará que aparezca un menú de comparación al costado. Si hacemos click en la opción "Clear All" aparecerá un alert preguntando si deseamos eliminar la lista de comparación.

Cuando aparece el alert podemos cambiar el foco del navegador hacia este con el comando `driver.switch_to_alert()` y es buena idea almacenarlo en una variable para interactuar así que podemos pensar en algo así:
`alert = driver.switch_to_alert()`

Tenemos dos opciones: aceptar o cancelar. Afortunadamente también comandos específicos para cada una:
```
# Aceptar
alert.accept()
# Cancelar
alert.dismiss()
# Extraer el texto del alert
alert.text
```

Si queremos aceptar el eliminar la lista entonces esa parte del código debe quedar así:
```
...
driver.find_element(By.CLASS_NAME, 'link-compare').click()
driver.find_element(By.LINK_TEXT, 'Clear All').click()
alert = driver.switch_to.alert()
alert.accept()
...
```

## Navegando cómo haría un usuario
Hay una serie de acciones que forman parte de lo que haría un usuario cómo el ir a la página anterior/siguiente, refrescar el navegador, etc. Realmente no hay mucha ciencia detrás de ello por lo que solo listaremos los comandos y te encargarás de probarlos:

### Navegación
- `driver.get('http://demo-store.seleniumacademy.com')`: se dirige a la URL que indiquemos entre comillas.
- `driver.current_url`: obtiene la URL de la barra del navegador.
- `driver.back()`: simular presionar el botón "atrás" del navegador.
- `driver.forward()`: simular presionar el botón "adelante" del navegador.
- `driver.refresh()`: refresca la página del navegador donde te encuentras.
- `driver.title`: obtiene el título de la página donde se encuentra el navegador.

### Manejando ventanas y pestañas
Las ventanas y pestañas son elementos independientes para Selenium por lo que cada vez que abras una nueva deberás indicar que deseas trabajar sobre la misma.
- `driver.current_window_handle`: indicas que trabajarás en la ventana actual, es buena idea almacenarla en una variable.
- `driver.switch_to.new_window('tab')`: abre una nueva pestaña y cambia el foco a esta.
- `driver.switch_to.new_window('window')`: abre una nueva ventana y cambia el foco a esta.
- `driver.close()`: cierra la pestaña actual.
- `driver.quit()`: cierra el navegador y cierra la sesión del mismo.


### Manejo de la ventana
También es posible controlar las ventanas y manipularlas para cambiar su tamaño, maximizarla o minimizarla. Estos son algunos métodos:
- `driver.get_window_size().get("width")`: obtiene el anchode la ventana.
- `driver.get_window_size().get("height")`: obtiene el alto de la ventana.
- `driver.set_window_size(width, height)`: cambia el tamaño de la ventana a los valores pasados cómo argumentos.
- `driver.get_window_position().get('x')`: obtiene la posición de la ventana en su eje X.
- `driver.get_window_position().get('y')`: obtiene la posición de la ventana en su eje Y.
- `driver.set_window_position(X, Y)`: ubica la ventana en la posición de las coordenadas pasadas cómo argumento.
- `driver.maximize_window()`: maximiza la ventana.
- `driver.minimize_window()`: minimiza la ventana.
- `driver.fullscreen_window()`: pasa la ventana a modo de pantalla completa.

En los archivos de la rama encontrarás los archivos correspondientes con sugerencias de cómo realizar lo visto hasta ahora ¡Prueba, experimenta y sigue probando!
