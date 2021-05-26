from django.db import models
from members.models import Member

class Industry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name='Industry'
        verbose_name_plural='Industries'

class MemberToIndustry(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.member, self.industry)

    class Meta:
        verbose_name="Company Industry"
        verbose_name_plural="Company Industries" 