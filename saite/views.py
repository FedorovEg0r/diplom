
from django.http import JsonResponse
from .models import City, Parser, TelegramGroup
from telegram_auth.views import update_parser_settings
import json
def main_page(request):
    return render(request, 'main.html')

def news_page(request):
    return render(request, 'news.html')

def about_page(request):
    return render(request, 'about.html')

from django.shortcuts import render, redirect
from .models import City, Parser
from .forms import ParserForm
from django.contrib.auth.decorators import login_required

@login_required
def manage_keywords(request):
    user = request.user
    existing_parser = Parser.objects.filter(user=user).first()
    existing_city = existing_parser.city if existing_parser else None
    existing_keywords = existing_parser.keywords if existing_parser else ""

    if request.method == 'POST':
        form = ParserForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            keywords = form.cleaned_data['keywords']

            # Удаление всех старых ключевых слов для данного пользователя и города
            Parser.objects.filter(user=user, city=city).delete()

            # Добавление новых ключевых слов для выбранного города
            parser = Parser.objects.create(
                user=user,
                city=city,
                keywords=keywords,
            )

            # Обновление настроек парсера в telegram_auth
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