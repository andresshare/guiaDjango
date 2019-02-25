# 👍 GUIA DJANGO 
![N|Solid](https://i.ibb.co/71MqnJN/formulariodjango.png)

En esta guia se creara un proyecto simple. Un formulario de registro con el cual
 se entiendera el flujo de trabajo de django en su version 1.11.4

Es importante aclarar  que la instalacion funcionara para  los tres sistemas operativos windows.linux y Mac


Usare django con python 3.6 o superior,si usted es un usuario nuevo con python es apropiado saber que las versiones de python 2 y 3 son diferentes 

# Instalacion de python 3

Revisa este enlace para la instalacion de python

[https://tutorial.djangogirls.org/es/python_installation/]


### INSTALAR VIRTUALENV

Aca dejo un enlace para la instalacion de virtualenv [https://tutorial.djangogirls.org/es/django_installation/]

o puede seguir esta guia para linux Debian

```
sudo pip3.6 install virtualenv

```
###  CREAR VIRTUALENV

```
virtualenv [nombredelentorno] -p python3.6
```

Active el entorno ingresando a la carpeta 

>  bin/source activate

despues ejecute este comando
```
pip install Django==1.11.4
```

🔴  #INICIANDO EL PROJECTO


 Django nos ofrece estos comandos 

```
 django-admin startproject [nombre del projecto]
 django-admin startapp [nombredelapp]
```

Como primer paso abrimos la consola de comandos y creamos el nombre al proyecto 

```
django-admin-startproject webpage
```

Creamos el app del projecto,dajngo es modular nos permiter tener n aplicaciones dentro de un proyecto

```
django-admin startapp home
```

Estructura del proyecto

```

+---(webpage)
|
|
+----[home]
  |---(migrations)
  |-----__init__.py
  |----admin.py
  |----app.py
  |----forms.py
  |----models.py
  |----test.py
  |----views.py
|---(static)
|
|
|---(templates)
    |-----home.html
+----[webpage]
  |-----(migrations)
  |-----__init__.py
  |----settings.py
  |----urls.py
  |----forms.py
  |----test.py
  |----wsgi.py    


```
!! Es necesarion crear la carpeta templates/ y su archivo home.html

# CONFIGURAR EL SETTINGS.PY

Nos ubicamos en settings.py :


```
+----[webpage]
  |-----(migrations)
  |-----__init__.py
  |----settings.py ***AQUI***
  |----urls.py
  |----forms.py
  |----test.py
  |----wsgi.py    


```


# Registrar el app

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #APPS
    'home'
]

```


## Modificar en la zona de TEMPLATES lo siguiente


```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # **MODIFICAMOS LA RUTA**,para que django entienda que debe dirigirse a la carpeta templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')]    
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


## Django, en su servidor de pruebas no reconoce directamente[static] 

Nos ubicamos al final de las lineas de codigo de  settings.py copiamos y pegamos esta linea
```
STATICFILES_DIRS=(os.path.join(BASE_DIR, 'static'),)

```


# CREAR TABLA con datos

Modificar los datos es facil en django creamos las tablas y sus relaciones en el 
archivo models.py
```
+---(webpage)
|
|
+----[home]
  |---(migrations)
  |-----__init__.py
  |----admin.py
  |----app.py
  |----forms.py
  |----models.py *Aqui*
  |----test.py
  |----views.py
```
Abrimos el archvio de models.py



# 💻 TABLA DE REGISTRO

creamos la tabla en models.py 

**Contacto** -- (from Contacto)
+ |-- nombre: models.ChartField
+ |-- correo: models.Email.Field
+ |-- mensaje: Textfield


*home/models.py*

```
from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(max_length=15)
    correo = models.EmailField(blank=True)
    mensaje = models.TextField()

    def __unicode__(self):
        return self.nombre

```


# 💻 $SHELL

Django nos ofrece una consola interactiva que nos permite modicar los registros de la BD

```
 python manage.py shell
```
# 

### CREAR Y GUARDAR DATOS

```
 from home.models import Contacto
 creardato = Contacto(name='cristiano',correo='cristianoronaldo@futbol.com',mensaje='saludo a django ')
 creado.save()
```
### IDENTIFICAR UN SOLO REGISTRO CREADO

```
 Contacto.id
 Contacto.correo
```
### LISTAR DATOS

```
 from home.models import Contacto
 guardo_datos=Contactoobjects.all()
 for l in guardo_datos:
 print(l.nombre)
```
### OBTENER DATOS POR EL NUMERO DE REGISTRO

```
s dato_numero_registro = Contacto.objects.get(id=2)
 print(dato_numero_registro.nombre)
```


# 🔑 MOSTRAR UN REGISTRO A UNA VISTA DEL TEMPLATE

# [1]  **webpage** /urls.py

Nos ubicamos en webpage/urls.py

``` 
from django.contrib import admin
from django.conf.urls import url, include



urlpatterns = [

    url(r'^$', include('home.urls', namespace='home', app_name='home')),
    url('admin/', admin.site.urls),
]

``` 

Creamos un archivo en urls.py en home


``` 
+----[home]
  |---(migrations)
  |-----__init__.py
  |----admin.py
  |----app.py
  |----forms.py
  |----models.py 
  |----test.py
  |----urls.py  *Archivo creado*
  |----views.py
```


``` 
from django.conf.urls import url
from home import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),

]

``` 



# [2] HOME/views.py

## !!! importar el modelo

> **from .models import Contacto**

``` 
 

from django.urls import reverse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from home.models import Contacto
from .forms import FormularioContacto


class Home(CreateView):
    model = Contacto
    form_class = FormularioContacto
    success_url = reverse_lazy('home:home')
    template_name = 'home.html'

    def get_success_url(self):

        return reverse('home:home')

```


# [3] TEMPLATES/home.html
## Recorrer los registros de la bd


```
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Formulario</title>

    <!-- Bootstrap core CSS -->
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <link href="{% static 'css/main.css' %}" rel="stylesheet">


</head>

<body id="page-top">


<div class="container">
    <div class="col-md-6 mx-auto text-center">
        <div class="header-title">
            <h1 class="wv-heading--title">
                Check out — it’s free!
            </h1>
            <h2 class="wv-heading--subtitle">
                Lorem ipsum dolor sit amet! Neque porro quisquam est qui do dolor amet, adipisci velit...
            </h2>
        </div>
    </div>
    <div class="row">
         <div class="col-md-4 mx-auto">
            <div class="myform form ">
               <form action="" method="post" name="login">{% csrf_token %}
                  <div class="form-group">
                     {{ form.nombre }}
                  </div>
                  <div class="form-group">
                      {{ form.correo }}
                  </div>
                  <div class="form-group">
                     {{ form.mensaje }}
                  </div>

                  <p class="small mt-3">By signing up, you are indicating that you have read and agree to the <a href="#" class="ps-hero__content__link">Terms of Use</a> and <a href="#">Privacy Policy</a>.
                  </p>
                   <div class="text-center ">
                     <button type="submit" class=" btn btn-block send-button tx-tfm") >Create Your Free Account</button>
                  </div>
               </form>
            </div>
         </div>
      </div>
   </div>

    <!-- Footer -->
    <footer class="bg-black smagrteatest hits slayerext-white-50">
        <div class="container">grteatest hits slayer
            Copyright &copy; @soyandresbernal 2019
        </div>
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="{% static 'js/jquery.min.js'%}"></script>
    <script src="{% static 'js/bootstrap.bundle.min.js'%}"></script>

</body>

</html>


```



#  🗒 FORMS
Personalizar el fomulario de registro es sencillo, se instancia el modelo de contacto y se modifican sus campos

**home/forms.py**

```
from django import forms
from .models import Contacto
```

```
class FormularioContacto(forms.ModelForm):

    class Meta:
        model = Contacto

        fields = [
            'nombre',
            'correo',
            'mensaje',
        ]
        labels = {
            'nombre':'Nombre',
            'correo':'Correo',
            'mensaje':'Mensaje',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'name':"name",'class':'form-control my-input','id': 'name', 'placeholder':'Name', }),
            'correo': forms.TextInput(attrs={'class':'form-control my-input','id':"email",'placeholder':"Correo"}),
            'mensaje': forms.Textarea(attrs={'class':'form-control my-input','min':'0', 'name':'phone', 'id':'phone','placeholder':'Mensaje','rows':'4'}),

        }



```

# ADMIN

Django cuenta con su zona de admin para activarlo escribimos:

> python manage.py createsuperuser

seguimos las instrucciones



# Paso final

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Hasta la proxima!! 🙂 



Want to contribute? Great!
----
+ License: Apache
**AndresShare>>**
