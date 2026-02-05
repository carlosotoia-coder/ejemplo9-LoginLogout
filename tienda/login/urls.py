from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # --- RUTAS PÚBLICAS ---
    path('', views.landing, name='landing'),
    path('registro/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    
    # --- RUTAS PROTEGIDAS (Basadas en funciones) ---
    path('dashboard/', views.dashboard, name='dashboard'),
    path('curso/clase-protegida/', views.vista_protegida_permiso, name='vista_permiso'),

    # --- RUTAS DE EJEMPLO (Mixins y Clases) ---
    path('dashboard-mixin/', views.DashboardMixinView.as_view(), name='dashboard_mixin'),
    path('permiso-mixin/', views.VistaPermisoMixinView.as_view(), name='permiso_mixin'),

    # --- LOGOUT ---
    # Usamos la vista predeterminada de Django para el logout
    path('logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),
]