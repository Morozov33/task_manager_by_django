"""todos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from task_manager.views import (HomeView, LoginView, LogoutView, UsersList,
                                UserCreateView, UserUpdateView, UserDeleteView,
                                StatusesList, StatusCreateView,
                                StatusUpdateView, StatusDeleteView, TaskView,
                                TasksList, TaskCreateView, TaskUpdateView,
                                TaskDeleteView, LabelsList, LabelCreateView,
                                LabelUpdateView, LabelDeleteView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UsersList.as_view(), name='users_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(),
         name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(),
         name='user_delete'),
    path('statuses/', StatusesList.as_view(), name='statuses_list'),
    path('statuses/create/', StatusCreateView.as_view(),
         name='status_create'),
    path('statuses/<int:pk>/update/', StatusUpdateView.as_view(),
         name='status_update'),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(),
         name='status_delete'),
    path('tasks/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('tasks/', TasksList.as_view(), name='tasks_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(),
         name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(),
         name='task_delete'),
    path('labels/', LabelsList.as_view(), name='labels_list'),
    path('labels/create/', LabelCreateView.as_view(), name='label_create'),
    path('labels/<int:pk>/update/', LabelUpdateView.as_view(),
         name='label_update'),
    path('labels/<int:pk>/delete/', LabelDeleteView.as_view(),
         name='label_delete'),
]
