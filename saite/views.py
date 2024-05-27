from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import City, TelegramGroup
from telegram_auth.views import update_parser_settings
from telegram_auth.models import ParserSetting
import json
def main_page(request):
    return render(request, 'main.html')

def news_page(request):
    return render(request, 'news.html')

def about_page(request):
    user_count = User.objects.count()
    city_count = City.objects.count()
    context = {
        'user_count': user_count,
        'city_count': city_count,
    }
    return render(request, 'about.html', context)

from django.shortcuts import render, redirect
from .models import City
from .forms import ParserForm
from django.contrib.auth.decorators import login_required

@login_required
def manage_keywords(request):
    user = request.user
    existing_parser = ParserSetting.objects.filter(user=user).first()
    existing_city = existing_parser.city if existing_parser else None
    existing_keywords = existing_parser.keywords if existing_parser else ""

    if request.method == 'POST':
        form = ParserForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            keywords = form.cleaned_data['keywords']

            ParserSetting.objects.filter(user=user, city=city).delete()

            parser = ParserSetting.objects.create(
                user=user,
                city=city,
                keywords=keywords,
            )

            request._body = json.dumps({
                'city_id': city.id,
                'keywords': keywords,
            }).encode('utf-8')
            response = update_parser_settings(request)

            return redirect('main-page')
    else:
        form = ParserForm(initial={'city': existing_city, 'keywords': existing_keywords})

    cities = City.objects.all()
    return render(request, 'manage_keywords.html', {
        'form': form,
        'cities': cities,
        'keywords': existing_keywords,
        'existing_city': existing_city,
    })


def get_groups(request, city_id):
    groups = TelegramGroup.objects.filter(city_id=city_id).values('group_tag')
    return JsonResponse({'groups': list(groups)})