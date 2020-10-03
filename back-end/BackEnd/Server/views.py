from django.shortcuts import render
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Server import models
from django.contrib.auth.models import User
from rest_framework import viewsets
from Server import serializers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import datetime



class Register(APIView):

    def post(self, request):
        user = serializers.ProfileSerializer.create(serializers.ProfileSerializer(), request.data)
        serializer = serializers.ProfileSerializer(user)
        return Response("Done")

class CandidateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
            profiles = models.Profile.objects.all()
            content_arr = []
            for temp in profiles:
                user = temp.user
                profile = temp
                content = {'id': user.id, 'first_name': user.first_name, 'email': user.email,
                           'last_name': user.last_name, 'status': profile.status, 'post': profile.post,
                           'company': profile.company}
                content_arr.append(content)
            serializer = serializers.ProfileSerializer(content_arr, many=True)
            return Response(serializer.data)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

            user = request.user
            profile = models.Profile.objects.get(user=user)
            content = {'id': user.id, 'first_name': user.first_name, 'email': user.email,
                       'last_name': user.last_name, 'status': profile.status, 'post': profile.post,
                       'company': profile.company}
            serializer = serializers.ProfileSerializer(content)
            return Response(serializer.data)


    def put(self, request):
        user = request.user
        profile = serializers.ProfileSerializer.update(serializers.ProfileSerializer(), request.data, user)
        user = profile.user
        content = {'id': user.id, 'first_name': user.first_name, 'email': user.email,
                   'last_name': user.last_name, 'status': profile.status, 'post': profile.post,
                   'company': profile.company}
        serializer = serializers.ProfileSerializer(content)
        return Response(serializer.data)

    def delete(self, request):
        user = request.user
        serializers.ProfileSerializer.delete(serializers.ProfileSerializer(), request.data, user)
        return Response("Done")


class SessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        session = models.Session.objects.filter(username=request.data['username'])
        serializer = serializers.SessionSerializer(session, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        user2 = models.User.objects.get(id=request.data['user_id'])
        session = serializers.SessionSerializer.create(serializers.SessionSerializer(), request.data, user, user2)
        serializer = serializers.SessionSerializer(session)
        return Response(serializer.data)

    def put(self, request):
        session = serializers.SessionSerializer.update(serializers.SessionSerializer(), request.data)
        serializer = serializers.SessionSerializer(session)
        return Response(serializer.data)

    def delete(self, request):
        serializers.SessionSerializer.delete(serializers.SessionSerializer(), request.data)
        return Response("Done")


class SessionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        session = models.Session.objects.filter(creator=user)
        serializer = serializers.SessionSerializer(session, many=True)
        return Response(serializer.data)

class GETSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        session = models.Session.objects.get(id=request.GET['id'])
        serializer = serializers.SessionSerializer(session)
        return Response(serializer.data)

class SessionCandidateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        session = models.Session.objects.filter(candidate=user)
        serializer = serializers.SessionSerializer(session, many=True)
        return Response(serializer.data)


class MessageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        message = models.Message.objects.filter(id=request.data['id'])
        serializer = serializers.MessageSerializer(message, many=True)
        return Response(serializer.data)

    def post(self, request):
        session = models.Session.objects.filter(id=request.data['session_id'])
        message = serializers.MessageSerializer.create(serializers.MessageSerializer(), request.data, session)
        serializer = serializers.MessageSerializer(session)
        return Response(serializer.data)

    def put(self, request):
        message = serializers.MessageSerializer.update(serializers.MessageSerializer(), request.data)
        serializer = serializers.MessageSerializer(message)
        return Response(serializer.data)

    def delete(self, request):
        serializers.MessageSerializer.delete(serializers.MessageSerializer(), request.data)
        return Response("Done")


class MessageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        session = models.Session.objects.filter(id=request.data['session_id'])
        message = models.Message.objects.filter(session=session)
        serializer = serializers.MessageSerializer(message, many=True)
        return Response(serializer.data)


class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        task = models.Task.objects.filter(id=request.data['id'])
        serializer = serializers.TaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        task = serializers.TaskSerializer.create(serializers.TaskSerializer(), request.data, user)
        serializer = serializers.TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request):
        task = serializers.TaskSerializer.update(serializers.TaskSerializer(), request.data)
        serializer = serializers.TaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request):
        serializers.TaskSerializer.delete(serializers.TaskSerializer(), request.data)
        return Response("Done")


class AllTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        task = models.Task.objects.filter(user=user)
        serializer = serializers.TaskSerializer(task, many=True)
        return Response(serializer.data)

class CandidateTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        task = models.Task.objects.all()
        serializer = serializers.TaskSerializer(task, many=True)
        return Response(serializer.data)


class TaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        session = models.Session.objects.get(id=request.GET['session_id'])
        tasklist = models.TaskList.objects.filter(session=session)
        serializer = serializers.TaskListSerializer(tasklist, many=True)
        return Response(serializer.data)

    def post(self, request):
        session = models.Session.objects.get(id=request.data['session_id'])
        task = models.Task.objects.get(id=request.data['task_id'])
        tasklist = serializers.TaskListSerializer.create(serializers.TaskListSerializer(), request.data, session, task)
        serializer = serializers.TaskListSerializer(tasklist)
        return Response(serializer.data)

    def put(self, request):
        print(request.data)
        task = models.TaskList.objects.get(id=request.data['id'])
        task.answer = request.data['answer']
        task.save()
        serializer = serializers.TaskListSerializer(task)
        return Response(serializer.data)

    def delete(self, request):
        serializers.TaskListSerializer.delete(serializers.TaskListSerializer(), request.data)
        return Response("Done")


class SpecializationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        specialization = models.Specialization.objects.all()
        serializer = serializers.SpecializationSerializer(specialization, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        specialization = serializers.SpecializationSerializer.create(serializers.SpecializationSerializer(),
                                                                     request.data, user)
        specialization = models.Specialization.objects.filter(user=user)
        serializer = serializers.SpecializationSerializer(specialization, many=True)
        return Response(serializer.data)

    def delete(self, request):
        user = request.user
        serializers.SpecializationSerializer.delete(serializers.SpecializationSerializer(), request.data)
        specialization = models.Specialization.objects.filter(user=user)
        serializer = serializers.SpecializationSerializer(specialization, many=True)
        return Response(serializer.data)