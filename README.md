# Papermill Ejemplo 4

<img src="https://th.bing.com/th/id/R.6920b7a1d49c34ccb3ed8e8c66fa89d5?rik=IsdEqlRjKLbOVQ&pid=ImgRaw&r=0" width="500">

[![Python](https://img.shields.io/badge/python-3.11.2-blue)](https://www.python.org/)
[![Papermill](https://img.shields.io/badge/papermill-2.4.0-green)](https://papermill.readthedocs.io/en/latest/)
[![Pandas](https://img.shields.io/badge/pandas-1.5.3-yellow)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.2.2-orange)](https://scikit-learn.org/)
[![Seaborn](https://img.shields.io/badge/seaborn-0.12-red)](https://seaborn.pydata.org/)

## Índice

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Notebook Java](#notebook-java)
  - [IJava](#ijava)
- [Notebook Julia](#notebook-julia)
  - [Crear un ambiente virtual en Julia](#crear-un-ambiente-virtual-en-julia)
  - [Instalar dependencias en el ambiente virtual](#instalar-dependencias-en-el-ambiente-virtual)
  - [Activación de dependencias de ambiente virtual](#activación-de-dependencias-de-ambiente-virtual)
- [Contribución](#contribución)

## Descripción

Este proyecto es un ejemplo de cómo usar papermill como data pipeline para un caso de un proyecto de machine learning. Papermill es una herramienta que permite ejecutar y parametrizar notebooks de Jupyter. El proyecto consta de cuatro notebooks:

- validacion_datos.ipynb: donde se hace una validación de los datos de entrada y se detectan posibles anomalías o valores faltantes.
- preprocesamiento.ipynb: donde se hace un preprocesamiento de los datos, como normalización, codificación, selección de características, etc.
- modelo.ipynb: donde se entrena un modelo de machine learning usando scikit-learn y se evalúa su rendimiento.
- prediccion.ipynb: donde se hace una predicción sobre nuevos datos usando el modelo entrenado y se muestra el resultado.

Este ejemplo es un submódulo de otro git que contiene todos los ejemplos desarrollados.

## Instalación

Para ejecutar este proyecto se necesita tener instalado Python 3.6 o superior y las siguientes librerías:

- papermill 2.X o superior
- pandas 1.X
- numpy 1.X
- scikit-learn 1.X
- seaborn 0.12 o superior

Se recomienda usar un ambiente virtual para instalar las librerías y evitar conflictos con otras versiones. Se puede crear un ambiente virtual **(para Windows)** usando los comandos:

Crea un ambiente virtual llamado venv
```bash
python -m venv venv
```
Activa el ambiente virtual
```bash
venv/scripts/activate
```
Instala las librerías y las actualiza si es necesario
```bash
pip install -r requirements.txt --upgrade
```

En caso de usar Linux o Mac, los comandos cambian un poco su sintaxis. Se recomenda revisar como crear ambientes virtuales en dichos OS si se desea ejecutar el código en alguna distribución de Linux o Mac.

Para instalar el proyecto desde el repositorio que lo contiene como submódulo, se puede usar el comando git clone con la opción --recurse-submodules. Por ejemplo, se podría usar este comando:

```bash
git clone --recurse-submodules https://github.com/LeandroNardiTaligent/Papermill-Ejemplos
```

Adicional a eso, se necesita tener instalado Java y Julia para correr las notebooks asociadas a esos lenguajes.

## Notebook Java

Lo primero es tener instalado Java en tu sistema. Para eso, hay que instalar el JDK de Java. Existen varios proveedores del servicio, siendo Oracle su creador, como Microsoft y hay un JDK open source disponibilizado por la comunidad. 
Para evitarse una demanda millonaria por Oracle (ya que sus términos y condiciones son muy controversiales), se recomienda usar openJDK, el cual es la versión OpenSource de Java disponibilizado por la comunidad.

Para eso, hay que descargarse el openJDK de https://openjdk.org/. Para este ejemplo, se usó el JDK 19, pero es compatible con la JDK 20, que a momento de creación de este ejemplo, es el último releases.

Los pasos de instalación son los siguientes:

1. Descarga OpenJDK desde el sitio oficial: https://jdk.java.net/.
2. Extrae el archivo zip descargado en una carpeta accesible y segura en tu sistema.
3. Agrega la carpeta bin de la instalación de OpenJDK a la variable de entorno PATH.
4. Crea la variable de entorno JAVA_HOME y establece su valor a la ruta donde se descomprimió el JDK (opcional).
5. Abre una consola y ejecuta el comando `java --version` para confirmar que la instalación ha quedado correcta.

Cuando ejecute el comando, debería visualizar un print similar en consola:

```bash
openjdk 19.0.2 2023-01-17
OpenJDK Runtime Environment (build 19.0.2+7-44)
OpenJDK 64-Bit Server VM (build 19.0.2+7-44, mixed mode, sharing)
```
### IJava

Una vez instalado el JDK de Java, el siguiente paso es instalar el kernel de Java. Para este ejemplo, se utilizó IJava, pero existen otros, como Jython. Los kernel de Java, suelen ser en general desarrollados por terceros.
En este caso, la manera de instalar IJava se encuentra en el siguiente repositorio: https://github.com/jxmlee/IJava

Para esta instalación, se usó la forma de instalación Install pre-built binary, explicada en el repositorio con el siguiente comando:

```bash
python install.py --prefix='path-to-root\Papermill\Ejemplo 4\venv'
```

## Notebook Julia

Al igual que con Java, lo primero que hay que hacer es instalar Julia. Los pasos de instalación son los siguientes:


Abre tu navegador web y ve al sitio oficial de Julia en .
1. Descargar la versión de Julia que deseas instalar en el sitio oficial de Julia (https://julialang.org/downloads/). Recomendamos descargar la versión más reciente estable.
2. Ejecuta el archivo de instalación descargado de Julia.
3. En en instalador, seleccionar la opción `Add to Path`. De lo contrario, habrá que anadir manualmente a Julia como variable de entorno en windows, como se hizo con openJDK.
4. Hacer clic en "Instalar" para comenzar la instalación de Julia en tu sistema.

### Crear un ambiente virtual en Julia

1. Abrir una terminal en Windows y posicionarse en la ruta donde se quiera crear el ambiente virtual
2. Ejecuta el siguiente comando para abrir la consola de Julia:
```bash
julia
```
3. Una vez en la consola de Julia, ingresa el siguiente comando para entrar al modo de administración de paquetes de Julia: `]`
4. Ejecuta el siguiente comando para crear un nuevo ambiente virtual (reemplaza "myenv" con el nombre que desees para tu ambiente virtual): 
```bash
activate myenv
```
Ahora estás dentro de tu nuevo ambiente virtual y puedes instalar paquetes y dependencias específicos en él.

### Instalar dependencias en el ambiente virtual

1. Asegúrate de estar dentro del ambiente virtual que creaste en el paso anterior. Para eso, hay que estar en la ruta donde se creó y activarlo usando el siguiente comando (reemplaza "myenv" con el nombre de tu ambiente virtual): 
```bash
activate myenv
```
Si uno no se encuentra en la ruta, Julia creará un ambiente nuevo distinto al anterior.

2. Ejecuta el siguiente comando para instalar una dependencia en el ambiente virtual de Julia (reemplaza "NOMBRE_DEL_PAQUETE" con el nombre del paquete que deseas instalar):
```bash
add NOMBRE_DEL_PAQUETE
```
Julia descargará e instalará la dependencia en el ambiente virtual que creaste

Para esta notebook, los paquetes utilizados fueron:

- DataFrames v1.5.0
- ScikitLearn v0.7.0
-  XLSX v0.9.0
- DelimitedFiles

**IMPORTANTE**: Para que esto funcione, en el ambiente principal de Julia hay que instalar el paquete `IJulia`.

### Activación de Dependencias de ambiente virtual

Una vez hecho esto, hay que decirle a Julia que dependencias usar. Para eso, hay que modificar el archivo `kernel.json` de la siguiente manera:
```json
{
  "display_name": "Julia 1.8.5",
  "argv": [
    "C:\\Users\\TALIGENT\\AppData\\Local\\Programs\\Julia-1.8.5\\bin\\julia.exe",
    "-i",
    "--color=yes",
    "--project=C:\\Users\\TALIGENT\\test\\Papermill\\Ejemplo 4\\julia_venv\\Project.toml",
    "C:\\Users\\TALIGENT\\.julia\\packages\\IJulia\\6TIq1\\src\\kernel.jl",
    "{connection_file}"
  ],
  "language": "julia",
  "env": {},
  "interrupt_mode": "message"
}
```
En `--project=`, hay que agregar la ruta donde se creó el ambiente virtual, junto con el archivo `Project.toml`. El archivo `kernel.json`, se encuentra en la carpeta julia-1.8. La ruta de la misma la proporciona la shell de Julia cuando se instala IJulia en el ambiente principal.
Luego, la ruta donde se creó IJulia, puede moverse a cualquier lugar y colocarla en la carpera del proyecto, por ejemplo.

## Uso

Para usar este proyecto, se deben seguir los siguientes pasos:

1. Ejecutar el archivo `datos_simulados.py`. Este archivo genera un conjunto de datos sintéticos llamado `dataset.xlsx` para el problema de regresión lineal y lo guarda en la carpeta `input/`. Si la carpeta `input/` no existe, el archivo la creará automáticamente.
2. Ejecutar el notebook `main.ipynb`. Este notebook se encarga de llamar a los otros notebooks con los parámetros adecuados mediante papermill. Los resultados de cada notebook se guardan en archivos con el sufijo _output.ipynb en la misma carpeta donde se encuentran las notebooks.
3. Finalizada la ejecución de `main.ipynb`, se crea el archivo `predicciones.xlsx` en la carpeta `output/`. Este archivo contiene las predicciones del modelo de regresión lineal sobre nuevos datos generados artificialmente. Si la carpeta `output/` no existe, el notebook la creará automáticamente.

## Contribución

Este proyecto es solo un ejemplo didáctico y no tiene fines comerciales. Si quieres contribuir a mejorar el código o la documentación, puedes hacer un fork del repositorio y enviar un pull request con tus cambios.

<br>

## <center> Made with &#x2764; for Advanced Analitycs</center>

<br>

<center><a href="https://www.taligent.com.ar/es/"><img src="https://www.taligent.com.ar/wp-content/uploads/2022/09/logo-e1664303535353-300x66.png" width='200'></a></center>
