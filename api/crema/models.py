# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Products(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
    name = models.TextField(blank=True)
    code = models.IntegerField(blank=True, null=True)
    representative_score = models.FloatField(blank=True, null=True)
    representative_review_id = models.IntegerField(blank=True, null=True)
    display = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    shop_builder_created_at = models.DateTimeField(blank=True, null=True)
    shop_builder_updated_at = models.DateTimeField(blank=True, null=True)
    reviews_count = models.BigIntegerField(blank=True, null=True)
    org_price = models.BigIntegerField(blank=True, null=True)
    final_price = models.BigIntegerField(blank=True, null=True)
    product_status = models.TextField(blank=True)
    image = models.JSONField(blank=True)
    message_positive = models.TextField(blank=True)
    top1_sentence_of_positive_reviews = models.TextField(blank=True)
    top2_sentence_of_positive_reviews = models.TextField(blank=True)
    top3_sentence_of_positive_reviews = models.TextField(blank=True)
    top4_sentence_of_positive_reviews = models.TextField(blank=True)
    top5_sentence_of_positive_reviews = models.TextField(blank=True)
    related_10_reviews_with_top1_sentence_of_positive_reviews = models.JSONField(blank=True, null=True)
    related_10_reviews_with_top2_sentence_of_positive_reviews = models.JSONField(blank=True, null=True)
    related_10_reviews_with_top3_sentence_of_positive_reviews = models.JSONField(blank=True, null=True)
    related_10_reviews_with_top4_sentence_of_positive_reviews = models.JSONField(blank=True, null=True)
    related_10_reviews_with_top5_sentence_of_positive_reviews = models.JSONField(blank=True, null=True)
    message_negative = models.TextField(blank=True, null=True)
    top1_sentence_of_negative_reviews = models.TextField(blank=True)
    top2_sentence_of_negative_reviews = models.TextField(blank=True)
    top3_sentence_of_negative_reviews = models.TextField(blank=True)
    top4_sentence_of_negative_reviews = models.TextField(blank=True)
    top5_sentence_of_negative_reviews = models.TextField(blank=True)
    related_10_reviews_with_top1_sentence_of_negative_reviews = models.JSONField(blank=True, null=True)
    related_10_reviews_with_top2_sentence_of_negative_reviews = models.JSONField(blank=True, null=True)
    related_10_reviews_with_top3_sentence_of_negative_reviews = models.JSONField(blank=True, null=True)
    related_10_reviews_with_top4_sentence_of_negative_reviews = models.JSONField(blank=True, null=True)
    related_10_reviews_with_top5_sentence_of_negative_reviews = models.JSONField(blank=True, null=True)
    representative_review_message = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'products'


class Reviews(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.TextField(blank=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_code = models.TextField(blank=True)
    user_name = models.TextField(blank=True)
    message = models.TextField(blank=True)
    message_cleaned = models.TextField(blank=True)
    score = models.BigIntegerField(blank=True, null=True)
    score_predicted = models.FloatField(blank=True, null=True)
    score_final = models.FloatField(blank=True, null=True)
    sentiment = models.TextField(blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    # on_delete ??? ???????????? ??????. models.CASCADE ??? ???????????????. ???????????? key??? ???????????? ???????????? ???????????? ????????????.
    # db_column='product_id' ??? ???????????? ?????? ???????????? ???????????? ????????? ????????? ???????????? ????????? ??? ??????. ????????? product_id ??????.
    # related_name??? ????????? ????????? ??? ????????? ??????. ?????? ????????? ????????? ?????????.    
    # product_id = models.ForeignKey(Products, on_delete=models.CASCADE, db_column='product_id', related_name="reviews") 
    product_id = models.BigIntegerField(blank=True, null=True) 
    product_code = models.TextField(blank=True)
    images_count = models.BigIntegerField(blank=True, null=True)
    images = models.JSONField(blank=True, null=True)
    likes_count = models.BigIntegerField(blank=True, null=True)
    plus_likes_count = models.BigIntegerField(blank=True, null=True)
    comments_count = models.BigIntegerField(blank=True, null=True)
    source = models.TextField(blank=True)
    options = models.JSONField(blank=True, null=True)
    product_options = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'
