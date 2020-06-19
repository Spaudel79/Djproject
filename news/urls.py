from django.urls import path, re_path, include
from django.contrib.auth import views as auth_view
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blogcricket', views.blog_cricket, name='blogcricket'),
    path('blognba', views.blog_nba, name='blognba'),
    path('blogtennis', views.blog_tennis, name='blogtennis'),
    path('blogepl', views.blog_epl, name='blogepl'),
    path('blogseriea', views.blog_seriea, name='blogseriea'),
    path('bloglaliga', views.blog_laliga, name='bloglaliga'),
    path('blogcleague', views.blog_cleague, name='blogcleague'),
    path('login', views.login, name='login'),
    path('logout', views.log_out, name='logout'),
    path('users', views.users, name='users'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('reset-password', auth_view.PasswordResetView.as_view(template_name= 'reset-password.html'), name ='reset-password'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-done/', auth_view.PasswordResetDoneView.as_view(template_name='password-reset-done.html'),name='password-reset-done'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'),name='password-reset-complete'),
    path('contact', views.contact, name='contact'),
    path( 'blog-details/<int:criteria>', views.blog_details, name='blog-details'),
    path( 'blogcricket-details/<int:criteria>', views.blogcricket_details, name='blogcricket-details'),
    path('gn', views.Bloglistview.as_view(), name='gn'),
    path('delete/<int:pk>', views.Blogdeleteview.as_view(), name='delete'),
    path('gn-details/<int:pk>', views.Blogdetailview.as_view(), name='gn-details'),
    # path('users/<int: criteria>', views.users),
    # # re_path(r'gallery/(?P<gid>[0-9]{3})/$', views.gallery),
    # # path('music', include([path('/', views.music), path('/<mid>', views.music_details)]))

]
