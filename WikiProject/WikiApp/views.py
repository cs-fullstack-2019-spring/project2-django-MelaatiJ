from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import WikiEntryModel, RIEntryModel
from .forms import NewUserForm, WikiEntryForm, RIEntryForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q

# Create your views here.
# currentUser = get_user_model()
currentUser = settings.AUTH_USER_MODEL


def myWikis(request):
    # if the user is logged in
    if request.user.is_authenticated:
        # get the current user with the request
        currentUser = request.user
        # filter objects to current user
        myWikis = WikiEntryModel.objects.filter(creator=currentUser)
        # print(myWikis[0].title)
    else:
        # pass it through a string to the webpage
        myWikis = ""
        # put it in my htmk
    context = {
        "myWikis": myWikis
    }
    return render(request, "WikiApp/myWiki.html", context)


def newUser(request):
    form = NewUserForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
            return redirect("WikiApp:index")

    context = {
        "form": form

    }
    return render(request, "WikiApp/newUser.html", context)


def addWiki(request):
    form = WikiEntryForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        currentUser = User.objects.get(username=request.user)
        WikiEntryModel.objects.create(title=request.POST["title"], text=request.POST['text'],
                                      createdDate=request.POST['createdDate'], updatedDate=request.POST["updatedDate"],
                                      image=request.FILES['image'], creator=currentUser)
        return redirect("WikiApp:myWikis")

    return render(request, "WikiApp/addWiki.html", context)


def editWiki(request, pk):
    if request.user.is_authenticated:
        wiki = get_object_or_404(WikiEntryModel, pk=pk)
        newWiki = WikiEntryForm(request.POST or None, instance=wiki)
        context = {
            "newWiki": newWiki
        }
        # validation
        if newWiki.is_valid():
            # save wiki
            newWiki.save()
            return redirect("WikiApp:eachWiki", pk)
        return render(request, "WikiApp/editWiki.html", context)

    return redirect("WikiApp:eachWiki", pk)



def deleteWiki(request, pk):
    if request.user.is_authenticated:
        wiki = get_object_or_404(WikiEntryModel, pk=pk)
        if request.method == 'POST':
            # delete
            wiki.delete()
            return redirect('WikiApp:myWikis')
        context = {
            "wiki": wiki
        }
        return render(request, "WikiApp/deleteWiki.html", context)


def index(request):
    return render(request, "WikiApp/index.html")


def allWikis(request):
    # get all wikis
    wikis = WikiEntryModel.objects.all()
    context = {
        "allWikis": wikis
    }

    return render(request, "WikiApp/allWikis.html", context)


def addRI(request, pk):
    # get form and files
    # files for images because you used a file field
    form = RIEntryForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    # if method equals post
    if request.method == "POST":
        # filter to selected wiki by primary key
        selectedWikis = WikiEntryModel.objects.filter(pk=pk)
        # filter returns a list even thoigh there is only one in the list because of its primary key
        # but you still habe to reqest the first so no error is present
        wiki = selectedWikis.first()
        print(request.POST)
        print(request.FILES)
        # create new form
        RIEntryModel.objects.create(title=request.POST["title"],
                                    text=request.POST["text"],
                                    image=request.FILES["image"],
                                    wiki=wiki)
        return redirect("WikiApp:eachWiki", pk)
    return render(request, "WikiApp/addRI.html", context)


def editRI(request, wikipk, ripk):
    RI = get_object_or_404(RIEntryModel, pk=ripk)
    newRI = RIEntryForm(request.POST or None, instance=RI)
    if newRI.is_valid():
        newRI.save()
        return redirect("WikiApp:eachWiki", wikipk)
    context = {
        "newRI": newRI
    }
    return render(request, "WikiApp/editRI.html", context)


def deleteRI(request, wikipk, ripk):
    RI = get_object_or_404(RIEntryModel, pk=ripk)
    if request.method == 'POST':
        RI.delete()
        return redirect('WikiApp:eachWiki', wikipk)
    context = {
        "RI": RI
    }
    return render(request, "WikiApp/deleteRi.html", context)


def eachWiki(request, pk):
    # using filter to return that it doesnt exist
    # QS stants for querdy set because filter returns a list
    QS = WikiEntryModel.objects.filter(pk=pk)
    wiki = QS.first()
    # retrieves a list of related items
    RIQS = RIEntryModel.objects.filter(wiki=wiki)
    context = {
        "wiki": wiki,
        "RIS": RIQS
    }

    return render(request, "WikiApp/eachWiki.html", context)

def search(request):
    search=request.POST['search']
    wikiSearch = WikiEntryModel.objects.filter(Q(title__icontains=search) or Q(text__icontains=search))
    context = {
        "wikiSearch": wikiSearch
    }
    return render(request, "WikiApp/searchResults.html", context)

