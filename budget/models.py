from django.db import models
from django.utils import timezone

TYPE_CHOICES = (
    ('saving', 'Saving'),
    ('credit', 'Credit'),
    ('other', 'Other'),
)


class Account(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='saving')
    create_at = models.DateField(auto_created=True, default=timezone.now)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Withdrawal(models.Model):
    amount = models.IntegerField(blank=False, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    datetime = models.DateField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.account}"


class Category(models.Model):
    title = models.CharField(unique=True, max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    create_at = models.DateField(auto_created=True, default=timezone.now)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Transaction(models.Model):
    date = models.DateField()
    amount = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)
    create_at = models.DateField(auto_created=True, default=timezone.now)

    def __str__(self):
        return f"{self.amount} - {self.category}"
