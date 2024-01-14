from django.urls import path
from .views import (
    CarsListView, NewCarCreateView, CarDetailView,
    CarUpdateView, CarDeleteView
)


urlpatterns = [
    path('', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),

]
