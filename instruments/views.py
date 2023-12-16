from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Applicant
from .serializers import ApplicantSerializer
from .forms import ApplicantForm


class ApplicantList(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def get(self, request, *args, **kwargs):
        form = ApplicantForm()
        return render(request, 'kursova/applicant_list.html', {'applicants': self.get_queryset(), 'form': form})

    def post(self, request, *args, **kwargs):
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('applicant-list')
        else:
            return render(request, 'kursova/applicant_list.html', {'applicants': self.get_queryset(), 'form': form})


class ApplicantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def retrieve(self, request,  *args, **kwargs):
        applicant = self.get_object()
        return render(request, 'kursova/applicant_detail.html', {'applicant': applicant})
