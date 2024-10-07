from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer


from main.models import Link, Product


class LinkSerializer(ModelSerializer):
    count_of_product = SerializerMethodField()
    products = SerializerMethodField()

    def get_count_of_product(self, link):
        return link.products.count()

    def get_products(self, link):
        product_set = Product.objects.filter(supplier=link.id)
        return [product.name for product in product_set]

    class Meta:
        model = Link
        fields = (
            "id", "name", "email", "country", "city", "street", "house_number", "level", "supplier", "arrears",
            "created_at", "count_of_product", "products"
        )


# class AdvertisementSerializer(ModelSerializer):
#     count_of_feedback = SerializerMethodField()
#     feedbacks = SerializerMethodField()
#
#     def get_count_of_feedback(self, advertisement):
#         return advertisement.feedbacks.count()
#
#     def get_feedbacks(self, advertisement):
#         feedback_set = Feedback.objects.filter(ad=advertisement.id)
#         return [feedback.text for feedback in feedback_set]
#
#     class Meta:
#         model = Advertisement
#         fields = ("title", "price", "author", "count_of_feedback", "feedbacks", "created_at")

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
