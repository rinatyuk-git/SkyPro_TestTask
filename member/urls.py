from django.urls import path
from member.apps import MemberConfig
from member.views import (
    ProductListCreateAPIView,
    ProductDetailUpdateAPIView,
    ProductDestroyAPIView,
    MemberListCreateAPIView,
    MemberDetailUpdateAPIView,
    MemberDestroyAPIView,
)

app_name = MemberConfig.name

urlpatterns = [
    # Product
    path('products/', ProductListCreateAPIView.as_view(), name='product_list'),
    path('product/create/', ProductListCreateAPIView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductDetailUpdateAPIView.as_view(), name='product_detail'),
    path('product/update/<int:pk>', ProductDetailUpdateAPIView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', ProductDestroyAPIView.as_view(), name='product_delete'),

    # Member
    path('members/', MemberListCreateAPIView.as_view(), name='member_list'),
    path('member/create/', MemberListCreateAPIView.as_view(), name='member_create'),
    path('member/<int:pk>', MemberDetailUpdateAPIView.as_view(), name='member_detail'),
    path('member/update/<int:pk>', MemberDetailUpdateAPIView.as_view(), name='member_edit'),
    path('member/delete/<int:pk>', MemberDestroyAPIView.as_view(), name='member_delete'),
    ]
