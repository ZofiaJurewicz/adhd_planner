from django.db import models

AMOUNT_TYPE_CHOICES = [
    ('+', 'Plus'),
    ('-', 'Minus')
]


class AddAThingToDo(models.Model):
    CATEGORY_CHOICES = [
        ('SHD', 'Should'),
        ('MST', 'Must'),
        ('NICE', 'It would be nice if')
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    deadline = models.DateTimeField()
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    operation = models.CharField(max_length=1, choices=AMOUNT_TYPE_CHOICES, default='+', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title


class Bank(models.Model):
    title = models.CharField(max_length=255)
    operation = models.CharField(max_length=1, choices=AMOUNT_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
