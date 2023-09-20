from django.db import models

class Vacancy(models.Model):

    COUNTRIES = [
        ('Польша(pl)', 'Польша(pl)'),
        ('Германия(de)', 'Германия(de)'),
        ('Литва(lt)', 'Литва(lt)'),
        ('Испания(es)', 'Испания(es)'),
        ('Бельгия(be)', 'Бельгия(be)'),
        ('Великобритания(uk)', 'Великобритания(uk)'),
    ]

    country = models.CharField(max_length=255, choices=COUNTRIES)
    city = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    description = models.TextField()
    salary_range = models.CharField(max_length=255)
    manager_account = models.CharField(max_length=255)
    profit_type = models.CharField(max_length=255)
    profit_amount = models.FloatField()
    working_conditions = models.TextField()
    contact_person = models.CharField(max_length=255)
    unique_id = models.CharField(max_length=10, unique=True, default='', editable=False)
    def get_country_code(self):
        # Получаем код страны из выбранной страны, например, 'pl' из 'Польша(pl)'
        return self.country.split('(')[1].split(')')[0]

    def generate_unique_id(self):
        country_code = self.get_country_code()
        vacancies_with_country_code = Vacancy.objects.filter(country__contains=country_code)
        count = vacancies_with_country_code.count() + 1
        unique_id = f"{country_code}{count:04d}"  # Например, 'pl0001'
        return unique_id

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.specialization
