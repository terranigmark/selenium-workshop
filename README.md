## 2. Instalación y Descargas
Para trabajar cómodamente con Selenium y Python realizaremos las siguientes instalaciones:
- Python cómo lenguaje de programación en una versión igual o superior a 3.9.
- Selenium 4.0 para automatizar nuestro navegador.
- PyUnitReport cómo generador de reportes en formato HTML.
- ipdb que nos permite hacer debugging e interactuar con nuestra aplicación web en tiempo real.
- Faker para generar datos falsos que pudiéramos ingreasr a una aplicación.
- Browser WebDrivers que enviarán nuestras instrucciones al navegador.

### Instalación de Python
#### Windows
1. Dirigirse a la [sección de descargas en el sitio oficial de Python](https://www.python.org/downloads/)
2. Descargar la versión 3.9 de Python o superior.
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
3. Si obtenemos como respuesta un mensaje cómo `Python 3.9.x` tenemos Python 3 instalado. Recuerda que trabajaremos con una versión igual o superior a Python 3.9.0.

En caso contrario debemos seguir los siguientes pasos:
1. Dirigirse a la [sección de descargas en el sitio oficial de Python](https://www.python.org/downloads/)
2. Ejecutamos el archivo de instalación, dejando las selecciones por defecto y continuado con los pasos de instalación.
3. Validamos si Python está instalado.

### Creando nuestro entorno virtual
Además de Python nos apoyaremos de algunos módulos externos, así que vale la pena crear un entorno virtual para tener todo organizado con `venv`.
Para crearlo ejecutaremos el comando correspondiente:
`python3 -m venv myenv`.
Donde `myenv` es el nombre de nuestro entorno virtual, tú puedes darle otro nombre si así lo deseas.

Para activar nuestro entorno lo hacemos con el comando `source myenv/bin/activate` y así realizar las instalaciones siguientes.
Recuerda que para salir del entorno virtual lo puedes hacer con el comando `deactivate`.

### Instalación de Selenium
1. Abrimos nuestra terminal.
2. Ejecutamos el comando `pip install selenium`.
3. Esto comenzará la instalación del paquete y nos indicará cuando haya finalizado.
4. Verificamos su instalación con el comando `pip freeze`.

### Instalación de PyUnitReport
PyUnitReport es un test runner de pruebas unitarias que genera reportes en HTML. Esto lo hace más fácil de compartir y visualizar para que otras personas puedan analizar nuestros reportes de pruebas.
1. Abrimos nuestra terminal.
2. Ejecutamos el comando `pip install PyUnitReport`.
3. Esto comenzará la instalación del paquete y nos indicará cuando haya finalizado.
4. Verificamos su instalación con el comando `pip freeze`.

### Instalación de ipdb
Esta herramienta exporta funciones para acceder al debugger de IPython permitiendo utilizarlo directamente en nuestro proyecto. Su gran utilidad es la de incluir breakpoints cuando algo falla sin saber su causa y experimentar en ese mismo momento con futuras posibilidades. Dicho de otra forma, pausa la ejecución de nuestra automatización para que interactuemos de manera "manual".
1. Abrimos nuestra terminal.
2. Ejecutamos el comando `pip install idpb`.
3. Esto comenzará la instalación del paquete y nos indicará cuando haya finalizado.
4. Verificamos su instalación con el comando `pip freeze`.

### Instalación de Faker
Este paquete genera datos falsos por nosotros ya sea para bases de datos, documentos o pruebas. Cuenta con proveedores de datos diverses cómo: domicilios, datos personales (nombres, apellido, edad, identificación, etc.), fechas, géneros musicales y muchos más. Además cuenta con la posibilidad de localizar los datos a algún país en específico.
1. Abrimos nuestra terminal.
2. Ejecutamos el comando `pip install Faker` (con mayúscula inicial).
3. Esto comenzará la instalación del paquete y nos indicará cuando haya finalizado.
4. Verificamos su instalación con el comando `pip freeze`.

### Descarga de browser drivers
Cada uno de los navegadores compatibles con Selenium tiene su propio driver que le permite comunicarse con el navegador y debemos descargar el correspondiente según el navegador que utilicemos.
Esta es una lista que redirige a sus sitios de descarga:
- [Chrome](https://sites.google.com/chromium.org/driver/) - La documentación de Chrome incluye la descarga correspondiente.
- [Firefox](https://github.com/mozilla/geckodriver/releases) - Se ubican al final de la página.
- [Internet Explorer](https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver) - Se puede descargar del vínculo con nombre  `Downloads` y seguir las instrucciones de configuración.
- [Safari](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari) - La página indica las instrucciones para utilizar WebDriver.
- [Opera](https://github.com/operasoftware/operachromiumdriver/releases) - La documentación de Opera incluye la descarga correspondiente.
- [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver) - La documentación de Chrome incluye la descarga correspondiente.

## "Hola, mundo!" en Selenium
Estamos listos para hacer nuestra primer prueba con Selenium y validar que funciona correctamente.
Para ello debemos colocar el siguiente código en nuestro editor de texto preferido si estamos utilizando Google Chrome.

**NOTA:**
- Si estás utilizando un navegador distinto deberás cambiar el nombre del mismo después de `webdriver.Chrome`
- La ruta entre comillas de `excecutable_path =`indica la ruta donde se encuentra el driver de tu navegador. Tenerlo en la misma carpeta que tu script es buena ieda.

```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('./chromedriver')
driver = webdriver.Chrome(service = s)
driver.get("https://www.python.org")

driver.quit()
```

Seguro notaste como se abrio una ventana de navegador, cargó el sitio web que le indicamos y se cerró una vez cumplida esta tarea. Esto es porque Selenium tratará de ejecutar las instrucciones asignadas una a una tan rápido como nuestra computadora y conexión a internet lo logre.

Podemos utilizar la librería `time`para colocar pausas explícitas, procurando no abusar de las mismas ya que esto haría nuestra tarea más lenta.

```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('./chromedriver')
driver = webdriver.Chrome(service = s)
driver.get("https://www.python.org")
sleep(3)

driver.quit()
```

El módulo `sleep` de la librería `time`incluirá estas pausas indicando cuantos segundos durará.
