from django.urls import path

from api.views import (
    GetKeywordById,
    KeywordManagementView,
    KeywordView,
    ParserView,
    TaggerCreateView,
    TaggerDestroyView,
    TaggerListView,
    TaggerRetrieveView,
    TaggerUpdateView, EducationLevel
)

urlpatterns = [
    path("parser/", ParserView.as_view()),
    path("keywords-management/", KeywordView.as_view()),
    path("keywords-management/<int:pk>/", KeywordManagementView.as_view()),
    path("keyword-tags/list/", TaggerListView.as_view(), name="keyword_tag_list"),
    path("keyword-tag/create/", TaggerCreateView.as_view(), name="keyword-tag-create"),
    path("keyword-tag/retrieve/<int:pk>/", TaggerRetrieveView.as_view(), name="specific-keyword-tag"),
    path("keyword-tag/update/<int:pk>/", TaggerUpdateView.as_view()),
    path("keyword-tag/delete/<int:pk>/", TaggerDestroyView.as_view(), name="delete-keyword-tag"),
    path("keyword-management/<int:pk>/", GetKeywordById.as_view(), name="keyword-id"),
    path("education-levels/", EducationLevel.as_view(), name="education-level"),
    # path("industry-dataset/", IndustryClassifier.as_view(), name="industry-dataset"),
]
