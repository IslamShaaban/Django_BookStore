from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model= User
        fields = ('username', 'email', 'password', 'password2')
    
    def save(self, **kwargs):
        user = User(
            email    = self.validated_data.get('email'),
            username = self.validated_data.get('username')
        )

        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError({
                'password' : "Passwords Don't Match"
            })
        else:
            user.set_password(self.validated_data.get('password'))
            user.save()