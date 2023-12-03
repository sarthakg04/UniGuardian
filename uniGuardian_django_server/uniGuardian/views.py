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
from .resume_parser import load_resume, call_palm_api
from .hightlight_profiler import get_hightlight
from .ai_content_detection import detect_ai_content
from .api_key_decoder import decode_openai_api_key
from .psychometric_profiler import create_user_profile, modify_user_persona
from rest_framework.decorators import api_view
import textract
import datetime 
import json
import time



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


@csrf_exempt
def index(request):
    if request.method == 'POST':
        process_files(request)
        print("success!")
        return dashboard_view(request)
    return render(request, 'index.html')


def process_files(request):
    resume_text = ""
    sop_text = ""
    lor1_text = ""
    lor2_text = ""
    palm_api_key = "AIzaSyB1Y9HF5GBUAKXBa-d3-1G_IxKKU93cFI8"
    sapling_api_key = "PX41HQGZ4FAV34HWVO3BQAOGULQH91AQ"
    openai_api_key_encoded = "T+mnB4EvhF+ePmHgxcTOv6ceIiSH+yRa/YjJubjeGkkvNf3j4/MhbY7Ie88QQBwZcAGK*Q4jd/UhZk0zh4VCrTZ74aw==*yRrvju6EUWgCzB9z0Zi7VQ==*mIEiCkl2eAYbljkd8Mr+iQ=="
    humanticai_api_key = "chrexec_96effa3d5b5f3c0de52193e04e91e087"
    psychometrics_json_text = ""
    analysis_text = ""
    openai_api_key = decode_openai_api_key(openai_api_key_encoded)
    print(openai_api_key)

    student_name = request.GET.get('fullname', '')
    cur_time = datetime.datetime.now()

    if 'resume' in request.FILES:
        file_resume = request.FILES['resume']
        with open('../Materials/UploadFiles/resume.pdf', 'wb+') as dest:
            for chunk in file_resume.chunks():
                dest.write(chunk)
        resume_text = load_resume('../Materials/UploadFiles/resume.pdf')
        print(type(resume_text))
        analysis_text = call_palm_api(resume_text, palm_api_key)
        resume_text = str(textract.process('../Materials/UploadFiles/resume.pdf', method='pdfminer'))
        print(analysis_text)

    if 'sop' in request.FILES:
        file_sop = request.FILES['sop']
        with open('../Materials/UploadFiles/sop.pdf', 'wb+') as dest:
            for chunk in file_resume.chunks():
                dest.write(chunk)
        PERSONA = "hiring"
        sop_text = str(textract.process('../Materials/UploadFiles/sop.pdf', method='pdfminer'))
        # create_user_profile(humanticai_api_key, student_name, '../Materials/UploadFiles/sop.pdf')
        # statu_code, psychometrics_json_text = modify_user_persona(humanticai_api_key, student_name, PERSONA)
        # print(psychometrics_json_text)

    if 'lor1' in request.FILES:           
        file_lor1 = request.FILES['lor1']
        with open('../Materials/UploadFiles/lor1.pdf', 'wb+') as dest:
            for chunk in file_lor1.chunks():
                dest.write(chunk)
        lor1_text = str(textract.process('../Materials/UploadFiles/lor1.pdf', method='pdfminer'))
        
    if 'lor2' in request.FILES:           
        file_lor1 = request.FILES['lor2']
        with open('../Materials/UploadFiles/lor2.pdf', 'wb+') as dest:
            for chunk in file_lor1.chunks():
                dest.write(chunk)
        lor2_text = str(textract.process('../Materials/UploadFiles/lor2.pdf', method='pdfminer'))
        print(type(lor2_text))


    resume_json_object = json.loads(analysis_text)
    email_address = resume_json_object["Email"]

    hightlight_text = get_hightlight(resume_text, sop_text, lor1_text, lor2_text, openai_api_key)
    ai_content_score = detect_ai_content(sapling_api_key, sop_text)

    user = UserProfile(email = email_address, createdAt = cur_time, raw_resume = resume_text, raw_sop = sop_text, raw_lor1 = lor1_text, raw_lor2 = lor2_text, psychometrics = psychometrics_json_text, analysis = analysis_text, hightlight = hightlight_text, ai_detection_score = ai_content_score)
    user.save()

    fetch_user_profile_test(email_address)


def fetch_user_profile_test(email):
    # find tutorial by pk (email)
    user_profile_data = UserProfile.objects.get(pk=email)
    user_profile_serializer = UserProfileSerializer(user_profile_data)
    print(user_profile_serializer.data)



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
