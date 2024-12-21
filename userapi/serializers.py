from rest_framework import serializers
from userapi.models import Company
# create serializers here 

class companySerializer(serializers.HyperlinkedModelSerializer)
    class Meta:
        model = Company
        fields = "__all__"