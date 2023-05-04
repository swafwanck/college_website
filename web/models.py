import datetime

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


COURSE = (
    ("bca", "BCA"),
    ("bba", "BBA"),
    ("bcom", "BCOM"),
    ("ba-english", "BA-ENGLISH"),
    ("bsc-physics", "BSC-PHYSICS"),
    ("mcom", "MCOM"),
    ("msc-physics", "MSC-PHYSICS"),
)

GENDER = (
    ("male", "MALE"),
    ("female", "FEMALE"),
    ("other", "OTHER"),
)


class CollegeDetail(models.Model):
    icon = models.CharField(max_length=150)
    count = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CollegeNew(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()

    def __str__(self):
        return self.title


class LatestEvent(models.Model):
    image = models.ImageField(upload_to="Latest_event/")
    title = models.CharField(max_length=250)
    event_date = models.DateField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="Testimonial/")
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    company = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Developer(models.Model):
    image = models.ImageField(upload_to="Developer/")
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    linkedin_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    cap_id = models.CharField(max_length=50)
    course = models.CharField(max_length=128, choices=COURSE)
    dob = models.DateField()
    gender = models.CharField(max_length=128, choices=GENDER)
    student_number = PhoneNumberField()
    father_name = models.CharField(max_length=128)
    mother_name = models.CharField(max_length=128)
    parent_number = PhoneNumberField()
    institution = models.CharField(max_length=128)
    month_and_year =  models.CharField(max_length=128)
    course_selected_for_plus_two = models.CharField(max_length=128)
    percentage_obtained = models.CharField(max_length=128)
    downloaded_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name


class Facility(models.Model):
    featured_image = models.ImageField(upload_to="facilities/featured_images")
    title = models.CharField(max_length=150)
    staff_count = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "facilities"
        
    def __str__(self):
        return self.title


class Gallery(models.Model):
    facility = models.ForeignKey("Facility", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="facility/gallery/")
    class Meta:
        verbose_name_plural = "gallery"      

    def __str__(self):
        return str(self.id)


class Department(models.Model):
    image = models.ImageField(upload_to="hod/image/")
    name = models.CharField(max_length=200)
    number = PhoneNumberField()
    short_title = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class Teacher(models.Model):
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="teacher/image/")
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Event(models.Model):
    featured_image = models.ImageField(upload_to="event/featured_image/")
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EventGallery(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="event/gallery/")

    class Meta:
        verbose_name_plural = "Event Gallery"      

    def __str__(self):
        return str(self.id)