from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer  

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  
