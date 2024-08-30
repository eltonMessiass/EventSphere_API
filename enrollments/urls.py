from  django.urls import path
from .views import EnrollmentLIST, Enrolled_to_specific_Event, EnrollmentDetail, TicketLIST, TicketDetail

urlpatterns = [
    path('', EnrollmentLIST.as_view(), name="enrollments"),
    path('<int:pk>/', EnrollmentDetail.as_view(), name="enrollment_detail"),
    path('event/<int:pk>/', Enrolled_to_specific_Event.as_view(), name="enrolled_to_specific_event"),
    path('tickets/', TicketLIST.as_view(), name="tickets"),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name="ticker_detail")
]
