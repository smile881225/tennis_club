from .models import Course_reservation
import django_filters


class Course_reservation_Filter(django_filters.FilterSet):
    class Meta:
        model = Course_reservation
        fields = '__all__'