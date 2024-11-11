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
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class University(models.Model):
    location = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    typeofprogramis = models.TextField()
    language = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='universityimage/', null=True, blank=True)
    description = models.TextField()
    date = models.TextField()
    cost = models.TextField()
    photo = models.ImageField(upload_to='image/', null=True, blank=True)
    category = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='facultyimage/', null=True, blank=True)
    description = models.TextField()
    studyabroad = models.ForeignKey(StudyAbroad, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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

