from django.conf.urls import url
from .views import PdfView

urlpatterns = [
    url(r'$', PdfView.as_view(), name='index'),
]