from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Job
from .models import User
from .serializers import JobSerializer
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/jobs/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of jobs'
        },
        {
            'Endpoint': '/jobs/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Job object'
        },
        {
            'Endpoint': '/jobs/category/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns an array of jobs based on category'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getJobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getJob(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createJob(request):
    data = request.data
    job = Job.objects.create(
        email=data['email'],
        name=data['name'],
        location=data['location'],
        website=data['website'],
        jobTitle=data['jobTitle'],
        linkToJob=data['linkToJob'],
        jobType=data['jobType'],
        jobCategory=data['jobCategory'],
        jobDesc=data['jobDesc'],
        level=data['level'],
        img=data['img']
    )
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

# @api_view(['GET'])
# def getCategory(request, cat):
#     Jobs = Job.objects.filter(category=cat)
#     serializer = JobSerializer(Jobs, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
def register(request):
    data = request.data
    hashed_password = make_password(data['password'])
    user = User.objects.create(
        username=data['username'],
        email=data['email'],
        password=hashed_password
    )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    data = request.data
    user = User.objects.get(email=data['email'])
    check = check_password(data['password'], user.password)
    if(check):
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    else:
        return Response('Incorrect password')
