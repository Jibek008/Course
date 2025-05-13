from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(16),
                                                      MaxValueValidator(70)],
                                             null=True,blank=True)
    user_image = models.ImageField(upload_to='user_images/')
    user_number = PhoneNumberField(null=True,blank=True)
    ROLE_CHOICES = (
        ('teacher','teacher'),
        ('student','student')

    )
    user_role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='student')
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class Network(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    network_name = models.CharField(max_length=32)
    network_link = models.URLField()


    def __str__(self):
        return f'{self.user},{self.network_name}'



class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    category =  models.ManyToManyField(Category)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    certificate_have = models.BooleanField()
    course_lan = models.CharField(max_length=32, verbose_name='Язык курса:')
    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    TYPE_CHOICES = (
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('master', 'master')
    )
    course_type = models.CharField(choices=TYPE_CHOICES, max_length=32)
    author = models.ManyToManyField(UserProfile)
    course_image = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return self.course_name


class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    lesson = models.CharField(max_length=64)
    video = models.FileField(upload_to='course_videos/',null=True,blank=True )
    document = models.FileField(upload_to='course_documents/', null=True, blank=True)


    def __str__(self):
        return f'{self.course}, {self.lesson}'


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=32)


class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    questions_name = models.CharField(max_length=64)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])


class Option(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    variant = models.CharField(max_length=32)
    check_var = models.BooleanField()


class Certificate(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    certificate = models.FileField(upload_to='certificate/')
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.user},  {self.course}'


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(2, 6)],
                                 null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.course}'