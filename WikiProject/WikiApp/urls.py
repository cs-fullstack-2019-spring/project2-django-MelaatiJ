from . import views
from django.urls import path


# tells you what app g
app_name = "WikiApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("newUser/", views.newUser, name="newUser"),

    path("addWiki/", views.addWiki, name="addWiki"),
    path("eachWiki/<pk>/", views.eachWiki, name="eachWiki"),

    path("editWiki/<pk>/", views.editWiki, name="editWiki"),
    path("deleteWiki/<pk>/", views.deleteWiki, name="deleteWiki"),
    path("myWikis/", views.myWikis, name="myWikis"),
    path("allWikis/", views.allWikis, name="allWikis"),


    path("addRI/<pk>/", views.addRI, name="addRI"),
    path("editRI/<wikipk>/<ripk>/", views.editRI, name="editRI"),
    path("deleteRI/<wikipk>/<ripk>/", views.deleteRI, name="deleteRI"),
]

