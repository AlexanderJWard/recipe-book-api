from rest_framework import serializers
from support_tickets.models import Support


class SupportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_screenshot(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.screenshot.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.screenshot.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Support
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'status', 'screenshot', 'is_owner', 'profile_id', 'profile_image',
            'email_address', 'issue'
        ]
