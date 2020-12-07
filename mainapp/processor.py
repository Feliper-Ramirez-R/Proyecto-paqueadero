from django.contrib.auth.models import User
from mainapp.models import Transporte, Usuario, Imagen

def get_users(request):

    users = User.objects.values_list('id', 'id','username','first_name', 'last_name', 'email')
   
    return {
        'users':users
              
    }


