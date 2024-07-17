from django.urls import path
from .views import ReduceReportCreateAPIView, ReduceReportByCompanyAPIView,create_reduce_report

urlpatterns = [
    path('create-report/', create_reduce_report, name='create-reduce-report'),
    path('create/', ReduceReportCreateAPIView.as_view(), name='reduce-report-create'),
    path('company/<str:company_name>', ReduceReportByCompanyAPIView.as_view(), name='reduce-report-by-company'),
]
