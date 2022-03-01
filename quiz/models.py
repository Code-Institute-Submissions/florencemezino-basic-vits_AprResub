from django.db import models


class Question(models.Model):
    question_id = models.CharField("ID", max_length=255, null=True)
    question_name = models.TextField("Question", max_length=400, null=True)
    question_description = models.TextField("Description", max_length=300, null=True, blank=True)
    option1 = models.CharField(max_length=200, null=True, blank=True)
    option2 = models.CharField(max_length=200, null=True, blank=True)
    option3 = models.CharField(max_length=200, null=True, blank=True)
    option4 = models.CharField(max_length=200, null=True, blank=True)
    option5 = models.CharField(max_length=200, null=True, blank=True)
    option6 = models.CharField(max_length=200, null=True, blank=True)
    option7 = models.CharField(max_length=200, null=True, blank=True)
    option8 = models.CharField(max_length=200, null=True, blank=True)
    option9 = models.CharField(max_length=200, null=True, blank=True)
    option10 = models.CharField(max_length=200, null=True, blank=True)
    option11 = models.CharField(max_length=200, null=True, blank=True)
    option12 = models.CharField(max_length=200, null=True, blank=True)
    option13 = models.CharField(max_length=200, null=True, blank=True)
    option14 = models.CharField(max_length=200, null=True, blank=True)
    option15 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.question


