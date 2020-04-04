# from articles.api.views import ArticleViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ArticleViewSet, base_name='articles')
# urlpatterns = router.urls

from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    
    P_ArticleListView,
    P_ArticleDetailView,
    P_ArticleCreateView
)

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    path('<pk>/update/', ArticleUpdateView.as_view()),
    path('<pk>/delete/', ArticleDeleteView.as_view()),
    
    
    path('pa', P_ArticleListView.as_view()),
    path('create/', P_ArticleCreateView.as_view()),
    path('<pk>', P_ArticleDetailView.as_view())
]
'''
urlpatterns = [
    path('pa', P_ArticleListView.as_view()),
    path('create/', P_ArticleCreateView.as_view()),
    path('<pk>', P_ArticleDetailView.as_view())
]
'''