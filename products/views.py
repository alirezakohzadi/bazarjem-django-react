from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductOption, Comment
from .serializers import ProductSerializer, ProductOptionSerializer, RecursiveCommentSerializer, CommentCreateSerializer


class CallOfDutyProductsView(generics.ListAPIView):
    authentication_classes = []
    serializer_class = ProductOptionSerializer
    queryset = ProductOption.objects.filter(product__game_type="cod")


class ClashProductsView(generics.ListAPIView):
    authentication_classes = []
    serializer_class = ProductOptionSerializer
    queryset = ProductOption.objects.filter(product__game_type="clash")


class PubgProductsView(generics.ListAPIView):
    authentication_classes = []
    serializer_class = ProductOptionSerializer
    queryset = ProductOption.objects.filter(product__game_type="pubg")


class ProductDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"


class ProductOptionDetailView(generics.RetrieveAPIView):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    lookup_field = "slug"


class PopularProductsView(generics.ListAPIView):
    serializer_class = ProductOptionSerializer
    queryset = ProductOption.objects.filter(is_popular=True)


class DiscountedProductsView(generics.ListAPIView):
    serializer_class = ProductOptionSerializer
    queryset = ProductOption.objects.filter(is_discounted=True)


class SpecialOffersView(generics.ListAPIView):
    serializer_class = ProductOptionSerializer
    queryset = ProductOption.objects.filter(is_special_offer=True)


class CartProductsView(APIView):
    def post(self, request, *args, **kwargs):
        ids = request.data.get("ids", [])
        products = ProductOption.objects.filter(id__in=ids)
        serializer = ProductOptionSerializer(products, many=True)
        return Response(serializer.data)


class CommentAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        authentication_classes = []
        product_option_id = request.query_params.get("product_option")
        
        if product_option_id:
            comments = Comment.objects.filter(
                product_option_id=product_option_id,
                is_approved=True
            ).select_related('user').prefetch_related('children')
        else:
            comments = Comment.objects.filter(
                is_approved=True
            ).select_related('user').prefetch_related('children')

        serializer = RecursiveCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"detail": "نظر با موفقیت ثبت شد و پس از تایید نمایش داده خواهد شد."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
