from django.test import TestCase, Client
from .models import Applicant
from django.urls import reverse
from .forms import ApplicantForm


class ApplicantModelTest(TestCase):
    def setUp(self):
        Applicant.objects.create(first_name='Jhon', last_name='Doe', email='jhon@example.com')

    def test_applicant_str_representation(self):
        applicant = Applicant.objects.get(first_name='Jhon')
        self.assertEqual(str(applicant), 'Jhon Doe')


class ApplicantListViewTest(TestCase):
    def test_applicant_list_view(self):
        response = self.client.get(reverse('applicant-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Список абітурієнтів')


class ApplicantFormTest(TestCase):
    def test_valid_applicant_form(self):
        form_data = {'first_name': 'Joe', 'last_name': 'Mama', 'email': 'joemama@example.com'}
        form = ApplicantForm(data=form_data)
        self.assertFalse(form.is_valid())


class ApplicantDetailViewTest(TestCase):
    def setUp(self):
        self.applicant = Applicant.objects.create(first_name='Deez', last_name='Nuts', email='deeznuts@example.com')

    def test_applicant_detail_view(self):
        response = self.client.get(reverse('applicant-detail', args=[self.applicant.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Деталі абітурієнта')
