from django.db import models


class Constituency(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    gss_code = models.CharField(max_length=15)
    three_code = models.CharField(max_length=4)
    region = models.CharField(max_length=255)
    electorate = models.PositiveIntegerField()


class Postcode(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    postcode = models.CharField(max_length=8)
    constituency_fk = models.ForeignKey(
        'elections24.Constituency',
        models.DO_NOTHING,
        db_column='constituency_fk',
        blank=True,
        null=True,
        related_name='constituency'
    )

    class Meta:
        indexes = [
            models.Index(fields=['postcode',]),
        ]
