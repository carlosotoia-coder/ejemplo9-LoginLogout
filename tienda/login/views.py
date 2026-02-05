from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from .forms import RegistroForm, LoginForm 

# --- VISTAS PÚBLICAS ---

def landing(request):
    return render(request, "landing.html")

def register(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegistroForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

# --- VISTAS PROTEGIDAS ---

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@permission_required("auth.view_user", raise_exception=True)
def vista_protegida_permiso(request):
    return render(request, "permiso.html")

# --- VISTAS BASADAS EN CLASES ---

class DashboardMixinView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

class VistaPermisoMixinView(PermissionRequiredMixin, TemplateView):
    permission_required = "auth.view_user"
    template_name = "permiso.html"
