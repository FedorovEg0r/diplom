from django.db import models
from django.contrib.auth.models import User
from saite import models as saite_models
from saite.models import City

class TelegramProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='telegram_profile')
    chat_id = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.chat_id}"

class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.timestamp}"

class ParserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parser_settings')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='parser_settings')
    keywords = models.TextField(help_text="Введите ключевые слова, разделенные запятыми")

    def __str__(self):
        return f"{self.user.username} - {self.city.name} - {self.keywords}"