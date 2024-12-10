from rest_framework import generics

from member.models import (
    Product,
    Member,
)
from member.serializers import (
    ProductSerializer,
    MemberSerializer,
    MemberUpdateSerializer,
    )


# Product
class ProductListCreateAPIView(generics.ListCreateAPIView):
    """ Listing&Creating Product """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    """ Detail&Update Product """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    """ Deleting Product """
    queryset = Product.objects.all()


# Member
class MemberListCreateAPIView(generics.ListCreateAPIView):
    """ Listing&Creating Member """
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    filterset_fields = ['member_country']


class MemberDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    """ Detail&Update Member """
    # serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def get_serializer_class(self):
        if self.request == "put" or "patch":
            return MemberUpdateSerializer
        return MemberSerializer


class MemberDestroyAPIView(generics.DestroyAPIView):
    """ Deleting Member """
    queryset = Member.objects.all()
