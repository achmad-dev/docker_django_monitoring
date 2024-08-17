from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from asgiref.sync import sync_to_async
import asyncio
# Create your views here.


def hello_world(request):
    return HttpResponse("Hello, World!")


@api_view(["GET"])
def hello_api(request):
    return Response({"message": "Hello, API World!"})


@require_http_methods(["GET"])
async def hello_async(request):
    await asyncio.sleep(1)
    return HttpResponse("Hello, Async World!")


@sync_to_async
def get_sync_message():
    return "Hello, Sync-to-Async World!"


async def hello_sync_to_async(request):
    message = await get_sync_message()
    return HttpResponse(message)
