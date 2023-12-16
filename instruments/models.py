from django.db import models
from datetime import date


class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    date_of_birth = models.DateField(default=date(2000, 1, 1))
    created_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='media/', null=True, blank = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Document(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50)
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.applicant.first_name} {self.applicant.last_name} - {self.document_type}'
