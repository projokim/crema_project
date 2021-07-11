"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from crema import views
from django.conf import settings


router = DefaultRouter()
router.register(r'products', views.ProductView, basename='products')
router.register(r'reviews', views.ReviewView, basename='reviews')

schema_view = get_schema_view(
    openapi.Info(
        title="CREMA 데이터를 활용한 API 구축 프로젝트",
        default_version='v1',
        description="",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="juwon@juwon.com"),
        license=openapi.License(name="Datarize"),
    ),
    # validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('', include('api.urls')),
    # path("test/<int:review_id>/", views.test),
    # path('products/', views.products_list), 
    # path('products/<int:product_id>/', views.product), 
    # path('reviews/', views.reviews_list), 
    # path('reviews/<int:review_id>/', views.review),
]

# 이건 디버그일때만 swagger 문서가 보이도록 해주는 설정이라는 듯. urlpath도 이 안에 설정 가능해서, debug일때만 작동시킬 api도 설정할 수 있음.
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    ]


# url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
 
