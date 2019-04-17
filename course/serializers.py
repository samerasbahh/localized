from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    time = serializers.StringRelatedField(many=True, read_only=True)
    professor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description','professor',  'time')


