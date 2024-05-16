from django.db import models
from django.contrib.auth.models import User
from saite import models as saite_models
from saite.models import City, Parser  # Импорт моделей из saite


class TelegramProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='telegram_profile')
    chat_id = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=64, blank=True, null=True)  # Добавляем поле для токена

    def __str__(self):
        return f"{self.user.username} - {self.chat_id}"

class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.timestamp}"

class ParserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parser_settings')
    parser = models.ForeignKey(Parser, on_delete=models.CASCADE, related_name='parser_settings')

    def __str__(self):
        return f"{self.user.username} - {self.parser.city.name} - {self.parser.keywords}"