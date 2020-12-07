from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.login_page, name="index"),
    path('inicio/',views.login_page, name="inicio"),
    path('registro_usuario/',views.register, name="register"),
    path('pagina/',views.page, name="page"),
    path('registrar_transporte/',views.transporte, name="transporte"),
    path('save_trans/', views.save_trans, name="save"),
    path('prueba/', views.prueba, name="prueba"),
    path('reporte/', views.reportes, name="reporte"),
    path('consultar/', views.consultar, name="consultar"),
    path('parqueadero/', views.parqueadero, name="parqueadero"),
    path('logout/', views.logout_user, name="logout"),
    path('pagos_mes/', views.pagos_mes, name="pagos_mes"),
    path('cambiar_imagen/', views.editar_imagen, name="save_image"),
    path('tarifas/', views.tarifas, name="tarifas")
 
   
]

#configuracion para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)