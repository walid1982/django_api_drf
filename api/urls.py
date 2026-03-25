from django.urls import path
from . import views

urlpatterns = [
    # /api/v1/students sans slash final
    path('students', views.studentsView, name='api-students'),
    # /api/v1/students/ avec slash final
    path('students/', views.studentsView, name='api-students-slash'),
    # détail étudiant : /api/v1/students/<pk>/
    path('students/<int:pk>/', views.studentDetailView, name='api-student-detail'),

    # path('employees/', views.employeesView, name='api-employees'),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view()),
    
    # blogs endpoints
    path('blogs/', views.Blogs.as_view()),
    path('blogs/<int:pk>/', views.BlogDetail.as_view()),

    path('bloogers/', views.Bloogers.as_view()),
    path('bloogers/<int:pk>/', views.BloogerDetail.as_view()),

    # comments endpoints
    path('comments/', views.Comments.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]