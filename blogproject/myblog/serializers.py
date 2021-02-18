from rest_framework import serializers

from myblog.models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = (
            'post',
            'title',
            'content',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['updated_on'] = instance.updated_on

        return data
