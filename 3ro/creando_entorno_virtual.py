
# Es necesario crear un entorno virtual para trabjar con proyectos
# y que otros no salgan destruidos o con diferentes versiones.
# 1. Crear un entorno virtual para que no afecte a las otras
# 2. Entrar en un entorno virtual, donde se debe especificar
# la versión de Python y las bibliotecas que necesitan.
# 3. Desarrollar el programa

# Para crear un entorno virtual, llama al módulo 'venv'
# 1. Ir al directorio donde guardamos el proyecto
# 2. Use el comando 'python -m venv env'

# Se crearán automáticamente algunos directorios.
# Include, Lib, Scripts, pyvenv.cfg

# NO COLOCAR LOS ARCHIVOS EN LA CARPETA 'env'
# COLOCAR LOS ARCHIVOS EN UNA CARPETA LLAMADA 'src' O SIMILAR.
# /env
# /src
#   programa.py

# Ya tenemos el entorno virtual. pero no hemos empezado a utilizarlo
# debemos activarlo mediante un script <activate>
# \env\Scripts\activate
# source env/bin/activate -> Bash

# Cuando se llama a <activate> cambia el símbolo del sistem.
# (env)
# (env) -> path/to/project

# Instalar un paquete mediante 'pip'
# El comando 'pip' usa el índice de paquetes de Python, o PyPi
# Para instalar un paquete, ejecute 'pip install' desde el cmd env.
# 'pip install python-dateutil'

# Se descargará e instlará 'dateutil'
# Un paquete para analizar el formato de archivo '.yml.'
# /env
#  /lib
#   /dateutil

# para ver que paquetes están instalados en el entorno virtual
# se ejecuta 'pip freeze'
# este comando genera una lsita de paquetes instalados en el terminal.

# python-dateutil==2.8.2
# six==1.16.0

# para asegurarse de que estos paquetes solo existen en el entorno virtual
# intente salir de ese entorno mediante una llamada: <deactivate>

# Cambia el símbolo de sistema en el terminal. Ya no hay un <env>

# Si se ejecuta 'pip freeze', se verá una lista más larga de dependencias.


# También puede usar los siguientes comandos para instalar un paquete:
# Tener un conjunto de archivos en la máquina e instalar desde ese origen:
# cd <to where the package is on your machine>
# python3 -m pip install .

# Instalar desde un repositorio de GitHub que
# proporciona control de versiones:
# git+https://github.com/your-repo.git

# Instalar desde un archivo comprimido:
# python3 -m pip install package.tar.gz


#  Uso de un paquete instalado
# Asegúrese de que tiene un directorio para los archivos.
#  Se recomienda llamar al directorio src y agregar un archivo
# Python de punto de entrada denominado app.py.
# Ahora agregue código para llamar a dateutil:
##
# from datetime import *
# from dateutil.relativedelta import *
# now = datetime.now()
# print(now)

# now = now + relativedelta(months=1, weeks=1, hour=10)

# print(now)
##

# Ejecute la aplicación:
# python app.py

# El resultado debe parecerse a este:
# 2023-01-30 17:04:24.799976
# 2023-03-07 10:04:24.799976
