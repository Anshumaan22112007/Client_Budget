from django.shortcuts import render

# Create your views here.


clientlist=[]


def home(request):
    return render(request, 'client/home.html')

def add(request):
    if request.POST :
        project={}

        project['client_name']=request.POST['client_name']
        project['project_name']=request.POST['project_name']
        project['budget'] = request.POST['budget']

        clientlist.append(project)


        return render(request,'client/new.html' , {"record":"You added Your Project Details Successfully."})

    else:
        return render(request, "client/new.html", {"record": ""})


def view(request):
    return render(request,'client/view.html',
    {"clientlist": clientlist})
