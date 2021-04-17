from django.db import models
from django.conf import settings


class UserModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True


class Doctor(UserModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(UserModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    doctor = models.ForeignKey(Doctor, null=True, blank=True, related_name='clinics', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    clinic = models.ForeignKey(Clinic, related_name='clinic_reservations', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='patient_reservations', on_delete=models.CASCADE)

    def __str__(self):
        return f'patient: {self.patient.name}, clinic: {self.clinic.name}'
