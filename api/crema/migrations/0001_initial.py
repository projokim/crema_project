# Generated by Django 3.1.7 on 2021-03-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('index', models.IntegerField(blank=True, null=True)),
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('representive_score', models.FloatField(blank=True, null=True)),
                ('display', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('shop_builder_created_at', models.TextField(blank=True, null=True)),
                ('shop_builder_updated_at', models.TextField(blank=True, null=True)),
                ('reviews_count', models.IntegerField(blank=True, null=True)),
                ('org_price', models.IntegerField(blank=True, null=True)),
                ('final_price', models.IntegerField(blank=True, null=True)),
                ('product_status', models.TextField(blank=True, null=True)),
                ('image', models.JSONField(blank=True, null=True)),
                ('message_positive', models.TextField(blank=True, null=True)),
                ('top1_sentence_of_positive_reviews', models.TextField(blank=True, null=True)),
                ('top2_sentence_of_positive_reviews', models.TextField(blank=True, null=True)),
                ('top3_sentence_of_positive_reviews', models.TextField(blank=True, null=True)),
                ('top4_sentence_of_positive_reviews', models.TextField(blank=True, null=True)),
                ('top5_sentence_of_positive_reviews', models.TextField(blank=True, null=True)),
                ('related_10_reviews_with_positive', models.JSONField(blank=True, null=True)),
                ('message_negative', models.TextField(blank=True, null=True)),
                ('top1_sentence_of_negative_reviews', models.TextField(blank=True, null=True)),
                ('top2_sentence_of_negative_reviews', models.TextField(blank=True, null=True)),
                ('top3_sentence_of_negative_reviews', models.TextField(blank=True, null=True)),
                ('top4_sentence_of_negative_reviews', models.TextField(blank=True, null=True)),
                ('top5_sentence_of_negative_reviews', models.TextField(blank=True, null=True)),
                ('related_10_reviews_with_negative', models.JSONField(blank=True, null=True)),
                ('image_json', models.TextField(blank=True, null=True)),
                ('related_10_reviews_with_positive_json', models.JSONField(blank=True, null=True)),
                ('related_10_reviews_with_negative_json', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('index', models.IntegerField(blank=True, null=True)),
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('code', models.TextField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('user_code', models.TextField(blank=True, null=True)),
                ('user_name', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('message_cleaned', models.TextField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('score_predicted', models.FloatField(blank=True, null=True)),
                ('score_final', models.FloatField(blank=True, null=True)),
                ('sentiment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('product_code', models.TextField(blank=True, null=True)),
                ('images_count', models.IntegerField(blank=True, null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('likes_count', models.IntegerField(blank=True, null=True)),
                ('plus_likes_count', models.IntegerField(blank=True, null=True)),
                ('comments_count', models.IntegerField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('options', models.JSONField(blank=True, null=True)),
                ('product_options', models.JSONField(blank=True, null=True)),
                ('images_json', models.JSONField(blank=True, null=True)),
                ('options_json', models.JSONField(blank=True, null=True)),
                ('product_options_json', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reviews',
                'managed': False,
            },
        ),
    ]
