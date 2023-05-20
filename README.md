PARA GENERAR UNA CARPETA BACK
primero hacemos la carpeta del proyecto, dentro de esa carpeta hacemos una back y una front
abrimos VSC
terminal
virtualenv venv
.\venv\Scripts\activate PARA ACTIVAR EL ENTORNO VIRTUAL
aparece en la ruta (venv) al comienzo
PARA ACTIVAR VESRION DE PYTHON y trabajar con la misma version de jose
pyenv install 3.10.6 (la version que sea)
pyenv global  para verificar cual es la que esta funcionando
pyenv global 3.10.6 (la version nuevamente) para definirla como eleccion 

PARA JOSE => pip install -r requirements.txt

si al querer cargar datos en base de datos da error en vez del codigo enorme 
elimino la carpeta migratiosn y voy con 
flask db init (no hace falta volver a hacerlo porque ya esta iniciado)

para el resto en vez de pipenv (solo si hay cambios en el modelo de tabla)
flask db migrate
flask db upgrade

para que se cree el requirements.txt que me dice que necesoto tener instalado para que el proyecto funcione ok
PARA AGOS => pip freeze > requirements.txt
cada vez que instalamos una nueva libreria de python eliminamos el requirements.xt y volvemos con 
pip freeze > requirements.txt
