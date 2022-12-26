from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    post = serializers.SlugRelatedField(read_only=True, slug_field='id')
    # Не нашел вас в пачке (когорта 49), если убираю поле post, pytest не
    # проходит(
    # без этого поля пишет что нужно установить поле post только для чтения)

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True, default=serializers.CurrentUserDefault())
    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following'),
            message='Нельзя повторно подписаться')]

    def validate_following(self, value):
        user = self.context.get('request').user
        if user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return value
