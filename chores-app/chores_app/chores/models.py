from django.db import models

class Chore(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points = models.IntegerField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    chores = models.ManyToManyField(Chore, through='Assignment')

    def __str__(self):
        return self.name

class Assignment(models.Model):
    chore = models.ForeignKey(Chore, on_delete=models.CASCADE)
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.chore.name} assigned to {self.family_member.name}"
