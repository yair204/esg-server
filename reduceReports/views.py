from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ReduceReport
from .serializers import ReduceReportSerializer

class ReduceReportCreateAPIView(APIView):
    def post(self, request):
        serializer = ReduceReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReduceReportByCompanyAPIView(APIView):
    def get(self, request, company_name):
        print(" ~ company_name:", company_name)
        try:
            reports = ReduceReport.objects.filter(company_name=company_name)
            serializer = ReduceReportSerializer(reports, many=True)
            print("🚀 ~ serializer:", serializer.data)
            return Response(serializer.data)
        except ReduceReport.DoesNotExist:
            return Response({'error': 'No reports found for this company'}, status=status.HTTP_404_NOT_FOUND)
