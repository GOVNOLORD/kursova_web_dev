from django.urls import path
from .views import ApplicantList, ApplicantDetail

urlpatterns = [
    path('applicants/', ApplicantList.as_view(), name='applicant-list'),
    path('home/<int:pk>/', ApplicantDetail.as_view(), name='applicant-detail'),
]
