# import asyncio
import os
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from random import choice
from rest_framework.response import Response
from account.models import Account
from api.serializers.user_account import (
    AccountSerializer,
)
from django.core.mail import send_mail
from asgiref.sync import sync_to_async
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt


@sync_to_async
@api_view(['POST'])
def user_registration(request):
    '''
        This view is for user registration.
        It accepts a post request with data:
        {
            "email": "example@mail.com"
             "first_name" : "First",
             "last_name" : "Last"
        }

        a password and auth token are automatically generated for the user. The password is done async while
        the token is created post save

        '''
    if request.method == 'POST':
        random_password = ''.join(
            [choice('1234567890qwertyuiopasdfghjklzxcvbnmABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(9)])
        user = {
            "first_name": request.data["first_name"],
            "last_name": request.data["last_name"],
            "email": request.data["email"],
            "password": random_password
        }
        serializer = AccountSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                "Your Password",
                "welcome! Your password is {}".format(random_password),
                os.environ.get('EMAIL_HOST_USER'),
                [request.data['email']],
                fail_silently=True
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    '''
        This view accepsts a POST request and is for user login.
        It accepts a post request with data:
        {
            "email": "example@mail.com"
             "password" : "password",
        }

        The endpoint returns an auth token that can be used to access protected view(which i have not included on this
        app for ease of use

        '''
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        user = Account.objects.get(email=email)

        if user.password == password:
            token = Token.objects.get(user=user).key
            serializer = AccountSerializer(user)

            content = {
                "user": serializer.data,
                "token": token
            }

            return Response(content, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@sync_to_async
@api_view(['GET'])
def view_users(request):
    '''
        This view is accepts a GET request returns a list of users.
        '''
    if request.method == "GET":
        users= Account.objects.all()
        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@sync_to_async
@api_view(['POST'])
def reset_password(request):
    '''
        This view accepts a POST request and is used to reset a user's passwor.
        It accepts a request with data:
        {
            "email": "example@mail.com"
        }

        The endpoint autogenerates a password, saves it to the user account and send it to the user's email async

        '''
    if request.method == "POST":

        user = Account.objects.filter(email=request.data['email'])
        old_password = Account.objects.get(email=request.data['email']).password
        new_password = ''.join(
            [choice('1234567890qwertyuiopasdfghjklzxcvbnmABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(9)])

        if old_password != new_password:
            user.update(password=new_password)
            send_mail(
                "Your Password",
                "Your new password is {}".format(new_password),
                os.environ.get('EMAIL_HOST_USER'),
                [request.data['email']],
                fail_silently=True
            )
            return Response(status=status.HTTP_201_CREATED)
        elif old_password == new_password:
            user.update(password=new_password[::-1]) #flip the password to read backwards. A bit insecure
            send_mail(
                "Your Password",
                "Your new password is {}".format(new_password[::-1]),
                os.environ.get('EMAIL_HOST_USER'),
                [request.data['email']],
                fail_silently=True
            )
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response({"message": "Could not update password"}, status=status.HTTP_400_BAD_REQUEST)












