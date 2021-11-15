from django.db import models

# Create your models here.


class Cities(models.Model):
    cityName = models.CharField(max_length=30)

    def __str__(self):
        # to let the city name automatically capitalized on card
        self.cityName = self.cityName.capitalize()
        return self.cityName
