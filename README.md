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
        http://127.0.0.1:8000/
                            /admin
                            /signup
2.  Para hacer pruebas
        python manage.py shell
            from django.contrib.auth.models import User
            User.objects.count()
            u=User.objects.first()
            u.username
            exit()
3.
4.

