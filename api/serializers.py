from rest_framework import serializers

from api.models import Keyword, KeywordTag, EducationLevels


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["keyword_tag"] = f"{instance.keyword_tag.name}"
        return response


class KeywordTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordTag
        fields = "__all__"


class EducationSerializer(serializers.Serializer):
    degreeName = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    fieldOfStudy = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    institutionName = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    location = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    sortOrder = serializers.IntegerField(required=True, min_value=1)


class ExperienceSerializer(serializers.Serializer):
    jobTitle = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    startDate = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    endDate = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    description = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    clientName = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    projectName = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    tools = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    sortOrder = serializers.IntegerField(required=True, min_value=1)


class CertificationSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    licenseNumber = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    certificationDate = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    certificationAuthority = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    certificationUrl = serializers.URLField(required=True, allow_blank=True, allow_null=True)
    sortOrder = serializers.IntegerField(required=True, min_value=1)


class SubQuerySerializer(serializers.Serializer):
    sortOrder = serializers.IntegerField(required=True, min_value=1)
    query = serializers.CharField(required=True, allow_blank=True, allow_null=True)


class QuerySerializer(serializers.Serializer):
    type = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    sortOrder = serializers.IntegerField(required=True, min_value=1)
    queries = SubQuerySerializer(many=True, required=True)


class FactorSerializer(serializers.Serializer):
    education = serializers.FloatField(default=25.0, min_value=0.0, max_value=100.0)
    certification = serializers.FloatField(default=25.0, min_value=0.0, max_value=100.0)
    experience = serializers.FloatField(default=25.0, min_value=0.0, max_value=100.0)
    jobTitle = serializers.FloatField(default=25.0, min_value=0.0, max_value=100.0)


class FilterParamSerializer(serializers.Serializer):
    alternativeSkill = serializers.BooleanField(required=True)
    complianceEvidence = serializers.BooleanField(required=False)


class ParserSerializer(serializers.Serializer):
    filters = FilterParamSerializer(required=True, many=False)
    weightage = FactorSerializer(required=True)
    firstName = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    lastName = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    jobTitle = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    summary = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    experiences = serializers.ListField(
        required=True, child=ExperienceSerializer(required=True), min_length=1
    )
    educations = serializers.ListField(
        required=True, child=EducationSerializer(required=False)
    )
    certifications = serializers.ListField(
        required=True, child=CertificationSerializer(required=False)
    )
    requests = serializers.ListField(required=True, child=QuerySerializer(required=True))


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevels
        fields = "__all__"


# class IndustrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IndustryDataset
#         fields = "__all__"
