# gemini-api
Primera actividad: conexión al api gemini

## Introducción

Este repositorio contiene el script de prueba de configuración de un entorno virtual y la conección con el API de Gemini.

## Requisitos de Instalación Antes de ejecutar el script:

1. *Python: Asegúrese de tener Python3 instalado en su sistema.

Puede descargarlo desde [python.org](https://www.python.org/).Puede verificar la versión de Python instalada en el sistema utilizando el siguiente comando en la línea de comandos o terminal, dependiendo de tu sistema operativo:

*Para Windows:* 
    
```bash
python --version
python -V 
```
  
*Para Linux o macOS:*
     
```bash
python3 --version
python3 -V 
```

Estos comandos deberían mostrar la versión de Python instalada en tu sistema.
Asegúrate de tener Python instalado y configurado en tu PATH para que estos comandos funcionen correctamente. 

2. *Variables de Entorno de google AI Studio que se deben configurar:*  Antes de ejecutar los scripts .py asegúrese de configurar su archivo .env con su token de google AI Studio: 

      - `GEMINI_API_KEY`: Token/clave del API de Gemini.

 Esta variable es esencial para la integración con el API google gemini AI. Es importante configurarla correctamente para asegurar el funcionamiento adecuado del scripts. Si no dispone de un token de usuario en esta herramienta, puede consultar haciendo click en el botón de  [crea o visualiaza una clave de API de Gemini](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419) 

## Ejecución de los scripts

Para ejecutar los scripts, debe seguir estos pasos:

1. *Clonar Repositorio:*     
a. Comience clonando el repositorio en su máquina local mediante el siguiente comando:
```bash  
git clone https://github.com/AlejandraBenavidez05/gemini-api.git
```
   

b. Ubiquese en el directorio gemini-api/

2. *Crear entorno Virtual (recomendado):*
Se recomienda utilizar un entorno virtual para evitar conflictos con las dependencias de otros proyectos.   
 
a. Puede crear un entorno virtual en el directorio del proyecto con el siguiente comando:

```bash
python3 -m venv venv 
``` 

      
b. Para activar el entorno virtual ejecute el comando adecuado según su sistema operativo.

  - En Windows (cmd): `venv\Scripts\activate.bat`

  - En Windows (PowerShell): `.\venv\Scripts\Activate.ps1`

  - En macOS y Linux: `source ./venv/bin/activate`

3. *Instalación de Dependencias:*

 Instale las dependencias del proyecto utilizando el siguiente comando:
 ```bash
pip install -r requirements.txt
```
Esto instalará todas las bibliotecas necesarias para ejecutar el script. 

4. *Ejecución del script de python:* 

Para ejecutar los scripts, utilice el siguiente comando:
```bash
python3 nombre_del_script.py
```
