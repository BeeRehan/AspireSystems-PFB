from django.shortcuts import render

# Create your views here.
def index(request):
    title = "Doctor page"
    return render(request,"doc_homepage.html",{'title':title})

def checklist(request):
    title = "checklist"
    return render(request,"checklist.html",{'title':title})
