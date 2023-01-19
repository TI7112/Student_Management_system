from django.shortcuts import render , redirect
from .forms import StudentForm
from .models import Students

def homepage(req):
    form = StudentForm(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)

    return render(req, "index.html", {"form":form, "students": Students.objects.all()})


def deleteStudent(req , id):
    student= Students.objects.get(pk = id)
    student.delete()
    return redirect(homepage)

def editStudent(req , id):
    student= Students.objects.get(pk = id)
    form = StudentForm(req.POST or None , instance = student)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
    return render(req , 'edit.html' , {'form':form})


def searchStudent(req):
    if req.method == "GET":
        search_query = req.GET.get('search_keyword')
        form = StudentForm()

        data = {
            'students': Students.objects.filter(name__icontains = search_query),
            'form' : form
        }

        return render(req , 'index.html' , data)


def filterCity(req):
    if req.method == "GET":
        search = req.GET.get('city')
        form = StudentForm()
        data = {
            'students': Students.objects.filter(city = search),
            'form' : form
        }
        return render(req , 'index.html' , data)
