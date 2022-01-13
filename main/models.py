from django.db import models

# Create your models here.


class Driver(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Client(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Order(models.Model):
    STATUSES = [
        ('created', 'CREATED'),
        ('canceled', 'CANCELED'),
        ('accepted', 'ACCEPTED'),
        ('finished', 'FINISHED')
    ]
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, max_length=250, blank=True, null=True)
    # status = models.CharField(choices=STATUSES, max_length=250, default=STATUSES[0][0])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.full_name}-{self.created_date.date()}"
