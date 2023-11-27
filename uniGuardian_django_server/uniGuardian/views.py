from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt


def dashboard_view(request):
    # Dummy data to simulate what you might get from your API
    dummy_data = {
        "Name": "John Doe",
        "Contact": {
            "Email": "john@example.com",
            "Phone": "555-1234",
            "Location": "Anywhere, USA",
            "LinkedIn": "johnlinkedin",
            "Other Website": ["johnsblog.com"]
        },
        "Education": [
            {
                "Institution": "University of Example",
                "Degree": "B.S. in Computer Science",
                "Location": "Example City",
                "GPA": "3.8",
                "Dates": "2017 - 2021",
                "Courses": ["Course 1", "Course 2"]
            }
        ],
        "Work_Experience": [
            {
                "Company": "ExampleTech",
                "Title": "Software Engineer",
                "Location": "Techville",
                "Dates": "2021 - Present",
                "Responsibilities": ["Developed features", "Fixed bugs"]
            }
        ],
        "Awards_Honors": [
            {
                "Title": "Employee of the Year",
                "Date": "2022",
                "Organization": "ExampleTech",
                "Details": "For outstanding performance and dedication."
            }
        ]
    }

    return render(request, 'dashboard.html', {'resume_data': dummy_data})


@csrf_exempt
def home(request):
    template = loader.get_template('home.html')
    store_process_file(request)
    return HttpResponse(template.render())


@csrf_exempt
def file_upload(request):
    template = loader.get_template('file_upload.html')
    store_process_file(request)
    return HttpResponse(template.render())


def store_process_file(request):
    # make sure the the request method is POST
    if request.method != 'POST':
        return HttpResponseBadRequest('Only POST requests are allowed')
    # now get the uploaded file
    #file = request.FILES['applicant_file']
    for file in request.FILES.getlist('applicant_rl'):
        print(file.name)
        # the file is going to be an instance of UploadedFile
        with open('../Materials/UploadFiles/RL/%s' % file.name, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)

    for file in request.FILES.getlist('applicant_resume'):
        print(file.name)
        # the file is going to be an instance of UploadedFile
        with open('../Materials/UploadFiles/Resume/%s' % file.name, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)

    for file in request.FILES.getlist('applicant_sop'):
        print(file.name)
        # the file is going to be an instance of UploadedFile
        with open('../Materials/UploadFiles/SOP/%s' % file.name, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)


@csrf_exempt
def file_upload_resume(request):
    template = loader.get_template('file_upload_resume.html')
    store_process_file(request)
    return HttpResponse(template.render())


@csrf_exempt
def file_upload_sop(request):
    template = loader.get_template('file_upload_sop.html')
    store_process_file(request)
    return HttpResponse(template.render())


@csrf_exempt
def file_upload_rl(request):
    template = loader.get_template('file_upload_rl.html')
    store_process_file(request)
    return HttpResponse(template.render())

