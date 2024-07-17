# reduceReports/forms.py
from django import forms
from .models import ReduceReport

class ReduceReportForm(forms.ModelForm):
    class Meta:
        model = ReduceReport
        fields = ['company_name', 'date', 'electricity', 'gas', 'water', 'electricity_cost', 'gas_cost', 'water_cost']
