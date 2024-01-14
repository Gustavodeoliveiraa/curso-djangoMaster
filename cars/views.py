from django.views.generic import ( 
    ListView, CreateView, DetailView, UpdateView, DeleteView
)
from .models import Car
from .forms import ModelCarForm
from django.urls import reverse_lazy


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('-id')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    model = Car
    form_class = ModelCarForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk}) #type: ignore # noqa


class NewCarCreateView(CreateView):
    model = Car
    form_class = ModelCarForm
    template_name = 'new_car.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        # altera o nome do objeto empurrado para o template
        # por padrão é (form), alterado para new_car_form
        context = super().get_context_data(**kwargs)
        context['new_car_form'] = context.pop('form')
        return context


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/'
