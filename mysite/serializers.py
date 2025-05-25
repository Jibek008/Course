from django.db.models.functions import RTrim
from rest_framework import serializers
from .models import *


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['network_name', 'network_link']


class UserProfileSerializer(serializers.ModelSerializer):
    user_network = NetworkSerializer(read_only=True, many=True)
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CourseListSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id','course_image','course_name', 'price','author',]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['lesson', 'video', 'document']


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer(many=True)
    author = UserProfileSimpleSerializer(many=True)
    update_date = serializers.DateTimeField(format=('%d-%m-%Y %H:%M'))
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    lessons = LessonSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['course_name', 'course_image', 'category', 'description','price','certificate_have',
                  'course_lan', 'update_date', 'created_date','course_type', 'author', 'lessons']




class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'



class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_courses = CourseListSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['category_name', 'category_courses']



class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class  CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'




class  ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'