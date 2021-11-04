![](https://img.shields.io/badge/Python-v3.9.0-yellow) ![](https://img.shields.io/badge/Selenium-WebDriver-brightgreen) ![](https://img.shields.io/badge/PyUnitReport-Unit%20Testing-brightgreen)

# Selenium Workshop (Work In Progress)
Este repositorio se mantiene en constante actualizacion y es utilizado como tutorial para iniciarse en el uso de Selenium con Python.

## ¿Cómo puedo utilizar este repositorio?
En la rama por default se ubica este README.md con la información general del repositorio. Navegando entre las distintas ramas y el orden numerado podrás encontrar los contenidos del tutorial como los archivos generados. Es recomendable que sigas las instrucciones en el orden de cada una.

## Requisitos
Cualquiera de los siguientes navegadores instalados:
- Firefox
- Safari
- Opera
- Chrome
- Edge

## Descripción
Selenium es un conjunto de herramientas que nos permite automatizar acciones en nuestro navegador, dando pie a crear scripts que ayuden a realizar un proceso específico en forma automática o hacer pruebas en el frontend de un sitio web. Actualmente Selenium puede ser utilizado con distintos lenguajes, sin embargo la mayor parte de la documentación se encuentra hecha para Java y mi deseo es que otras personas que gustan del lenguaje Python comiencen a utilizarlo también PyUnitReport cómo librería para generar reportes de pruebas en formato HTML.

### Agenda
Durante este taller abordaremos los siguientes temas:
#### 1. Para iniciar
- Presentación
- ¿Qué es Selenium?
- Ventajas y desventajas de Selenium

#### 2. Preparación del entorno de trabajo
- Instalación y Descargas
- "Hola, mundo!" en Selenium

#### 3. Comandos básicos
- Unittest
- Selectores
- Localizar elementos

#### 4. Interactual con elementos
- TextBox, Submit Button, SendKeys() y click()
- CheckBox, Form, RadioButton
- Dropdown
- Alert y Pop-Up
- Navegación en la ventana

#### 5. Sincronización de pruebas
- Demora explícita (explicit await)
- Demora implícita (implicit await)

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
- Selenium Remote Control (RC), actualmente en desuso
- WebDriver
- Selenium Grid

Durante su evolución el proyecto Selenium Remote Control se fusionó al de WebDriver.
A partir de este momento nos referiremos a Selenium WebDriver cómo "Selenium".

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

A final de cuentas lo que buscamos con Selenium es imitar o automatizar las acciones de una persona en alguna aplicación web quedando a tu imaginación, lo que puede ir desde ahorrar tiempo en una tarea repetitiva hasta incluso realizar acciones maliciosas cómo una ataque de fuerza bruta.
