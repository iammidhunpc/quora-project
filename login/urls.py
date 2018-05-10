from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('adminlogin', views.LogAdminView.as_view(), name="adminlogin"),
    path('question_detail/<int:qid>/', views.AnswerView.as_view(), name="questiondetail"),

    path('answer_detail/<int:aid>/', views.CommentView.as_view(), name="answerdetail"),

    path('delete_detail/<int:did>/', views.DeleteView.as_view(), name="deletedetail"),
    path('deleteans_detail/<int:daid>/', views.DeleteansView.as_view(), name="deleteansdetail"),

    path('questap', views.QuestapView.as_view(), name="questap"),
    path('questap/<int:statusid>/', views.StatusView.as_view(), name="questap1"),
    path('ansap', views.AnsapView.as_view(), name="ansap"),
    path('ansap/<int:statusansid>/', views.StatusAnsView.as_view(), name="ansap1"),



    path('logout/', auth_views.LogoutView.as_view(next_page='/login/home'), name='logout'),

    path('registration/<str:key>/',  views.RegistrationSuccess.as_view(), name='product_success'),


]
