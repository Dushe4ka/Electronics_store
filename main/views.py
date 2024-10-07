from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from main.models import Link, Product
from main.paginators import LinkPaginator
from main.permissions import IsActive
from main.serializers import LinkSerializer, ProductSerializer


class LinkCreateAPIView(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsActive,]


class LinkListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsActive]
    pagination_class = LinkPaginator
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ('country',)


class LinkRetrieveAPIView(RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsActive,]


class LinkUpdateAPIView(UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsActive,]

    def perform_update(self, serializer):
        if "arrears" in serializer.validated_data:
            serializer.validated_data.pop("arrears")
            raise Exception("Вы не можете менять поле задолженности")
        super().perform_update(serializer)


class LinkDestroyAPIView(DestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsActive,]


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive,]


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive, ]


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive, ]


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive, ]
