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
- Instalación y Descarga
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

## Instalación
### Instalación de Python
#### Windows
1. Dirigirse a la [sección de descargas en el sitio oficial de Python](https://www.python.org/downloads/)
2. Descargar la versión 3.6 de Python o superior.
3. Abrir el ejecutable de instalación.
4. En la primer pantalla marcar la opción "Add Python 3.x to PATH.
5. Elegir "Install now".
6. Marcar todas las casillas en la opción "Optional features".
7. Abrimos el cmd de windows, escribimos `python`y presionamos la tecla 'ENTER'
