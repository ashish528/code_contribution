<!DOCTYPE html>
<html lang="en">

<head>
	<title>Resume</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="sadsa" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
	<link rel="preconnect" href="https://fonts.gstatic.com">
	<link rel="styleshasdaeet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link
		href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,400&display=swap"
		rel="stylesheet">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.4/angular.min.js"></script>
</head>

	<div class="main-pagedesignjdbuilder">

	<body ng-app="fupApp" ng-controller="resultController" ng-init="resultData();" ng-cloak>
		<div class="nav-bar-hono">
			<div class="hono-logo">
				<img src="https://devchatbot.honohr.com/profile/static/profile_img/honohr.png">
			</div>
			<div class="nav-details">
				<div class="bg-gray-color">

				</div>
				<div class="bg-circle-img">

				</div>
			</div>
		</div>

			.list .card {
		width: 309px;
		height: 132px;
		margin-left: 15.5px;
		margin-bottom: 2px;
		padding-top: 17px;
		border-radius: 8px;
		transition: 0.3s;
		cursor: pointer;
	}
		
		from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from app import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.conf import settings
import requests
import urllib.request
import time
import os
import difflib
from difflib import SequenceMatcher
import pdb
from nltk.tokenize import LineTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
