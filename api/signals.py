from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

import parser.matcher
from parser.resume_query_classifier import retrain_query_model
from .models import KeywordTag, Keyword, ResumeDescriptionDataset, QueryIndustryDataset, EducationLevels, Configuration
from parser.matcher import retrain_model, configuration_weightage
from parser.resume_Industry_classifier import retrain_industry_model
from similarity.education import retrain_model



@receiver(post_save, sender=KeywordTag)
def post_handler(sender, created, **kwargs):
    """
    This signal is called when create or update operation
    is performed from admin site on KeywordTag model.
    """
    if created:  # On creation
        retrain_model()
    else:  # On update
        retrain_model()


@receiver(post_delete, sender=KeywordTag)
def delete_handler(sender, **kwargs):
    """
    This signal is called when delete operation
    is performed from admin site on KeywordTag model.
    """
    retrain_model()


@receiver(post_save, sender=Keyword)
def post_handler(sender, created, **kwargs):
    """
    This signal is called when create or update operation
    is performed from admin site on Keyword model.
    """
    if created:
        retrain_model()
    else:
        retrain_model()


@receiver(post_delete, sender=Keyword)
def delete_handler(sender, **kwargs):
    """
    This signal is called when delete operation
    is performed from admin site on Keyword model.
    """
    retrain_model()


@receiver(post_save, sender=ResumeDescriptionDataset)
def post_handler(sender, created, **kwargs):
    """
    This signal is called when create or update operation
    is performed from admin site on KeywordTag model.
    """
    if created:  # On creation
        retrain_industry_model()
    else:  # On update
        retrain_industry_model()


@receiver(post_save, sender=QueryIndustryDataset)
def pos_handler(sender, created, **kwargs):
    """
    This signal is called when create or update operation
    is performed from admin site on KeywordTag model.
    """
    if created:  # On creation
        retrain_query_model()
    else:  # On update
        retrain_query_model()


@receiver(post_save, sender=EducationLevels)
def pos_handler(sender, created, **kwargs):
    """
    This signal is called when create or update operation
    is performed from admin site on KeywordTag model.
    """
    if created:  # On creation
        retrain_model()
    else:  # On update
        retrain_model()


@receiver(post_save, sender=Configuration)
def pos_handler(sender, created, **kwargs):
    """
    This signal is called when create or update operation
    is performed from admin site on KeywordTag model.
    """
    if created:  # On creation
        configuration_weightage()
    else:  # On update
        configuration_weightage()
