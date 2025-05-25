from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'networks', NetworkViewSet, basename='networks'),
router.register(r'lesson', LessenViewSet, basename='lesson'),
router.register(r'exam', ExamViewSet, basename='exam'),
router.register(r'question', QuestionsViewSet, basename='question'),
router.register(r'option', OptionViewSet, basename='option'),
router.register(r'certificate', CertificateViewSet, basename='certificate'),
router.register(r'review', ReviewViewSet, basename='review'),

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),

    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
]