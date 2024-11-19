from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserModel.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password]
                                     )
    name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ['name', 'email', 'password']
        extra_kwargs = {
            'name': {'required': True}
        }

    def create(self, validated_data):  # noqa
        user = UserModel.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
