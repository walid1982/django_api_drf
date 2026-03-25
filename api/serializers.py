#from xml.etree.ElementTree import Comment

from bloogers.models import Blooger, Comment
from rest_framework import serializers
from students.models import Student
from employees.models import Employee
from blogs.models import Blog

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BloogerSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blooger
        fields = ['id', 'title', 'author', 'content', 'comments']