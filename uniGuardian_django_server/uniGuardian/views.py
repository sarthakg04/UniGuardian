from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from uniGuardian.models import UserProfile
from uniGuardian.serializers import UserProfileSerializer
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
