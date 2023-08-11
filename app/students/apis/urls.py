from django.urls import path
from students.apis.views import  StudentHomeAPIView, StudentCourseEnroleAPIView,\
    StudentCourseDetailAPIView, StudentSessionDetailAPIView

urlpatterns = [
    path('home/', StudentHomeAPIView.as_view(), name='home'),
    path('course/<int:course_id>/',
         StudentCourseDetailAPIView.as_view(), name="course_detail"),
    path('enroll/<int:course_id>/', 
         StudentCourseEnroleAPIView.as_view(), name="course_enroll"),
    path('session/<int:session_id>/',
         StudentSessionDetailAPIView.as_view(), name="session_detail"),
]
