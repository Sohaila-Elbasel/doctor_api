# Doctor Api
\
*__Django project Api__* has many endpoints to create:
* doctor
* patients
* clinics
* reservations

## Install
---
```
$ pip install -r requirements.txt
```

## Api endpoints
---
### Request(_GET_)
`/api/v1/`

### Response
```
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "Api Overview": "/api/v1/",
    "View all doctors": "/api/v1/view-doctors/",
    "View all patients": "/api/v1/view-patients/",
    "Create doctor": "/api/v1/create-doctor/",
    "Create patient": "/api/v1/create-patient/",
    "Create clinic": "/api/v1/create-clinic/<str:doctor_id>/",
    "View doctor": "/api/v1/view-doctor/<str:doctor_id>/",
    "View patient": "/api/v1/view-patient/<str:patient_id>/",
    "Create Reservation": "/api/v1/create-reservation/<str:patient_id>"
}
```  
### Request(_GET_)
View all doctors `/api/v1/view-doctors/`

### Response
```
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept
[]
```
### Request(_POST_)
`/api/v1/create-doctor/`
```
{
 "name": "Doctor name"
}
```

### Response
```
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "name": "Doctor name",
    "clinics": []
}
```
### Request(_POST_)
`/api/v1/create-patient/`
```
{
 "name": "patient name"
}
```

### Response
```
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "name": "patient name",
    "patient_reservations": []
}
```
### Request(_POST_)
create reservation with patient id
`/api/v1/create-reservation/<str:patient_id>/`
```
{
 "clinic": clinic_id,
 "patient": patient_id,
}
```

### Response
```
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": reservation_id,
    "clinic": clinic_id,
    "patient": patient_id
}
```
### Request(_GET_)

`/api/v1/view-patients/`


### Response
```
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

[]
```
### Request(_GET_)

`/api/v1/view-patient/<str:patient_id>/`


### Response
```
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "id": patient_id,
    "name": "patient_name",
    "patient_reservations": [
        "patient: patient_name, clinic: clinic_name",
        "patient: patient_name, clinic: clinic_name"
    ]
}
```

### Request(_GET_)

`/api/v1/view-doctor/<str:doctor_id>/`


### Response
```
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "id": doctor_id,
    "name": "doctor_name",
    "clinics": [
        {
            "id": clinic_id,
            "name": "clinic_name",
            "price": clinic_price,
            "date": "date",
            "start_time": "clinic_start_time",
            "end_time": "clinic_end_time",
            "doctor": doctor_id,
            "clinic_reservations": []
        }
    ]
}
```
### Request(_POST_)
`/api/v1/create-clinic/<str:doctor_id>/`
```
{
 "name": clinic_name,
 "price": clinic_price,
 "start_time": clinic start time,
 "end_time": clinic end time,

}
```

### Response
```
HTTP 201 Created
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "id": clinic_id,
    "name": clinic_name,
    "price": clinic_price,
    "date": clinic_date,
    "start_time": clinic start time,
    "end_time": clinic end time,
    "doctor": doctor_id,
    "clinic_reservations": []
}
```
