from django.db import models
from django.utils import timezone

class PriorityType(models.IntegerChoices):
    BAIXA = 0
    MEDIA = 1
    ALTA = 2

class StatusType(models.IntegerChoices):
    PENDENTE = 0
    ANDAMENTO = 1
    CONCLUIDO = 2


class Task(models.Model):
    name = models.CharField(max_length=50)
    priority = models.IntegerField(choices=PriorityType.choices, default=PriorityType.MEDIA, db_index=True)
    status = models.IntegerField(choices=StatusType.choices, default=StatusType.PENDENTE, db_index=True)
    event_at = models.DateTimeField(db_index=True)
    finish_at = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
