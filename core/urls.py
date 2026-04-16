"""
URL patterns for the CampusDate core app.

Maps URLs to view functions.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ── Public pages ──────────────────────────────
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ── Dashboard (browse users) ───────────────────
    path('dashboard/', views.dashboard, name='dashboard'),

    # ── Profile pages ──────────────────────────────
    # IMPORTANT: 'edit' must come BEFORE <str:username> or Django
    # will treat the word "edit" as a username and 404.
    path('profile/', views.profile, name='profile_self'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/photos/', views.manage_photos, name='manage_photos'),
    path('profile/<str:username>/', views.profile, name='profile'),

    # ── Likes & Matching ───────────────────────────
    path('like/<int:user_id>/', views.like_user, name='like_user'),
    path('matches/', views.matches, name='matches'),

    # ── Chat / Messaging ───────────────────────────
    path('chat/<int:match_id>/', views.chat, name='chat'),
    path('chat/<int:match_id>/messages/', views.get_new_messages, name='get_new_messages'),

    # ── Password Reset System ───────────────────────────

    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]
