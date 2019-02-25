from django.urls import reverse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from home.models import Contacto
from .forms import FormularioContacto


class Home(CreateView):
    model = Contacto
    form_class = FormularioContacto
    success_url = reverse_lazy('home:home')
    template_name = 'home.html'

    def get_success_url(self):

        return reverse('home:home')






