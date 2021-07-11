from rest_framework import serializers 
from .models import Products, Reviews

class ReviewsOfProductHyperlink(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        return "http://" + request.get_host() + "/reviews/?product_id=" + str(obj.id)

class ProductOfReviewHyperlink(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        return "http://" + request.get_host() + "/products/" + str(obj.product_id)


class RelatedPositiveField(serializers.JSONField):
    # values에 필드값이 들어온다. object가 들어오는게 아니다!
    def to_representation(self, value):
        result = ["http://" + self.context['request'].get_host() + "/reviews/" + str(review_id) for review_id in value]
        return result


class RelatedNegativeField(serializers.JSONField):
    def to_representation(self, value):
        result = ["http://" + self.context['request'].get_host() + "/reviews/" + str(review_id) for review_id in value]
        return result


class ReviewsUrlSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="reviews-detail" ,read_only=True)

    class Meta:
        model = Reviews
        fields = ("url", )


class ProductSerializer(serializers.ModelSerializer):
    # 기존 컬럼 이름과 똑같이 지정. 기존 컬럼의 정보를 가져온다. 중요!
    # 필드로 지정하려면 기존에 모델에 지정된 필드이름을 써줘야한다.
    related_10_reviews_with_top1_sentence_of_positive_reviews = RelatedPositiveField()
    related_10_reviews_with_top2_sentence_of_positive_reviews = RelatedPositiveField()
    related_10_reviews_with_top3_sentence_of_positive_reviews = RelatedPositiveField()
    related_10_reviews_with_top4_sentence_of_positive_reviews = RelatedPositiveField()
    related_10_reviews_with_top5_sentence_of_positive_reviews = RelatedPositiveField()

    related_10_reviews_with_top1_sentence_of_negative_reviews = RelatedNegativeField()
    related_10_reviews_with_top2_sentence_of_negative_reviews = RelatedNegativeField()
    related_10_reviews_with_top3_sentence_of_negative_reviews = RelatedNegativeField()
    related_10_reviews_with_top4_sentence_of_negative_reviews = RelatedNegativeField()
    related_10_reviews_with_top5_sentence_of_negative_reviews = RelatedNegativeField()
    
    class Meta:
        model = Products
        # 디폴트
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    reviews_link = ReviewsOfProductHyperlink(view_name="reviews-detail", read_only=True)
    # 이렇게 하면 review_id가 아닌 상품의 id가 연결된다.
    # reviews = serializers.HyperlinkedIdentityField(view_name="reviews-detail", read_only=True)

    product_id_link = serializers.HyperlinkedIdentityField(view_name="products-detail", read_only=True)

    class Meta:
        model = Products
        # 제외할 컬럼들
        exclude = (
            'message_positive', 
            'message_negative', 
            'related_10_reviews_with_top1_sentence_of_positive_reviews',
            'related_10_reviews_with_top2_sentence_of_positive_reviews',
            'related_10_reviews_with_top3_sentence_of_positive_reviews',
            'related_10_reviews_with_top4_sentence_of_positive_reviews',
            'related_10_reviews_with_top5_sentence_of_positive_reviews',
            'related_10_reviews_with_top1_sentence_of_negative_reviews',
            'related_10_reviews_with_top2_sentence_of_negative_reviews',
            'related_10_reviews_with_top3_sentence_of_negative_reviews',
            'related_10_reviews_with_top4_sentence_of_negative_reviews',
            'related_10_reviews_with_top5_sentence_of_negative_reviews',
            )

        # 직접 지정도 가능    
        # fields = ('product_status', 'id', 'code', )


class ReviewSerializer(serializers.ModelSerializer):
    # DateTime 지정 가능
    # created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S+09:00", )

    product_link = ProductOfReviewHyperlink(view_name="products-detail", read_only=True)
    class Meta:
        model = Reviews
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):
    review_id_link = serializers.HyperlinkedIdentityField(view_name="reviews-detail", read_only=True)

    class Meta:
        model = Reviews
        fields = "__all__"


