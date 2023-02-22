from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PriorityType(models.IntegerChoices):
    UMA_ESTRELA = 1
    DUAS_ESTRELA = 2
    TRES_ESTRELA = 3
    QUATRO_ESTRELA = 4
    CINCO_ESTRELA = 5


class StatusType(models.IntegerChoices):
    PENDENTE = 0
    ANDAMENTO = 1
    CONCLUIDO = 2


class Task(models.Model):
    name = models.CharField(max_length=50)
    priority = models.IntegerField(choices=PriorityType.choices, default=PriorityType.TRES_ESTRELA, db_index=True)
    status = models.IntegerField(choices=StatusType.choices, default=StatusType.PENDENTE, db_index=True)
    event_at = models.DateTimeField(db_index=True)
    finish_at = models.DateTimeField(db_index=True, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

