from django.urls import path
from .views import ReduceReportCreateAPIView, ReduceReportByCompanyAPIView

urlpatterns = [
    path('create/', ReduceReportCreateAPIView.as_view(), name='reduce-report-create'),
    path('company/<str:company_name>', ReduceReportByCompanyAPIView.as_view(), name='reduce-report-by-company'),
]
