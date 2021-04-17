from rest_framework import serializers
from . import models


class ClinicSerializer(serializers.ModelSerializer):
    clinic_reservations = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Clinic
        fields = ('id', 'name', 'name', 'price', 'date', 'start_time', 'end_time', 'doctor', 'clinic_reservations')


class DoctorSerializer(serializers.ModelSerializer):
    clinics = ClinicSerializer(many=True, read_only=True)

    class Meta:
        model = models.Doctor
        fields = ('id', 'name', 'clinics')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = ('id', 'clinic', 'patient')


class PatientSerializer(serializers.ModelSerializer):
    patient_reservations = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Patient
        fields = ('id', 'name', 'patient_reservations')
