![](https://img.shields.io/badge/Python-v3.7-yellow) ![](https://img.shields.io/badge/Selenium-WebDriver-brightgreen)

# Selenium Workshop
Repositorio utilizado durante el taller presencial en Platzi Bogotá.

## Requisitos
Cualquiera de los siguientes navegadores instalados:
- Firefox
- Internet Explorer
- Safari
- Opera
- Chrome
- Edge

## Descripción
Selenium es un framework que nos permite automatizar acciones en nuestro navegador, dando pie crear scripts que ayuden a realizar un proceso específico en forma automática o hacer pruebas en el frontend de un sitio web. Actualmente Selenium puede ser utilizado con distintos lenguajes, sin embargo la mayor parte de la documentación se encuentra hecha para Java y mi deseo es que otras personas que gustan del lenguaje Python comiencen a utilizarlo también.

Durante este taller abordaremos los siguientes temas:
- Presentación
- ¿Qué es Selenium?
- Ventajas y desventajas de Selenium
- Instalación y Descargas
- "Hola, mundo!" en Selenium
- Selectores
- Encontrar elementos
- TextBox, Submit Button, SendKeys() y click()
- Checkbox y Radio Button

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
1. Abrimos nues

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
XPath es el lenguaje utilizado para identificar nodos en XML, extendiendo su uso a identificar elementos en HTML.

Cómo última opción deberíamos ubicar a los elementos por su XPath, por ejemplo cuando no hay una forma explícita de identificarlos por medio de alguna de las opciones anteriores.
