from django.urls import path
from . import views

urlpatterns = [
    path('flight_status/',views.flight_status,name="check flight-status"),
    path('update/', views.update_flight_status, name='update_flight_status'),
    path('get_all_flights/', views.get_all_flights, name='get_all_flights'),
    path('flights/<str:flight_number>/', views.get_flight_status, name='get_flight_status'),
#    path('flights/update/', views.update_flight_status, name='update_flight_status'),
]


