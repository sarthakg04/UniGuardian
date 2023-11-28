from django.shortcuts import render


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
