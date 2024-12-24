from django.urls import path
from . import views
from django.urls import path
from .views import saisie_jobs
urlpatterns = [
    path('', views.home, name='home'),
    path('probleme', views.probleme, name='probleme'),
    path('jobs',views.jobsdetail,name='jobsdetail'),
    path('contraint/',views.contraint,name='contraint'),
    path('regle',views.regle,name='regle'),
    path('afficher_donnees',views.afficher_donnees,name='afficher_donnees'),
    path('fifo-sanscontrainte/', views.fifo_sanscontrainte, name='fifo_sanscontrainte'),
    path('SDST/', views.sdst, name='sdst'),
    path('sdst_gantt/', views.sdst_gantt, name='sdst_gantt'),  # Nom de l'URL atten
    path('sist/',views.sist,name='sist'),
    path(' sist_gantt/',views. sist_gantt,name='sist_gantt'),
    path('no_wait/',views.no_wait,name='no_wait'),
    path('no_idle/',views.no_idle,name='no_idle'),
    path('probleme_optimisation/',views.probleme_optimisation,name='probleme_optimisation'),
    path('optimisation/',views.optimisation,name='optimisation'),
    path('Demande/', views.Demande, name='Demande'),
    path('TAR/', views.TAR, name='tar'),
    path('ateliersinjobshop/',views.ateliersinjobshop,name='ateliersinjobshop'),

    path('saisie_classe_12/',views.saisie_classe_12,name='saisie_classe_12'),
    path('saisie_classe_1/',views.saisie_classe_1,name='saisie_classe_1'),
    path('saisie_classe_21/',views.saisie_classe_21,name='saisie_classe_21'),
    path('saisie_classe_2/',views.saisie_classe_2,name='saisie_classe_2'),
    path('ordjobshop2gantt/',views.ordjobshop2gantt,name='ordjobshop2gantt'),

    path('jobs_detail2/',views.jobs_detail2,name='jobs_detail2'),
    path('probleme2/',views.probleme2,name='probleme2'),
    path('gantt_jobshop',views.gantt_jobshop,name='gantt_jobshop'),
    path('gantt_jobshopLPT',views.gantt_jobshopLPT,name='gantt_jobshopLPT'),
    path('gantt_jobshopSPT',views.gantt_jobshopSPT,name='gantt_jobshopSPT'),

    path('contraintjobshop',views.contraintjobshop,name='contraintjobshop'),

    path('setup_time_view/', views.setup_time_view, name='setup_time_view'),
    path('setup_time_gantt/', views.setup_time_gantt, name='setup_time_gantt'),
    path('display_setup_time_view/',views.display_setup_time_view,name='display_setup_time_view'),
    path('setup_time_ganttLPT/',views.setup_time_ganttLPT,name='setup_time_ganttLPT'),
    path('regleopt/',views.regleopt,name='regleopt'),
    path('vue_johnson/',views.vue_johnson,name='vue_johnson'),
    path('atelierMP/',views.atelierMP,name='atelierMP'),
    path('MP/',views.MP,name='MP'),
    path('gantt_view/',views.gantt_view,name='gantt_view'),
    path('mp_at',views.mp_at,name='mp_at'),
    path('MPr',views.MPr,name='MPr'),
    path('gantt_view_with_arrival/', views.gantt_view_with_arrival, name='gantt_view_with_arrival'),  # Vue Gantt
    path('cds_gantt',views.cds_gantt,name='cds_gantt'),
    path('K',views.k,name='k'),
    path('mpateliers',views.mpateliers,name='mpateliers')
]


