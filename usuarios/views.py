from django.shortcuts import render, redirect
from .models import Usuario, Rol
from django.contrib.auth import authenticate, login
from django.contrib import messages



def registro_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        telefono = request.POST.get("telefono")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        # Verificación de contraseñas
        if password != password_confirm:
            messages.error(request, "Las contraseñas no coinciden")
            return render(request, 'usuarios/registro.html')

        # Verifica si el rol 'cliente' existe
        try:
            rol_cliente = Rol.objects.get(nombre="cliente")
        except Rol.DoesNotExist:
            messages.error(request, "El rol de cliente no existe")
            return render(request, 'usuarios/registro.html')

        # Verifica si el email ya está registrado
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Este email ya está registrado")
            return render(request, 'usuarios/registro.html')

        # Crea el usuario si todo está correcto
        try:
            usuario = Usuario.objects.create_user(
                email=email,
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                password=password,
                rol=rol_cliente  # Asegúrate de pasar el rol aquí
            )
            messages.success(request, "Registro exitoso.")
            return redirect('login')  # Redirige al login solo si el registro es exitoso

        except Exception as e:
            messages.error(request, f"Ocurrió un error al registrar el usuario: {e}")
            return render(request, 'usuarios/registro.html')

    return render(request, 'usuarios/registro.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Autenticación con el modelo de usuario personalizado
        user = authenticate(request, email=email, password=password)  # Cambia username por email

        if user is not None:
            login(request, user)
            return redirect('home')  # Asegúrate de que 'home' esté definido en tu URL
        else:
            messages.error(request, "Credenciales inválidas.")
    
    return render(request, 'usuarios/login.html')


def home(request):
    return render(request, 'home.html')

