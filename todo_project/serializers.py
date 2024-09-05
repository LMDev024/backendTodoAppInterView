from rest_framework import serializers
from tasks.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = ['id','email','first_name','last_name','password']