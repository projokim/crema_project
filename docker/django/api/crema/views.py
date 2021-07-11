# from django.shortcuts import render 
# from django.http import JsonResponse 
# from django.views.decorators.csrf import csrf_exempt 
# from rest_framework.parsers import JSONParser
# from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
from .models import Products, Reviews 
from rest_framework.response import Response
from .serializers import ProductsSerializer, ProductSerializer, ReviewsSerializer, ReviewSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from .filters import ProductFilter, ReviewFilter
# import json


# json_dumps_params = {'ensure_ascii':False} 

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

# 가장 기본적인 형태
# class ProductView(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer
#     pagination_class = StandardResultsSetPagination
#     filterset_class = ProductFilter

#     ordering_fields = ['created_at',]
#     ordering = ['created_at']    

class ProductView(viewsets.ModelViewSet):
    '''
    상품 리스트 및 상세 페이지 정보
    ---
    ### 상품 리스트
    - filter : 상품등록날짜, 대표점수(예측), 판매중 여부, code, id, 최소 리뷰수
    - sort : 상품등록날짜, 대표점수(예측)
    - field : product_id, product_id_link, 이름, 등록날짜, **대표리뷰**, **대표점수**, **부정/긍정별 대표 문장** 5개, 판매중 여부 등
    - link : product_id_link -> 해당 상품 상세

    '''
    queryset = Products.objects.all()

    # 속성(queryset, serializer_class, pagination_class, filters_backend)을 먼저 지정한다. 쿼리셋 속성을 사용한다.
    # setting에서 디폴트로 지정한 것(filters_backend)들은 이미 되어있음!
    serializer_class = ProductsSerializer
    pagination_class = StandardResultsSetPagination
    # setting 에서 지정해주면 디폴트로 사용되니까 여기서 굳이 DjangoFilterBackend를 쓰지 않아도 된다.
    # 하나만 쓰면 디폴트르 덮어씌우게 된다. 즉 써준 것만 사용한다.
    # filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    # filterset_fields = ['product_status', 'code']
    # filter_class 나 filterset_class 나 똑같네...? 어느 메서드에서 사용되는 것일까...
    filterset_class = ProductFilter

    ordering_fields = ['created_at',]
    ordering = ['created_at']

    # 최대한 기존 것을 지키는 것
    def retrieve(self, request, *args, **kwargs):
        '''
        상품 상세 정보에 대한 응답을 반환
        ---
        ### 상품 상세
        - field : product_id, reviews(해당 상품의 리뷰 리스트 링크), 이름, **대표 문장과 연관된 최대 10개의 리뷰 리스트** 등 모든 상품 필드
        - link : reviews -> 해당 상품의 리뷰 리스트, 대표 문장과 연관된 최대 10개의 리뷰 리스트 → 해당 리스트 상세
        '''
        instance = self.get_object()
        self.serializer_class = ProductSerializer
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # 뷰에서 하이퍼 링크 구현
    # def retrieve(self, request, *args, **kwargs):
    # '''
    # 흠
    # '''
    #     instance = self.get_object()
    #     host_url = self.request.get_host()
        
    #     if instance.related_10_reviews_with_positive != "":
    #         instance.related_10_reviews_with_positive = ["http://" + host_url + '/reviews/' + str(review_id) for review_id in instance.related_10_reviews_with_positive]
        
    #     if instance.related_10_reviews_with_negative != "":
    #         instance.related_10_reviews_with_negative = ["http://" + host_url + '/reviews/' + str(review_id) for review_id in instance.related_10_reviews_with_negative]            
        
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


    # 쿼리셋에서 정렬을 구현할 수 있다.
    # def get_queryset(self):
    #     created_at = self.request.query_params.get("created_at", '2000-01-01')
    #     # product_status = self.request.query_params.get("product_status", 'selling')
    #     representive_score = self.request.query_params.get("representive_score", 0)

    #     return self.queryset.filter(
    #         created_at__gte=created_at, 
    #         # product_status=product_status,
    #         representive_score__gte=representive_score,
    #     )


class ReviewView(viewsets.ModelViewSet):
    '''
    리뷰 리스트 및 상세 페이지 정보
    ---
    ### 리뷰 리스트
    - filter : 리뷰등록날짜, product_id, 키워드, 점수(최종), code, id
    - sort : 리뷰등록날짜, 점수(최종)
    - field : review_id, review_id_link, product_id, 상품이름, user_id, 등록날짜 등
    - link : review_id_link -> 해당 리뷰 상세
       
    '''    
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = StandardResultsSetPagination
    filter_class = ReviewFilter
    # filterset_fields = ['created_at', 'product_id', 'product_code', 'code']
    ordering_fields = ['created_at', 'score_final']
    ordering = ['created_at']



    def retrieve(self, request, *args, **kwargs):
        '''
        ### 리뷰 상세
        - field : review_id, product_id, product_id_link, `이름, **키워드 리스트**, 등록날짜, 점수 등
        - link : product_id_link -> 해당 상품 상세         
        '''
        instance = self.get_object()
        self.serializer_class = ReviewSerializer
        serializer = self.get_serializer(instance)
        return Response(serializer.data)    


    # def get_queryset(self):
    #     created_at = self.request.query_params.get("created_at", '2000-01-01')
    #     score_final = self.request.query_params.get("score_final", 0)
    #     keyword = self.request.query_params.get("keyword", "")

    #     return self.queryset.filter(created_at__gte=created_at,
    #                                 score_final_field__gte=score_final,
    #                                 message_cleaned_field__contains = keyword)        


# -------------------------------------------------------------------------------------------     
# 테스트

# def test(request, review_id):
#     obj = Reviews.objects.get(pk=review_id)
#     if request.method == 'GET':
#         serializer = ReviewsSerializer(obj)
#         return Response(serializer.data)
        # return JsonResponse(serializer.data)

# -------------------------------------------------------------------------------------------
# 함수로만 구현하는 방법

# def products_list(request):
#     if request.method == 'GET':
#         min_score = request.query_params.get('min_score', 0)
#         product_status = request.query_params.get('product_status', 'selling')
#         request.query_params.get('created_at', '2000.00.00')

#         query_set = Products.objects.all()
#         serializer = ProductsSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False, json_dumps_params=json_dumps_params)

# def reviews_list(request):
#     if request.method == 'GET':
#         query_set = Reviews.objects.all()
#         serializer = ReviewsSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False, json_dumps_params=json_dumps_params)


# def product(request, product_id):
#     obj = Products.objects.get(pk=product_id)
#     if request.method == 'GET':
#         serializer = ProductsSerializer(obj)
#         return JsonResponse(serializer.data, safe=False, json_dumps_params=json_dumps_params)

# def review(request, review_id):
#     obj = Reviews.objects.get(pk=review_id)
#     if request.method == 'GET':
#         serializer = ReviewsSerializer(obj)
#         return JsonResponse(serializer.data, safe=False, json_dumps_params=json_dumps_params)