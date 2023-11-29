from rest_framework import serializers
from .models import UserProfile


# exclude_fields = ('raw_resume', 'raw_sop', 'raw_lor1', 'raw_lor2')
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('email',
                  'psychometrics',
                  'analysis')
