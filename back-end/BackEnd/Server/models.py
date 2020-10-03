from django.db import models
from django.contrib.auth.models import User
import hashlib
import datetime
import random as rnd


class Profile(models.Model):
    company = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Test')

    def create(self, valid_data):
        user = User.objects.create_user(valid_data['username'], valid_data['email'], valid_data['password'])
        user.first_name = valid_data['first_name']
        user.last_name = valid_data['last_name']
        user.save()
        profile = Profile.objects.create(
            company=valid_data['company'],
            status=valid_data['status'],
            post=valid_data['post'],
            user=user,
            )
        profile.save()
        return profile

    def update_(self, valid_data, profile):
        user = User.objects.get(id=profile.user.id)
        user.email = valid_data['email']
        user.first_name = valid_data['first_name']
        user.last_name = valid_data['last_name']
        user.save()
        profile.company = valid_data['company']
        profile.status = valid_data['status']
        profile.post = valid_data['post']
        profile.save()
        return profile

    def delete_(self, profile):
        user = profile.user
        profile.delete()
        user.delete()


class Specialization(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Gef')
    level = models.CharField(max_length=30)

    def create(self, valid_data, user):
        specialization = Specialization.objects.create(
            name=valid_data['name'],
            level=valid_data['level'],
            user=user,
        )
        specialization.save()
        return specialization

    def delete_(self, specialization):
        specialization.delete()


class Session(models.Model):
    videoIdent = models.CharField(max_length=60)
    status = models.CharField(max_length=30)
    result = models.CharField(max_length=30)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Ivan')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Ivanchik')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    state = models.CharField(max_length=1000)

    def create(self, valid_data, user_input1, user_input2, specialization):
        Ident_video = hashlib.md5(str(user_input1.id + user_input2.id + rnd.randint(0,50)).encode()).hexdigest()
        session = Session.objects.create(
            videoIdent=Ident_video,
            status="not start",
            result="no result",
            creator=user_input1,
            candidate=user_input2,
            specialization=specialization,
            state="",
        )
        session.save()
        return session

    def update_(self, valid_data, session, state):
        session.status = valid_data['status']
        session.result = valid_data['result']
        session.state = state
        session.save()
        return session

    def delete_(self, session):
        session.delete()


class Message(models.Model):
    text = models.CharField(max_length=200)
    from_user = models.CharField(max_length=30)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def create(self, valid_data, session):
        message = Message.objects.create(
            text=valid_data['text'],
            from_user=valid_data['from'],
            session=session,
        )
        message.save()
        return message

    def update_(self, valid_data, message):
        message.text = valid_data['text']
        message.from_user = valid_data['from']
        message.save()
        return message

    def delete_(self, message):
        message.delete()


class Task(models.Model):
    text = models.CharField(max_length=200)
    answer = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Google')

    def create(self, valid_data, user):
        task = Task.objects.create(
            user=user,
            text=valid_data['text'],
            answer=valid_data['answer'],
        )
        task.save()
        return task

    def update_(self, valid_data, task):
        task.text = valid_data['text']
        task.answer = valid_data['answer']
        task.save()
        return task

    def delete_(self, task):
        task.delete()


class TaskList(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    answer = models.CharField(max_length=30)

    def create(self, valid_data, session, task):
        tasklist = TaskList.objects.create(
            task=task,
            session=session,
            answer=valid_data['text'],
        )
        tasklist.save()
        return tasklist


    def delete_(self, tasklist):
        tasklist.delete()

