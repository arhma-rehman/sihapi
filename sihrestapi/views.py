from multiprocessing import connection
from rest_framework.response import Response
from sihrestapi.serializers import student_serializer
from sihrestapi.models import student
from rest_framework.decorators import api_view
from django.db import connection

# Create your views here.


@api_view(['GET', 'POST'])
def sihApi(request):
    if request.method == 'GET':
        if connection.connection is None:
            cursor = connection.cursor()
        cursor = connection.connection.cursor()
        cursor.execute(f'SELECT * FROM sihrestapi_student')
        stu = cursor.fetchall()
        return Response(stu)
    if request.method == 'POST':
        aadhar = request.data['aadhar_no']
        if connection.connection is None:
            cursor = connection.cursor()
        cursor = connection.connection.cursor()
        cursor.execute(
            f"SELECT * FROM sihrestapi_student WHERE aadhar_no = {aadhar}")
        stu = cursor.fetchall()
        return Response(stu)

    # if request.method == 'GET':
    #     stud = student.objects.all()
    #     studserializer = student_serializer(stud)
    #     return Response(studserializer.data)

    # if request.method == 'POST':
    #     aadhar = request.data(student.aadhar_no)
    #     stud = student.objects.get(student.aadhar_no == aadhar)
    #     studserializer = student_serializer(stud)
    #     return Response(studserializer.data)
