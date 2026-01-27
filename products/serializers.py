from rest_framework import serializers
from .models import Product, ProductOption
from .models import Comment



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductOptionSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='product.game_type', read_only=True)

    class Meta:
        model = ProductOption
        fields = ["id", "price", "slug", "title", "image", "body", "category_title"]

    
class ProductIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ["id"]
        
        
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product_option', 'text', 'rating', 'parent']

        

class ChildCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'rating', 'user', 'parent']


class RecursiveCommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'rating', 'user', 'children', 'parent']

    def get_children(self, obj):
        children = obj.children.filter(is_approved=True)
        return ChildCommentSerializer(children, many=True).data
