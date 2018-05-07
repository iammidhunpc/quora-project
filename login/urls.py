from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'login'
urlpatterns = [
    path('home', views.HomeView.as_view(), name="home"),
    path('index', views.IndexView.as_view(), name="index"),
    path('display', views.DisplayView.as_view(), name="display"),
    path('log', views.LogView.as_view(), name="log"),
    path('success', views.SuccessView.as_view(), name="success"),
    path('failed', views.FailedView.as_view(), name="failed"),
    path('answer', views.AnswerView.as_view(), name="answer"),
    path('admin', views.AdminView.as_view(), name="admin"),
    path('question_detail/<int:qid>/', views.AnswerView.as_view(), name="questiondetail"),

    path('answer_detail/<int:aid>/', views.CommentView.as_view(), name="answerdetail"),

    path('delete_detail/<int:did>/', views.SuccessView.as_view(), name="deletedetail"),
    path('deleteans_detail/<int:daid>/', views.DeleteansView.as_view(), name="deleteansdetail"),

    path('questap', views.QuestapView.as_view(), name="questap"),
    path('ansap', views.AnsapView.as_view(), name="ansap"),

]
