Este es un proyecto básico hecho con Django que permite al usuario completar un formulario sobre un escrito proporcionado para que se rellene automaticamente y quede listo para firmar.
El formulario sin rellenar lo dejo adjuntado en el repositorio.

Características

  Formulario funcional que recoge datos del usuario.
  Plantilla HTML para una interfaz sencilla.
  Estructura clara para escalar el proyecto con más campos y validaciones.

Requisitos

  Python 3.10 o superior
  pip
  Git (para clonar el repositorio)
  Django (instalable vía pip)
  (Opcional) Entorno virtual
  Instalación y ejecución

Clona este repositorio:

  git clone https://github.com/JIMBus88/Formulario.git

  cd mi_proyecto_django

  Crea un entorno virtual y actívalo:

  python -m venv env

  En windows: env\Scripts\activate

  En Mac/Linux: source env/bin/activate

Instala Django:

  pip install Django

Ejecuta el servidor de desarrollo:

  python manage.py runserver

Abre tu navegador y visita:

  http://127.0.0.1:8000/

Ahí podrás ver y probar el formulario, se rellena y en el botón de generar PDF, te abre el archivo PDF con el texto escrito.
