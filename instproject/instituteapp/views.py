from django.shortcuts import render
from.models import FeedbackData,ContactData,CourseData
from.forms import FeedbackForm,ContactForm
from django.http.response import HttpResponse
import datetime
date1=datetime.datetime.now()
import datetime
start_date=datetime.datetime.now()

def main_page(request):
    return render(request,'basehome.html')


def home(request):
    return render(request,'home_view.html')


def courses (request):
    course= CourseData.objects.all()
    return render(request,'courses.html',{'course':course})


def contact(request):
    if request.method == "POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name=cform.cleaned_data.get('name')
            email=cform.cleaned_data.get('email')
            mobile=cform.cleaned_data.get('mobile')
            courses=cform.cleaned_data.get('courses')
            shifts=cform.cleaned_data.get('shifts')
            locations=cform.cleaned_data.get('locations')
            gender=cform.cleaned_data.get('gender')
            # start_date=cform.cleaned_data.get('stat_date')
            data=ContactData(
                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                shifts=shifts,
                locations=locations,
                gender=gender,
                start_date=start_date
            )
            data.save()
            cform = ContactForm()
            cdata=ContactData.objects.all()
            return render(request , 'contact.html' , {'cform':cform,'cdata':cdata})
        else:
            return HttpResponse("User Invelid Data")
    else:
        cform = ContactForm()
        cdata = ContactData.objects.all()
        return render(request, 'contact.html', {'cform': cform,'cdata':cdata})


def feedback(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform=FeedbackForm()
            fdata=FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'fdata':fdata})
        else:
            return HttpResponse("invalid User Data")

    else:
        fform=FeedbackForm()
        fdata=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'fdata':fdata})




def team(request):
    return render(request,'team.html')


def gellery(request):
    return render(request,'gellery.html')