from django.urls import path,include
import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('content',blog.views.article_content),
    path('index2',blog.views.get_index_page),
    path('index',blog.views.get_index_page2),
    path('about',blog.views.get_about_page),
    path('achievements',blog.views.get_achievements_page),
    path('contact',blog.views.get_contact_page),
    path('detail',blog.views.get_detail_page),
    path('list',blog.views.get_list_page),
    path('people',blog.views.get_people_page),
    path('people-detail/<int:id>',blog.views.get_people_detail_page),
    path('resources',blog.views.get_resources_page),
    #path('detail',blog.views.get_detail_page),
    path('detail/<int:article_id>', blog.views.get_detail_page),

    path('peopleuse',blog.views.get_people_vue),
    path('articleuse',blog.views.article_content_vue),
    path('education',blog.views.people_education_vue),
    path('people_simple',blog.views.people_simples_vue),
    path('index_slider',blog.views.index_slider_vue),
    path('index_people',blog.views.index_people_vue),
    path('introduction',blog.views.index_introduction_vue),
    path('achievementvue',blog.views.get_achievements_vue),
    path('gerloginper',blog.views.gerloginper),
    path('getimage', blog.views.getimageuse),
    path('project_vue', blog.views.project_vue),

    path('controller', blog.views.get_ueditor_controller),
    path('TransaltePDF', blog.views.testPDF)

]