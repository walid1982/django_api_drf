# from django.shortcuts import render
# from django.http import JsonResponse
# from urllib import response

# from django.http import JsonResponse
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from students.models import Student
from employees.models import Employee
from blogs.models import Blog
from bloogers.models import Blooger, Comment
from rest_framework import mixins, generics

from .serializers import (
    CommentSerializer,
    EmployeeSerializer,
    StudentSerializer,
    BlogSerializer,
    BloogerSerializer,
)


@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', "DELETE"])
def studentDetailView(request, pk):

    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class Employees(APIView):
#     def get(self, request):
#         Employees = Employee.objects.all()
#         serializer = EmployeeSerializer(Employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EmployeesDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         # serializer = StudentSerializer(data=request.data)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#Mixins 
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class EmployeesDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#         queryset = Employee.objects.all()
#         serializer_class = EmployeeSerializer
    
#         def get(self, request, pk):
#             return self.retrieve(request, pk)
        
#         def put(self, request, pk):
#             return self.update(request, pk)
        
#         def delete(self, request, pk):
#             return self.destroy(request, pk)


#Generic Views
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Blogs(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class Bloogers(generics.ListCreateAPIView):
    queryset = Blooger.objects.all()
    serializer_class = BloogerSerializer


class BloogerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blooger.objects.all()
    serializer_class = BloogerSerializer


class Comments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer