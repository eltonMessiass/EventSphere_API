from django.urls import path
from .views import EventLIST, CategoryList, CategoryDetail, EventDetail, TagLIST, TagDetail



urlpatterns = [
    path('events/', EventLIST.as_view(), name="events"),
    path('<int:pk>/', EventDetail.as_view(), name="event_detail"),
    path('categories/', CategoryList.as_view(), name="category"),
    path('categories/<int:pk>/', CategoryDetail.as_view, name="category_detail"),
    path('tags/', TagLIST.as_view(), name="tags"),
    path('tags/<int:pk>/', TagDetail.as_view(), name="tag=detail")
]
