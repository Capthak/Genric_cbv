from django.urls import path
from .views import LaptopCreateView,LaptopListView,LaptopUpadateView,LaptopDelete

urlpatterns=[
    path('list/',LaptopListView.as_view()),
    path('create/',LaptopCreateView.as_view()),
    path('update/<int:pk>',LaptopUpadateView.as_view()),
    path('delete/<int:pk>',LaptopDelete.as_view()),
    

]