from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Api Overview':'/api/v1/',
		'View all doctors': '/api/v1/view-doctors/',
		'View all patients': '/api/v1/view-patients/',
		'Create doctor': '/api/v1/create-doctor/',
		'Create patient': '/api/v1/create-patient/',
		'Create clinic':'/api/v1/create-clinic/<str:doctor_id>/',
		'View doctor': '/api/v1/view-doctor/<str:doctor_id>/',
		'View patient': '/api/v1/view-patient/<str:patient_id>/',
		'Create Reservation': '/api/v1/create-reservation/<str:patient_id>',

		}

	return Response(api_urls)


@api_view(['POST'])
def createDoctor(request):
    doctor = serializers.DoctorSerializer(data=request.data)
    print(doctor)
    if not doctor.is_valid():
        return Response({'message': 'Doctor not valid'}, status=status.HTTP_404_NOT_FOUND)

    doctor.save()

    return Response(doctor.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def viewDoctors(request):
    doctors = models.Doctor.objects.all()
    serialize = serializers.DoctorSerializer(doctors, many=True)

    return Response(serialize.data)


@api_view(['GET'])
def viewDoctor(request, doctor_id):
	doctor = models.Doctor.objects.filter(id=doctor_id).first()

	if not doctor:
	    return Response({'message': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

	serialize = serializers.DoctorSerializer(doctor)


	return Response(serialize.data)


@api_view(['POST'])
def createClinic(request, doctor_id):
    doctor = models.Doctor.objects.filter(id=doctor_id).first()
    if not doctor:
        return Response({'message': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

    clinic = request.data
    clinic['doctor'] = doctor_id
    serialize = serializers.ClinicSerializer(data=clinic)

    if not serialize.is_valid():
        return Response({'message': 'clinic not valid'}, status=status.HTTP_404_NOT_FOUND)

    serialize.save()

    return Response(serialize.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def createPatient(request):
    patient = serializers.PatientSerializer(data=request.data)
    if not patient.is_valid():
        return Response({'message': 'Patient not valid'}, status=status.HTTP_404_NOT_FOUND)

    patient.save()

    return Response(patient.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def viewPatients(request):
    patients = models.Patient.objects.all()
    serializer = serializers.PatientSerializer(patients, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def viewPatient(request, patient_id):
    patient = models.Patient.objects.filter(id=patient_id).first()

    if not patient:
        return Response({'message': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

    serialize = serializers.PatientSerializer(patient)


    return Response(serialize.data)


@api_view(['POST'])
def createReservation(request, patient_id):
	reservation = serializers.ReservationSerializer(data=request.data)

	if not reservation.is_valid():
		return Response({'message': 'Reservation not valid'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


	clinic = models.Clinic.objects.filter(id=request.data.get('clinic'))
	if not clinic:
		return Response({'message': 'clinic not found'}, status=status.HTTP_404_NOT_FOUND)

	reservation.save()

	return Response(reservation.data, status=status.HTTP_201_CREATED)
