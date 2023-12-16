from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from instruments.views import ApplicantList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applicants/', ApplicantList.as_view(), name='applicant-list'),
    path('applicants/', include('instruments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
