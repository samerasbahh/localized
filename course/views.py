from .models import Course # Import our Course model
from .serializers import CourseSerializer # Import the serializer we just created
from rest_framework import filters, generics

# Import django rest framework functions
from rest_framework.permissions import AllowAny

from rest_framework.filters import OrderingFilter, SearchFilter


class CourseListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = ('title', 'description')
    ordering_fields = ('title', 'description', 'time', 'professor')
    search_fields = ('title', 'description', 'professor__first_name', 'professor__last_name', 'professor__email',
                     'time__period')


