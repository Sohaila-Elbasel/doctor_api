from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('view-doctors/', views.viewDoctors, name='view-doctors'),
    path('create-doctor/', views.createDoctor, name='create-doctor'),
    path('create-patient/', views.createPatient, name='create-patient'),
    path('create-reservation/<str:patient_id>', views.createReservation, name='create-reservation'),
    path('view-patients/', views.viewPatients, name='view-patients'),
    path('view-patient/<str:patient_id>', views.viewPatient, name='view-patient'),
    path('view-doctor/<str:doctor_id>', views.viewDoctor, name='view-doctor'),
    path('create-clinic/<str:doctor_id>/', views.createClinic, name='create-clinic'),
]
