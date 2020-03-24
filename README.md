# just_for_fun

1.  Para activar/desactivar entorno virtual:
        source venv/bin/activate
        deactivate 
2.  Instalar dependencias:
        pip install -r requirements.txt
3.  Verificar dependencias
        pip list

## Django
0. Instalar django
        pip install django
1. Poner el servidor al servicio
        python manage.py runserver
                            /admin
                            /signup
Salir del servidor: ctrl+c
2.  Para hacer pruebas
        python manage.py shell
            from django.contrib.auth.models import User
            User.objects.count()
            u=User.objects.first()
            u.username
            #Revisemos el email que esté asociado al usuario
            u = User.objects.get(username='espe1') 
            #Mmmm mejor asignémosle uno
            u.email = 'espe1@example.com'
            u.save  
            exit()
3. URLS 
        /accounts/login/
        accounts/password_reset/
        /password_change/
        /secret/
        /secretitos/

4. Para las vistas dentro de login:
        Hay dos mecanismos que se pueden ver en las urls /secret + /secretitos. 
        El mecanismo recomendado es /secret:  es straightforward: se crea la función en views.py y luego la url en url.py, basado en la página que se quiera enviar (ver ejemplo con el html). 

