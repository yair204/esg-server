

from rest_framework import serializers
from .models import ReduceReport

class ReduceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReduceReport
        fields = ['id', 'company_name', 'date', 'electricity', 'gas', 'water']
