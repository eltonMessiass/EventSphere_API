from  django.urls import path
from .views import EnrollmentLIST

urlpatterns = [
    path('', EnrollmentLIST.as_view(), name="enrollments")
]
