
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from django.urls import path, include
from administrator import views, generic, generic_csv, impersonate
from administrator.generic_pdf import generate_pdf
from adminsettings import commonsettings

urlpatterns = [
    # overwrite django buildin urls start
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>/', 
        auth_view.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('user/', views.list_user, name='list_user'),
    path('group/', views.list_group, name='list_group'),
    path('log/', views.list_logentry, name='list_logentry'),
    path('impersonate/<int:user_id>/', impersonate.impersonate_user, name='impersonate_user'),
    path('stop-impersonating/', impersonate.stop_impersonating, name='stop_impersonating'),

    # django overwrite buildin urls end buildin auth urls start
    path('', include('django.contrib.auth.urls')), 

    # django buildin auth urls end admininstrator urls starts
    path('', views.dashboard, name='dashboard'),
    path('change_password/', views.password_change_request, name='change_password'),
    path('signup/', views.register, name='signup'), 
    path('international_region/', views.list_internationalregion, name='list_internationalregion'), 
    path('country/', views.list_country, name='list_country'),
    path('subscription/plan/', views.list_subscriptionplan, name='list_subscriptionplan'),
    path('sitesettings/', views.list_sitesettings, name='list_sitesettings'),
    path('siteuser/', views.list_siteuser, name='list_siteuser'),
    path('company_settings/', views.company_settings, name='company_settings'),
    path('access_model_settings/', views.access_model_add, name='access_model_settings'),
    path('backup_db/', generic.backup_database, name='backup_database'),

    # admininstrator urls end and generic urls start
    path('add/<str:model_name>/<int:columns>/', generic.add, name='add'),
    path('add/<str:model_name>/<int:columns>/<str:m2m>/', generic.add, name='add_with_m2m'),
    path('add_fk/<str:model_name>/<str:app_name>/<str:field_name>/<int:fk_id>', generic.add_fk, name='add_with_fk'),
    path('change/<int:id>/<str:app_name>/<str:model_name>/<int:columns>/', generic.change, name='change'),
    path('change/<int:id>/<str:app_name>/<str:model_name>/<int:columns>/<str:m2m>', generic.change, name='change_with_m2m'),
    path('change_fk/<int:id>/<str:app_name>/<str:model_name>/<int:fk_id>/', generic.change_fk, name='change_with_fk'),
    path('view/<int:id>/<str:app_name>/<str:model_name>/<int:columns>/', generic.view, name='view'),
    path('view_fk/<int:id>/<str:app_name>/<str:model_name>/<int:fk_id>/', generic.view_fk, name='view_with_fk'),
    path('delete/<int:id>/<str:app_name>/<str:model_name>/', generic.delete, name='delete'),
    path('delete_fk/<int:id>/<str:app_name>/<str:model_name>/<int:fk_id>/', generic.delete_fk, name='delete_fk'),
    path('delete/multiple/', generic.delete_multiple, name='delete_multiple'), 
    path('export/pdf/<str:app_name>/<str:model_name>/', generate_pdf, name='export_pdf'), 
    path('export/csv/<str:app_name>/<str:model_name>/', generic_csv.export_to_csv, name='export_csv'), 
    path('import/csv/<str:app_name>/<str:model_name>/', generic_csv.upload_csv_file, name='import_csv'), 
    path('create/csv/<str:app_name>/<str:model_name>/', generic_csv.create_csv, name='create_csv'),
    path('user_active_status/', views.toggle_user_active_status, name='user_active_status'), 
    path('user_admin_status/', views.toggle_user_admin_status, name='user_admin_status'), 

    # generic urls end
    # shohoj it urls
    path('slider/', views.list_slider, name='list_slider'),
    path('stats/', views.stats_settings, name='stats_settings'),
    path('home-about-section/', views.home_about_section_settings, name='home_about_section_settings'),
    path('home-about-feature/', views.list_homeaboutfeature, name='list_homeaboutfeature'),
    path('contact-us/', views.contact_us_settings, name='contact_us_settings'),
    path('testimonials/', views.list_testimonials, name='list_testimonials'),
    path('testimonials-images/', views.list_testimonialsimages, name='list_testimonialsimages'),
    path('team-category/', views.list_teamcategory, name='list_teamcategory'),
    path('team-members/', views.list_teammembers, name='list_teammembers'),
    path('gallery-category/', views.list_gallerycategory, name='list_gallerycategory'),
    path('gallery-images/', views.list_galleryimages, name='list_galleryimages'),
    path('messages/', views.list_messages, name='list_messages'),
    path('services/', views.list_service, name='list_service'),
    path('faq/', views.list_faq, name='list_faq'),
    path('our-journey/', views.list_ourjourney, name='list_ourjourney'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# social login allauth urls
if commonsettings.DASHBOARD_CONFIG == 'web':
    urlpatterns += [
        path('accounts/', include('allauth.urls')), 
    ]