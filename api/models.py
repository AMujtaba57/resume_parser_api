from django.contrib import admin
from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat
from jsoneditor.fields.django3_jsonfield import JSONField


class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class TextField(models.TextField):
    def __init__(self, *args, **kwargs):
        super(TextField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class KeywordTag(models.Model):
    name = NameField(unique=True, max_length=100)

    def __str__(self):
        return str(self.name).capitalize()


class Keyword(models.Model):
    keyword_value = NameField(max_length=100, unique=True)
    keyword_tag = models.ForeignKey(KeywordTag, related_name="keyword_tagger", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.keyword_value).capitalize()


class ResultHistory(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    query = models.CharField(max_length=500, null=True, blank=True)
    predicted_keywords = models.JSONField(null=True, blank=True)
    result = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(ordering=Concat('first_name', Value(' '), 'last_name'))
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ('-updated_at', 'created_at')


class EducationLevels(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class KeywordAlternative(models.Model):
    choices = [
        ("education", "Education"),
        ("certification", "Certification"),
        ("experience", "Experience")
    ]
    keyword_tag = models.ForeignKey(KeywordTag, related_name="alter_keyword_tagger", on_delete=models.PROTECT)
    alter_keyword_list = NameField(max_length=500)
    actual_keyword_list = models.ManyToManyField(Keyword,  verbose_name="keywords list", max_length=1000, blank=True)
    category = models.CharField(choices=choices, max_length=15)

    def __str__(self):
        return self.alter_keyword_list


class LabelIndustryDataset(models.Model):
    industry_label = NameField(max_length=500)

    def __str__(self):
        return self.industry_label


class ResumeDescriptionDataset(models.Model):
    industry_definition = TextField()
    industry = models.ForeignKey(LabelIndustryDataset, related_name='resume_industry',
                                 on_delete=models.PROTECT)


class QueryIndustryDataset(models.Model):
    query = models.TextField()
    industry = models.ForeignKey(LabelIndustryDataset, related_name='query_industry',
                                 on_delete=models.PROTECT)


class KeywordHistory(models.Model):
    query = TextField(unique=True)
    actual_keywords = TextField()
    alternative_included = TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Configuration(models.Model):
    name = models.CharField(max_length=250, unique=True)
    configuration_setting = JSONField()

    def __str__(self):
        return self.name
