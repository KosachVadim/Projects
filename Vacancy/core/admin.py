from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from .models import Vacancy
from django.urls import path
from django.shortcuts import render



@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['specialization', 'unique_id']
    search_fields = ['unique_id']

