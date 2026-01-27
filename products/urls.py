from django.urls import path


from .views import (
    ProductDetailView,ProductOptionDetailView,
    PopularProductsView, DiscountedProductsView, SpecialOffersView,
    CallOfDutyProductsView, ClashProductsView, PubgProductsView,
    CartProductsView, CommentAPIView
)
urlpatterns = [
    path('option/<slug:slug>/', ProductOptionDetailView.as_view(), name='product-option-detail'),
    path("comments/", CommentAPIView.as_view(), name="comments"),
 
    path("cod/", CallOfDutyProductsView.as_view(), name="cod-products"),
    path("clash/", ClashProductsView.as_view(), name="clash-products"),
    path("pubg/", PubgProductsView.as_view(), name="pubg-products"),

    path("popular/", PopularProductsView.as_view(), name="popular-products"),
    path("discounted/", DiscountedProductsView.as_view(), name="discounted-products"),
    path("special-offers/", SpecialOffersView.as_view(), name="special-offers"),
    path("cart/products/", CartProductsView.as_view(), name="cart-products"),
    
  
    path("<str:slug>/", ProductDetailView.as_view(), name="product-detail"),
]
