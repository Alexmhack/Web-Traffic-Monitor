import urllib.request
import httpagentparser
import os
import hashlib

from django.shortcuts import render
from django.http import JsonResponse

from pusher import Pusher
from decouple import config

pusher = Pusher(
	app_id=config('PUSHER_APP_ID'),
	key=config('PUSHER_KEY'),
	secret=config('PUSHER_SECRET'),
	cluster=config('PUSHER_CLUSTER'),
	ssl=True
)
