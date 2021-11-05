# 5. Sincronización de pruebas
Cómo bien sabes la actividad en el DOM ocurre de forma asíncrona, lo que puede representar un reto para Selenium ya que no hace un seguimiento activo del estado del DOM y es común que aparezcan errores relacionados a que no se encontró un elemento porque aún no estaba visible o el sitio web tardó en cargar más de lo estimado.

Por ejemplo, supongamos que hay un formulario en el cual el botón "Enviar" no aparece sino hasta que llenamos todos los campos requeridos y queremos hacer click en dicho botón sin haber cumplido la condición anterior. Esto generaría un error donde dicho botón no puede ser localizado a pesar de que sabemos de su existencia y lo encontramos en el código del DOM ¿entonces qué podemos hacer al respecto?

Lo más sencillo y, no mejor práctica, es utilizar el método `sleep` del módulo `time` para colocar una espera de "n" segundos hasta que se cumpla dicha condición pero esto trae inconvenientes cómo extender la duración de la prueba y no tener precisión en que ese sea el tiempo requerido al ser un proceso asíncrono. Para solucionarlo Selenium nos ofrece tres distintos tipos de demoras:
- Explicit wait
- Implicit wait
- Fluent wait

## Explcit wait (demoras explícitas)
Las demoras explícitas funcionan deteniendo el proceso de ejecución de la automatización y continúan hasta que se cumpla una condición indicada. Dicha condición es llamada con una frecuencia hasta que dicho tiempo expira, por lo que se llama de forma continua a dicha condición en tanto siga retornando un valor falso.

Veamos un ejemplo en donde nos dirigimos a la sección de accesorios en Madison Island y ejecutamos una demora explícita hasta que se logra identificar que el título del sitio es `Jewelery - Accesories` y que el H1 de esta página es `Jwelery`:

```
# Importamos el submódulo WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

# Dentro de nuestro método de prueba incluimos una función obtener el title del sitio
def title_jewelery(driver):
            return driver.title
            
# Después vamos al sitio en cuestión, definimos la demora explícita para 5 segundos,
# localizamos el H1 y hacemos un assert para validar que es el texto que buscamos.
driver.get('http://demo-store.seleniumacademy.com/accessories/jewelry.html')
WebDriverWait(driver, 5).until(title_jewelery)
el = driver.find_element(By.TAG_NAME, "h1")
self.assertEqual(el.text, 'JEWELRY')
```

Así cómo utilizamos una función anónima podemos también pasar el elemento de manera explícita. Recuerda que para este caso definimos una espera máxima de 5 segundos y si durante la misma no se logra cumplir la condición tendremos que esperar a que pase este tiempo ¿te imagina que sucede si estamos en un sitio que se conecta a terceros y debemos esperar 2 o 3 minutos a una petición?

### Expected conditions (condiciones esperadas)
Podrás imaginarte que las condiciones para que una demora explícita funcione puedes ser diversas, lo cual es cierto y además pueden variar de un lenguaje a otro. En Python las más comunes son:
- title_is
- title_contains
- presence_of_element_located
- visibility_of_element_located
- visibility_of
- presence_of_all_elements_located
- text_to_be_present_in_element
- text_to_be_present_in_element_value
- frame_to_be_available_and_switch_to_it
- invisibility_of_element_located
- element_to_be_clickable
- staleness_of
- element_to_be_selected
- element_located_to_be_selected
- element_selection_state_to_be
- element_located_selection_state_to_be
- alert_is_present

Veamos un ejemplo sencillo de cómo es implementarlas:
```
# Importamos también el submódulo expected_conditions
from selenium.webdriver.support import expected_conditions as EC

# Definimos una demora explícita de hasta 10 segundos esperando a que se pueda hacer click en el elemento.
el = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'firstname')))
```

Madison Island es un sitio bastante sencillo que en general no requiere de demoras explícitas o condiciones esperadas, sin embargo es buena idea que practiques con estas.

## Implicit wait (demoras implícitas)
Las demoras implícitas llaman al DOM de forma constante para encontrar un elemento durante el tiempo que le indicamos, volviéndose bastante útil cuando no hay una condición específica y lo único que debemos esperar esa que cargue el sitio o aplicación web.

La sintaxis es bastante sencilla, veamos un ejemplo:
```
driver.implicitly_wait(15)
```

## Fluent wait (demoras fluidas)
Estas demoras definen un tiempo máximo de tiempo en el que esperarán por una condición, al mismo tiempo la frecuencia con la que se verifica dicha condición. Son utilizadas principalmente para ignorar tipos específicos de excepciones cuando se buscan elementos, por ejemplo `NoSuchElementException`.

Un ejemplo sería el siguiente:
```
wait = WebDriverWait(driver, 10, frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
el = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id="form-validate"]/div[2]/button")))
```

Podemos observar algunas cosas interesantes:
- Primero que el método `WebDriverWait` lo almacenamos en una variable para reusarlo en la búsqueda del elemento, muy útil.
- Dentro del mismo método estamos definiendo varias cosas: nuestro driver, el tiempo de espera, la frecuencia o número de veces que se hará dicha espera y las excepciones que ignoraremos.
- Por último todo se coloca en la identificación de un elemento donde estamos también realizando esta espera fluida.

Hasta este momento tienes ya suficiente conocimiento para automatizar prácticamente cualquier sitio, por supuesto hay muchas cosas que aprender de Selenium y hasta que actualicemos este repositorio te invito a que revises la documentación oficial.
