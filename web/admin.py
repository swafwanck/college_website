from django.contrib import admin
from web.models import CollegeDetail, CollegeNew, Contact, Department, Developer, Event, EventGallery, Facility, Gallery, LatestEvent, Teacher, Testimonial


class GalleryAdmin(admin.TabularInline):
    list_display = ["id"]
    model = Gallery

class TeacherAdmin(admin.TabularInline):
    list_display = ["id"]
    model = Teacher


class EventGalleryAdmin(admin.TabularInline):
    list_display = ["id"]
    model = EventGallery

class CollegeDetailAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(CollegeDetail, CollegeDetailAdmin)


class CollegeNewAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "event_date")

admin.site.register(CollegeNew, CollegeNewAdmin)


class LatestEventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date")

admin.site.register(LatestEvent, LatestEventAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "name", "designation", "company")

admin.site.register(Testimonial, TestimonialAdmin)


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("name", "designation")

admin.site.register(Developer, DeveloperAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "cap_id", "course", "dob", "gender", "father_name", "mother_name", "downloaded_date")

admin.site.register(Contact, ContactAdmin)


class FacilityAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

    inlines = [GalleryAdmin]

admin.site.register(Facility, FacilityAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

    inlines = [TeacherAdmin]

admin.site.register(Department, DepartmentAdmin)


class  EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

    inlines = [EventGalleryAdmin]

admin.site.register(Event, EventAdmin)
