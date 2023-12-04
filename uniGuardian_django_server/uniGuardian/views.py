from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.decorators import api_view


@api_view(['POST', 'DELETE'])
def create_user_profile(request):
    if request.method == 'POST':
        user_profile_data = JSONParser().parse(request)
        user_profile_serializer = UserProfileSerializer(data=user_profile_data)
        if user_profile_serializer.is_valid():
            user_profile_serializer.save()

            return JsonResponse(user_profile_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET list of tutorials, POST a new tutorial, DELETE all tutorials


@api_view(['GET'])
def fetch_user_profile(request, email):
    # find tutorial by pk (email)
    try:
        user_profile_data = UserProfile.objects.get(pk=email)
        user_profile_serializer = UserProfileSerializer(user_profile_data)
        return JsonResponse(user_profile_serializer.data)
    except UserProfile.DoesNotExist:
        return JsonResponse({'message': 'The profile does not exist'}, status=status.HTTP_404_NOT_FOUND)


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def dashboard_view(request):
    # Dummy data to simulate what you might get from your API
    context = {
        "personal_details": {
            "name": "Kshitiz Dhyaani",
            "course": "Master’s in Computer Science Engineering",
            "semester": "Fall’25",
            "course_type": "Full Time Course",
            "avatar_url": "uniGuardian/avatar.png"  # URL or path to the avatar image
        },
        "key_highlights": {
            "summary": "Kshitiz Dhyani, a Gold Medalist from IIT Kanpur, demonstrated expertise as a Quantitative Trader at AlphaGrep, formulating optimal trading strategies and ensuring regulatory compliance. He further showcased technical prowess at Georgia Tech and Rivian, developing neural networks for Brain Imagery and optimizing fleet management systems. His accomplishments are backed by high-impact academic recommendations.",
            "percentage_written_by_ai": 3
        },
        "academic_history": [
            "Bachelor’s in Computer Engineering, Indian Institute of Technology, Kanpur",
            "Senior Secondary School STEM, City Montessori School, Lucknow",
            "High School, City Montessori School, Lucknow"
        ],
        "highlights": [
            "Gold Medalist Cultural Secretary of Techkriti, 3.8/4, Dean’s List",
            "91%, CBSE Good Academic History",
            "89%, CBSE Fair Academic History"
        ],
        "professional_experience": [
            {
                "title": "AlphaGrep : Software Engineer",
                "details": [
                    "Algorithm Mastery: Crafted optimal trading strategies",
                    "Financial Insight: Delved deep into market analysis",
                    "Risk Management: Employed quantitative safety techniques",
                    "Performance Tracking: Monitored using rigorous metrics",
                    "Compliance Adherence: Upheld strict regulatory standards"
                ]
            },
            {
                "title": "Georgia Tech : Research Intern",
                "details": [
                    "Internship Experience: Interned under Dr. Eva Dyer, NerDS Lab",
                    "Technical Design: Designed neural network for Brain Imagery",
                    "Data Analysis: Formulated perceptual ranking dataset; assessed performance"
                ]
            },
            {
                "title": "Rivian : Software Engineer Intern",
                "details": [
                    "System Design: Designed High-Throughput Fleet Management Systems",
                    "Vision Solutions Deployment: Deployed 133 Factory Vision Solutions resulting in a 13% reduction in cycle-time",
                    "Code Optimization: Optimized Legacy Code, boosting software performance by 20%"
                ]
            }
            # Add other experiences as needed
        ],
        "psychometric_evaluation": {
            "image_url": "psychometric_graph.png"  # URL or path to the psychometric evaluation image
        },
        "skills": [
            "Python, C++, JavaScript, SQL, Bash, Golang",
            "Django, Flask, NodeJS, ReactJS, Scikit, Boto3, TensorFlow",
            "Kubernetes, Docker, GIT, PostgreSQL, MySQL, SQLite",
            "Linux, Web, AWS, Google Cloud Platform, Snowflake, Airflow"
                ],
    }
    return render(request, 'dashboard.html', context)


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

