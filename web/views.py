from django.shortcuts import render, redirect, get_object_or_404
from .models import CalificacionFlan, Flan
from .forms import ContactForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Vistas para tu aplicación

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html', {})

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    nombre_usuario = request.user.username if request.user.is_authenticated else None
    return render(request, 'welcome.html', {'flanes': flanes_privados, 'nombre_usuario': nombre_usuario})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_exitoso')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_view_exito(request):
    return render(request, 'contacto_exitoso.html', {})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'

def flan_details(request, flan_id):
    flan = get_object_or_404(Flan, pk=flan_id)
    return render(request, 'flan_details.html', {'flan': flan})

def mi_vista(request):
    nombre_usuario = None
    if request.user.is_authenticated:
        nombre_usuario = request.user.username  # Suponiendo que estás usando el modelo User predeterminado de Django
    return render(request, 'welcome.html', {'nombre_usuario': nombre_usuario})

def calificar_flan(request, flan_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        print(rating)
        if rating is not None:
            try:
                rating = int(rating)
                # Obtener el objeto Flan
                flan = get_object_or_404(Flan, pk=flan_id)
                
                # Crear un nuevo objeto CalificacionFlan
                calificacion_flan = CalificacionFlan.objects.create(flan=flan, calificacion=rating)
                calificacion_flan.save()
                
                # Redirigir al usuario a la página de detalles del flan
                return redirect('flan_details', flan_id=flan_id)
            except ValueError:
                # Manejar el caso en el que la calificación no sea un número entero válido
                pass
        else:
            # Manejar el caso cuando el valor de la calificación no se proporciona en la solicitud POST
            pass
    
    # Si la solicitud no es POST, redirigir al usuario a la página de detalles del flan
    return redirect('flan_details', flan_id=flan_id)