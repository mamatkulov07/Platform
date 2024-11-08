from django.db import models


class Home(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to='homeimage/', null=True, blank=True)
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    exams = models.TextField()
    examsimage = models.ImageField(upload_to='examsimage/', null=True, blank=True)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    image = models.ImageField(upload_to='aboutusimage/', null=True, blank=True)
    descriptions = models.TextField()
    personimage = models.ImageField(upload_to='personimage/', null=True, blank=True)
    nameperson = models.CharField(max_length=100)
    profession = models.CharField(max_length=200)

    def __str__(self):
        return self.nameperson


class StudyAbroad(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return self.description


class Country(models.Model):
    highereducation = (
        ('Secondary Educations', 'Secondary Educations'),
        ('Higher Educations', 'Higher Educations'),
        ('Language courses for youth', 'Language courses for youth'),
        ('Children language camps', 'Children language camps'),
    )
    higher = models.CharField(max_length=100, choices=highereducation)
    specialization = (
        ('IT Technologies', 'IT Technologies'),
        ('Business', 'Business'),
        ('Medicine', 'Medicine'),
        ('International Relationship', 'International Relationship'),
        ('Tourism', 'Tourism')
    )
    specializations = models.CharField(max_length=100, choices=specialization)
    country = (
        ('America', 'America'),
        ('Germany', 'Germany'),
        ('Austria', 'Austria'),
        ('Italy', 'Italy'),
        ('Spain', 'Spain'),
        ('Greate Britain', 'Greate Britain'),
        ('China', 'China'),
        ('Latvia', 'Latvia'),
        ('Indonesia', 'Indonesia'),
        ('Holland', 'Holland'),
        ('Ireland', 'Ireland'),
        ('Cyprus', 'Cyprus'),
        ('Canada', 'Canada'),
    )
    countrys = models.CharField(max_length=100, choices=country)
    image = models.ImageField(upload_to='countryimage/', null=True, blank=True)
    studyabroad = models.ForeignKey(StudyAbroad, on_delete=models.CASCADE)

    def __str__(self):
        return self.countrys


class Contacts(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    group = (
        ('Group', 'Group'),
        ('Company', 'Company')
    )
    company = models.CharField(max_length=100, choices=group)
    help = models.TextField()

    def __str__(self):
        return self.firstname

