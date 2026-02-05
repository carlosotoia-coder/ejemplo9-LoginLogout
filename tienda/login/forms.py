from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicamos estilos de Tailwind a cada campo automáticamente
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = (
                'w-full px-4 py-3 rounded-xl border border-gray-200 '
                'focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 '
                'outline-none transition-all duration-200'
            )

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = (
                'w-full px-4 py-3 rounded-xl border border-gray-200 '
                'focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 '
                'outline-none transition-all duration-200'
            )