from django.db import models


class Company(models.Model):
    company = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return str(self.company)


class Position(models.Model):
    position = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return str(self.position)


class Mail(models.Model):
    mail = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return str(self.mail)


class Tel(models.Model):
    tel = models.CharField(max_length=13, null=True, blank=True)
    tel_1 = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return str(self.tel)


class Department(models.Model):
    department = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return str(self.department)


class Location(models.Model):
    location = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return str(self.location)


class Contacts(models.Model):
    family_name = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20, blank=True)
    company_id = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT)
    department_id = models.ForeignKey(Department, null=True, blank=True, on_delete=models.PROTECT)
    position_id = models.ForeignKey(Position, null=True, blank=True, on_delete=models.PROTECT)
    tel_id = models.ForeignKey(Tel, null=True, blank=True, on_delete=models.PROTECT)
    mail_id = models.ForeignKey(Mail, null=True, blank=True, on_delete=models.PROTECT)
    info = models.TextField(max_length=250, blank=True)
    is_chief = models.BooleanField(default=False)

    def __str__(self):
        name = self.family_name + " " + self.name
        return str(name)
