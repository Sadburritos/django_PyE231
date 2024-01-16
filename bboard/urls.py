from django.urls import path

from .views import BbCreateView, BbDetailView, BbEditView, BbDeleteView, BbByRubricView, BbIndexView, \
    BbRedirectView, BbMonthView

app_name = "bboard"

urlpatterns = [
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),

    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),

    # path('', index, name='index'),
    path('', BbIndexView.as_view(), name='index'),
    path('year/<int:year>/', BbRedirectView.as_view(), name='redirect'),
    path('<int:year>/<int:month>/', BbMonthView.as_view(), name='month'),
]
