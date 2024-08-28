from django.urls import path
from .views import EventLIST, CategoryList, CategoryDetail



urlpatterns = [
    path('events/', EventLIST.as_view(), name="events"),
    path('categories/', CategoryList.as_view(), name="category"),
    path('categories/<int:pk>/', CategoryDetail.as_view, name="category_detail")
]
