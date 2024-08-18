from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Loja API",
      default_version='v1',
      description="Documentação da API para a loja",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clientes.urls')),
    path('api/', include('grupos_produtos.urls')),
    path('api/', include('produtos.urls')),
    path('api/vendas/', include('vendas.urls')),
    path('api/', include('vendedores.urls')),
    path('api/', include('itens_venda.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
