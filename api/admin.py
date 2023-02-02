from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from jsoneditor.fields.django3_jsonfield import JSONField
from jsoneditor.forms import JSONEditor

from api.forms import KeyAlterForm
from api.models import Keyword, KeywordTag, EducationLevels, KeywordAlternative, ResultHistory, \
    ResumeDescriptionDataset, QueryIndustryDataset, LabelIndustryDataset, KeywordHistory, Configuration

admin.site.site_header = "Zbizlink Admin Panel"
admin.site.site_title = "ZbizlinkPortal"
admin.site.index_title = "Welcome to Zbizlink Portal"


class KeywordAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
        "keyword_value",
        "keyword_tag",
    )
    list_filter = ("keyword_tag",)
    search_fields = ("keyword_value",)
    list_per_page = 25


class KeywordTagAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    list_per_page = 25


class ResultHistoryAdmin(SummernoteModelAdmin):
    list_display = ('full_name', 'job_title', 'query', 'predicted_keywords', 'result')
    summernote_fields = ('result', 'query', 'predicted_keywords')
    search_fields = ("query", "first_name", "last_name")
    list_filter = ("first_name", "last_name")
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(KeywordHistory)
class KeywordHistoryAdmin(admin.ModelAdmin):
    list_display = ('query', 'actual_keywords', 'alternative_included', 'created_at', 'updated_at')
    search_fields = ("query", "actual_keywords", "alternative_included")
    list_per_page = 25
    ordering = ('-updated_at', '-created_at')

    def save_model(self, request, obj, form, change):
        pass

    def save_related(self, request, form, formsets, change):
        pass

    def has_add_permission(self, request):
        return False


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(KeywordTag, KeywordTagAdmin)
admin.site.register(ResultHistory, ResultHistoryAdmin)


@admin.register(KeywordAlternative)
class KeyAlterAdmin(admin.ModelAdmin):
    autocomplete_fields = ['actual_keyword_list', ]
    list_display = ('keyword_tag', 'alter_keyword_list', 'category')
    search_fields = ('actual_keyword_list', 'alter_keyword_list')
    empty_value_display = '-empty-'
    list_per_page = 25


@admin.register(ResumeDescriptionDataset)
class IndustryResumeAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
        "industry_definition",
        "industry"
    )
    search_fields = ("industry_definition",)
    list_filter = ("industry",)
    list_per_page = 25


@admin.register(QueryIndustryDataset)
class IndustryQueryAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
        "query",
        "industry"
    )
    search_fields = ("query",)
    list_filter = ("industry",)
    list_per_page = 25


@admin.register(EducationLevels)
class EducationLevelsAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
        "name",
        "level",
    )
    search_fields = ("level",)
    list_per_page = 25


@admin.register(LabelIndustryDataset)
class LabelIndustry(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
        "industry_label",
        "id"
    )
    search_fields = ("industry",)
    list_per_page = 25


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditor},
    }
    # readonly_fields = ('name',)
    list_display = (
        "name",
    )
    search_fields = ("name", "configuration_setting")
    list_per_page = 25

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
