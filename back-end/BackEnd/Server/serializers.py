from django.contrib.auth.models import User
from rest_framework import serializers
from Server import models
import requests


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=20)
    status = serializers.CharField(max_length=20)
    company = serializers.CharField(max_length=20)
    post = serializers.CharField(max_length=20)

    def create(self, valid_data):
        user = models.Profile.create(models.Profile(), valid_data)
        return user

    def update(self, valid_data, user):
        profile = models.Profile.objects.get(user=user)
        profile = models.Profile.update_(models.Profile(), valid_data, profile)
        return profile

    def delete(self, valid_data, user):
        profile = models.Profile.objects.get(user=user)
        models.Profile.delete_(models.Profile(), profile)


class SessionSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30)
    videoIdent = serializers.CharField(max_length=60)
    state = serializers.CharField(max_length=1000)
    status = serializers.CharField(max_length=30)
    result = serializers.CharField(max_length=30)
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    candidate = serializers.PrimaryKeyRelatedField(read_only=True)
    specialization = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, valid_data, user1, user2):
        specialization = models.Specialization.objects.get(id=valid_data['id'])
        session = models.Session.create(models.Session(), valid_data, user1, user2, specialization)
        return session

    def update(self, valid_data):
        session = models.Session.objects.get(id=valid_data['id'])
        state = ""
        if valid_data['status'] == 'finished':
            state = requests.post('http://localhost:8080/iot/').text
        session = models.Session.update_(models.Session(), valid_data, session, state)
        return session

    def delete(self, valid_data):
        session = models.Session.objects.get(id=valid_data['id'])
        models.Session.delete_(models.Session(), session)


class SpecializationSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=60)
    level = serializers.CharField(max_length=30)

    def create(self, valid_data, user):
        specialization = models.Specialization.create(models.Specialization(), valid_data, user)
        return specialization

    def delete(self, valid_data):
        specialization = models.Specialization.objects.get(id=valid_data['id'])
        models.Specialization.delete_(models.Specialization(), specialization)


class MessageSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30)
    text = serializers.CharField(max_length=200)
    from_user = serializers.CharField(max_length=30)
    session = serializers.CharField(max_length=30)

    def create(self, valid_data, session):
        message = models.Message.create(models.Message(), valid_data, session)
        return message

    def update(self, valid_data):
        message = models.Message.objects.get(id=valid_data['id'])
        message = models.Message.update_(models.Message(), valid_data, message)
        return message

    def delete(self, valid_data):
        message = models.Message.objects.get(id=valid_data['id'])
        models.Message.delete_(models.Message(), message)


class TaskSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30)
    text = serializers.CharField(max_length=200)
    answer = serializers.CharField(max_length=30)

    def create(self, valid_data, user):
        task = models.Task.create(models.Task(), valid_data, user)
        return task

    def update(self, valid_data):
        task = models.Task.objects.get(id=valid_data['id'])
        task = models.Task.update_(models.Task(), valid_data, task)
        return task

    def delete(self, valid_data):
        task = models.Task.objects.get(id=valid_data['id'])
        models.Task.delete_(models.Task(), task)


class TaskListSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30)
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    session = serializers.PrimaryKeyRelatedField(read_only=True)
    answer = serializers.CharField(max_length=30)

    def create(self, valid_data, session, task):
        tasklist = models.TaskList.create(models.TaskList(), valid_data, session, task)
        return tasklist

    def delete(self, valid_data):
        tasklist = models.TaskList.objects.get(id=valid_data['id'])
        models.TaskList.delete_(models.TaskList(), tasklist)
