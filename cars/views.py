from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Car
from .forms import ModelCarForm


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
    success_url = '/'


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
