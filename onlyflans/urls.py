from django.contrib import admin
from django.urls import include, path
from web.views import contact_view_exito, index, about, welcome, contact_view, flan_details, calificar_flan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('welcome/', welcome, name='welcome'),
    path('contacto_exitoso/', contact_view_exito, name='contacto_exitoso'),
    path('contact_form/', contact_view, name='contact_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('flan/<int:flan_id>/', flan_details, name='flan_details'),
    path('calificar-flan/<int:flan_id>/', calificar_flan, name='calificar_flan'),
]





    
    
    
    
    

