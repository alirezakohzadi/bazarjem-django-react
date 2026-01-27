from django.contrib import admin
from .models import Product, ProductOption, Comment

# 🔹 نمایش گزینه‌های خرید در صفحه محصول
class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 0  # تعداد فیلدهای خالی اولیه

# 🔹 تنظیمات حرفه‌ای برای صفحه محصولات
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'game_type', 'created_at', "image")
    list_filter = ('game_type', 'created_at', "image")
    search_fields = ('name', 'description')
    ordering = ('-created_at',)  # مرتب‌سازی بر اساس جدیدترین‌ها
    inlines = [ProductOptionInline]  # اضافه کردن گزینه‌های خرید در صفحه محصول

# 🔹 تنظیمات مدیریت گزینه‌های خرید
@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'price', 'is_special_offer', 'is_discounted', 'is_popular')
    search_fields = ('product__name', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_option', 'rating', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    search_fields = ('text', 'user__username')
    actions = ['approve_comments']

    @admin.action(description="تأیید کامنت‌های انتخاب‌شده")
    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)