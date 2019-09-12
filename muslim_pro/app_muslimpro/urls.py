from django.urls import path

from . import views

app_name = 'app_muslimpro'  # this app's name-space,
# app_name allows it to distinguish it's urls from same name urls of other app's in the same project
urlpatterns = [
    # ex: /muslimpro/
    path('', views.index, name='index'),
    path('sql_select/<sql_string>', views.any_sql, name='any_sql'),

    # simple query

    path('names_of_Allah/', views.names_of_Allah, name='names_of_Allah'),
    path('namaj_tracker/<int:user_id>', views.namaj_tracker, name='namaj_tracker'),
    path('fast_tracker/<int:user_id>', views.fast_tracker, name='fast_tracker'),
    path('show_sura_list/', views.show_sura_list, name='show_sura_list'),
    path('show_sura_of_particular_type/<type>', views.show_sura_of_particular_type, name='show_sura_of_particular_type'),
    path('show_popular_suras/', views.show_popular_suras, name='show_popular_suras'),
    path('show_suras_starting_with/<s_letter>', views.show_suras_starting_with, name='show_suras_starting_with'),
    path('show_quotes/<int:id>', views.show_quotes, name='show_quotes'),

    # complex query

    path('show_sura/<sura_name>/<language>', views.show_sura, name='show_sura'),
    path('show_nearby_places/<type>', views.show_nearby_places, name='show_nearby_places'),
    path('show_juz/<int:juz_id>/<language>', views.show_juz, name='show_juz'),
    path('next_namaj/', views.next_namaj, name='next_namaj'),
    path('show_dua/<category>/<name>/<type>/<language>', views.show_dua, name='show_dua'),
    path('any_nearby_place/<int:user_id>', views.any_nearby_place, name='any_nearby_place'),




    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('doshit/<randomstring>/', views.doshit, name='doshit'),

]
