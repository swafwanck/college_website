import json

from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from main.functions import generate_form_error

from web.forms import ContactForm
from web.models import CollegeDetail, CollegeNew, Contact, Department, Developer, Event, EventGallery, Facility, Gallery, LatestEvent, Teacher, Testimonial


def index(request):
    college_details = CollegeDetail.objects.all()
    college_news = CollegeNew.objects.all() 
    latest_events = LatestEvent.objects.all()
    departments = Department.objects.all()
    testimonials = Testimonial.objects.all()
    developers = Developer.objects.all()
    facilities = Facility.objects.all() 
    events = Event.objects.all()

    context = {
        "title" : "Jamia Nadwiyya Art Science College",
        "college_details" : college_details,
        "college_news" : college_news,
        "latest_events" : latest_events,
        "departments" : departments,
        "testimonials" : testimonials,
        "developers" : developers,
        "facilities" : facilities,
        "events": events,
    }

    return render(request, 'web/index.html', context=context)


def form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            response_data ={
                "title" : "Successfully Registered your form",
                "message" : "Thank you of choosing JNE",
                "status" : "success",
                "redirect" : "yes",
                "redirect_url" : "download/"+ str(instance.id)
            }
        
        else:
            error_message = generate_form_error(form)
            response_data = {
                "title" : "From validation error",
                "message" : str(error_message),
                "status" : "error",
                "stable" : "yes",
                }
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        data = {
            "full_name" :  "hello",
            "email" : "hello@example.com",
            "cap_id" : "123",
            "course" : "bca",
            "dob" : "2001-05-24",
            "gender" : "male",
            "student_number" : "+12125552368",
            "father_name" : "John",
            "mother_name" : "John",
            "parent_number" : "+12125552368",
            "institution" : "pvs",
            "month_and_year" : "2001",
            "course_selected_for_plus_two" : "science",
            "percentage_obtained" : "75%",
            "downloaded_date" : "2001-02-24",
        }
        form = ContactForm(initial=data)

        context = {
            "title" : "JNE | Application form",
            "form" : form,
        }

        return render(request, 'form/form.html', context=context)


def download(request, id):
    # form = Contact.objects.filter().latest("id")
    form = get_object_or_404(Contact, id=id)

    context = {
        "title" : "JNE | Application form download",
        "form" : form,
    }

    return render(request, 'form/pdf.html', context=context)
   
   
def facility(request, id):
    facilities = get_object_or_404(Facility, id=id)

    if Gallery.objects.filter(facility=facilities).exists():
        galleries = Gallery.objects.filter(facility=facilities)

        context = {
            "title" : "JNE | Facilities",
            "facilities" : facilities,
            "galleries" : galleries,
        }

        return render(request, 'single page/facility.html', context=context)


def department(request, id):
    department = get_object_or_404(Department, id=id)
    teachers = Teacher.objects.filter(department=department)

    context = {
        "title" : "JNE | Department",
        "department" : department,
        "teachers" : teachers,
    }

    return render(request, 'single page/department.html', context=context)


def event(request, id):
    events = get_object_or_404(Event, id=id)
    event_gallery = EventGallery.objects.filter(event=events)

    context = {
        "title" : "JNE | Events",
        "events" : events,
        "event_gallery" : event_gallery,
    }

    return render(request, 'single page/event.html', context=context)