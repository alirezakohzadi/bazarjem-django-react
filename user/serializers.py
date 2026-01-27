from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password



User = get_user_model()

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone_number", "is_verified", "wallet_balance", "role"]
        

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "این ایمیل قبلاً ثبت شده است."})
        
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "رمز عبور با تاییدیه مطابقت ندارد."})
        
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  
        user = User.objects.create_user(**validated_data)  
        return user
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    
    
    def validate(self, attrs):
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError({"new_password": "رمز عبور جدید نباید با رمز قبلی یکی باشد."})
        return attrs

        
        

class ChangeUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['role']

    def validate_role(self, value):
        allowed_roles = ['admin', 'seller', 'customer']
        if value not in allowed_roles:
            raise serializers.ValidationError("نقش انتخاب شده معتبر نیست.")
        return value



