import traceback

from drf_yasg.openapi import IN_QUERY, Parameter
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Keyword, KeywordTag, EducationLevels
from api.pagination import BasicPagination, PaginationHandlerMixin
from api.serializers import KeywordSerializer, KeywordTagSerializer, ParserSerializer, EducationLevelSerializer
from parser.matcher import sentence_extract


def error_fields_finding(data: dict):
    """
    parameters:data-->dict
    Returns:list, str
    """
    try:
        response_list = []
        for key, value in data.items():
            if isinstance(value, dict):
                for _key, _value in value.items():
                    if isinstance(_value, dict):
                        for __key, __value in _value.items():
                            if isinstance(__value, list):
                                for item in __value:
                                    if isinstance(item, dict):
                                        for ___key, ___value in item.items():
                                            response_list.append(f"{key}_{_key}_{__key}_{___key}")
                                    else:
                                        response_list.append(f"{key}_{_key}_{__key}")
                            else:
                                response_list.append(f"{key}_{_key}_{__key}")
                    elif isinstance(_value, list):
                        response_list.append(f"{key}_{_key}")
            else:
                response_list.append(f"{key}")
        return ", ".join(response_list) + " has/have invalid values"
    except Exception:
        return "something wrong in sending request"


def response_standard(response_data, message, _status):
    return {"data": response_data, "message": message, "httpCode": _status}


def validate_Factors(data: dict) -> dict:
    factors = dict(data['weightage'])
    if "education" not in factors.keys():
        factors["educationWeightage"] = 25.0

    if "certification" not in factors.keys():
        factors["certificationWeightage"] = 25.0

    if "experience" not in factors.keys():
        factors["experienceWeightage"] = 25.0

    if "jobTitle" not in factors.keys():
        factors["jobTitleWeightage"] = 25.0
    data['weightage'] = factors
    return data


class ParserView(APIView):
    """
    ParserView Class

    This view performs POST operation for Parser

    Parameters
    ----------
    APIView : rest_framework.views
    """

    @swagger_auto_schema(
        request_body=ParserSerializer,
        responses={
            200: "Parsed",
            401: "Unauthorized",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        # manual_parameters=[
        #     Parameter("alter", IN_QUERY, type="int"),
        #     Parameter("validate", IN_QUERY, type="int"),
        # ],
    )
    def post(self, request):
        """
        HTTP POST request

        An HTTP endpoint that saves a parser in DB

        Parameters
        ----------
        request : django.http.request

        Returns
        -------
        rest_framework.response
            returns success message if data saved successfully,error message otherwise
        """

        try:
            request_data = validate_Factors(request.data)

            serializer = ParserSerializer(data=request_data)
            if serializer.is_valid():
                response = sentence_extract(request_data)
                return Response(response_standard(response_data=response, message=None, _status=200), "200")
            else:
                return Response(
                    response_standard(response_data=None, message=error_fields_finding(serializer.errors), _status=400),
                    "400",
                )
        except Exception as e:
            traceback.print_exc()
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


class TaggerRetrieveView(APIView):
    """
    TaggerRetrieveView Class

    This view performs GET operation for Tagger

    Parameters
    ----------
    APIView : rest_framework.views
    """

    @swagger_auto_schema(
        responses={
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
    )
    def get(self, request, pk):
        """
        HTTP GET request

        An HTTP endpoint that returns specific Taggers

        Parameters
        ----------
        request : django.http.request

        Returns
        -------
        rest_framework.response
            returns HTTP 200 status if data returned successfully,error message otherwise
        """
        try:
            keywords = KeywordTag.objects.get(pk=pk)
            serializer = KeywordTagSerializer(keywords)
            return Response(
                response_standard(response_data=serializer.data, message=None, _status=200), status=status.HTTP_200_OK
            )
        except KeywordTag.DoesNotExist:
            return Response(
                response_standard(
                    response_data=None, message=f"KeywordTag Object not exist against id {pk}", _status=400
                ),
                "400",
            )
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


class TaggerCreateView(APIView):
    """
    TaggerCreateView Class

    This view performs POST operation for Tagger

    Parameters
    ----------
    APIView : rest_framework.views
    """

    @swagger_auto_schema(
        request_body=KeywordTagSerializer,
        responses={
            201: "Created",
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        """
        HTTP POST request

        An HTTP endpoint that saves a tagger in DB

        Parameters
        ----------
        request : django.http.request

        Returns
        -------
        rest_framework.response
            returns success message if data saved successfully,error message otherwise
        """
        try:
            data = request.data
            serializer = KeywordTagSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(response_standard(response_data=serializer.data, message=None, _status=201), "201")
            else:
                return Response(
                    response_standard(response_data=None, message=error_fields_finding(serializer.errors), _status=400),
                    "400",
                )
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


class TaggerListView(APIView, PaginationHandlerMixin):
    """
    TaggerListView Class

    This view performs GET operation for Tagger

    Parameters
    ----------
    APIView : rest_framework.views
    """
    pagination_class = BasicPagination
    serializer_class = KeywordTagSerializer

    @swagger_auto_schema(
        responses={
            200: "OK",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
        manual_parameters=[
            Parameter("name", IN_QUERY, type="string"),
        ],
    )
    def get(self, request):
        """
        HTTP GET request

        An HTTP endpoint that returns all Taggers

        Parameters
        ----------
        request : django.http.request

        Returns
        -------
        rest_framework.response
            returns HTTP 200 status if data returned successfully,error message otherwise
        """
        try:
            if request.query_params.get("name"):
                tags = KeywordTag.objects.filter(
                    name__icontains=request.query_params.get("name")
                ).order_by('-id')
            else:
                tags = KeywordTag.objects.all().order_by('-id')
            page = self.paginate_queryset(tags)
            if page is not None:
                serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
                return Response(
                    response_standard(response_data=serializer.data, message=None, _status=200),
                    status=status.HTTP_200_OK,
                )
            else:
                serializer = self.serializer_class(tags, many=True)
                return Response(
                    response_standard(response_data=serializer.data, message=None, _status=200),
                    status=status.HTTP_200_OK,
                )

        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


class TaggerDestroyView(APIView):
    """
    TaggerDeleteView Class

    This view performs DELETE operation for Tagger

    Parameters
    ----------
    APIView : rest_framework.views
    """

    serializer_class = KeywordTagSerializer

    @swagger_auto_schema(
        responses={
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
    )
    def delete(self, request, pk):
        """
        HTTP DELETE request

        An HTTP endpoint that deletes a tagger for provided PK

        Parameters
        ----------
        request : django.http.request

        pk : integer

        Returns
        -------
        rest_framework.response
            returns success message if data deleted successfully,error message otherwise
        """
        try:
            keyword = KeywordTag.objects.get(pk=pk)
            keyword.delete()
            return Response(
                response_standard(
                    response_data=None, message=f"KeywordTag Object deleted successfully against id {pk}", _status=200
                ),
                "200",
            )
        except KeywordTag.DoesNotExist:
            return Response(
                response_standard(
                    response_data=None, message=f"KeywordTag Object not exist against id {pk}", _status=400
                ),
                status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


class TaggerUpdateView(UpdateAPIView):
    """
    TaggerUpdateView Class

    This view performs PUT operation for Tagger

    Parameters
    ----------
    APIView : rest_framework.views
    """
    serializer_class = KeywordTagSerializer

    @swagger_auto_schema(
        responses={
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
    )
    def put(self, request, pk):
        """
        HTTP PUT request

        An HTTP endpoint that updates a tagger for provided PK

        Parameters
        ----------
        request : django.http.request

        pk : integer

        Returns
        -------
        rest_framework.response
            returns success message if data updated successfully,error message otherwise
        """
        try:
            keyword = KeywordTag.objects.get(pk=pk)
            serializer = KeywordTagSerializer(data=request.data, instance=keyword)
            if serializer.is_valid():
                serializer.save()
                return Response(response_standard(response_data=serializer.data, message=None, _status=200), "200")
            else:
                return Response(
                    response_standard(response_data=None, message=error_fields_finding(serializer.errors), _status=400),
                    "400",
                )
        except KeywordTag.DoesNotExist:
            return Response(
                response_standard(
                    response_data=None, message=f"KeywordTag Object not exist against id {pk}", _status=400
                ),
                "400",
            )
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


class KeywordManagementView(APIView):
    """
    KeywordManagementView Class

    This view performs PUT,DEELETE operation for Keyword

    Parameters
    ----------
    APIView : rest_framework.views
    """

    @swagger_auto_schema(
        operation_description="PUT keywords-management/1/",
        request_body=KeywordSerializer,
        responses={
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
    )
    def put(self, request, pk):
        """
        HTTP PUT request

        An HTTP endpoint that updates a keyword for provided PK

        Parameters
        ----------
        request : django.http.request

        pk : integer

        Returns
        -------
        rest_framework.response
            returns success message if data updated successfully,error message otherwise
        """
        try:
            keyword = Keyword.objects.get(pk=pk)
            serializer = KeywordSerializer(data=request.data, instance=keyword)
            if serializer.is_valid():
                serializer.save()
                return Response(response_standard(response_data=serializer.data, message=None, _status=200), "200")
            else:
                return Response(
                    response_standard(response_data=None, message=error_fields_finding(serializer.errors), _status=400),
                    "400",
                )
        except Keyword.DoesNotExist:
            return Response(
                response_standard(response_data=None, message=f"Keyword Object not exist against id {pk}", _status=400),
                "400",
            )
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")

    @swagger_auto_schema(
        operation_description="DELETE keywords-management/1/",
        responses={
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
    )
    def delete(self, request, pk):
        """
        HTTP DELETE request

        An HTTP endpoint that deletes a keyword for provided PK

        Parameters
        ----------
        request : django.http.request

        pk : integer

        Returns
        -------
        rest_framework.response
            returns success message if data deleted successfully,error message otherwise
        """
        try:
            keyword = Keyword.objects.get(pk=pk)
            keyword.delete()
            return Response(
                response_standard(
                    response_data=None, message=f"Keyword Object deleted successfully against id {pk}", _status=200
                ),
                "200",
            )
        except Keyword.DoesNotExist:
            return Response(
                response_standard(response_data=None, message=f"Keyword Object not exist against id {pk}", _status=400),
                "400",
            )

        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


class KeywordView(APIView, PaginationHandlerMixin):
    """
    KeywordView Class

    This view performs POST ,GET operation for Keyword

    Parameters
    ----------
    APIView : rest_framework.views
    """
    pagination_class = BasicPagination
    serializer_class = KeywordSerializer

    @swagger_auto_schema(
        operation_description="POST keywords-management",
        request_body=KeywordSerializer,
        responses={
            201: "Created",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        """
        HTTP POST request

        An HTTP endpoint that saves a keyword in DB

        Parameters
        ----------
        request : django.http.request

        Returns
        -------
        rest_framework.response
            returns success message if data saved successfully,error message otherwise
        """
        try:
            data = request.data
            serializer = KeywordSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(response_standard(response_data=serializer.data, message=None, _status=201), "201")
            else:
                return Response(
                    response_standard(response_data=None, message=error_fields_finding(serializer.errors), _status=400),
                    "400",
                )
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")

    @swagger_auto_schema(
        operation_description="GET keywords-management",
        responses={
            200: "OK",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
        manual_parameters=[
            Parameter("keyword_value", IN_QUERY, type="string"),
        ],
    )
    def get(self, request):
        """
        HTTP GET request

        An HTTP endpoint that returns all Keyword

        Parameters
        ----------
        request : django.http.request

        Returns
        -------
        rest_framework.response
            returns HTTP 200 status if data returned successfully,error message otherwise
        """
        try:
            if request.query_params.get("keyword_value"):
                keywords = Keyword.objects.filter(
                    keyword_value__icontains=request.query_params.get("keyword_value")
                ).order_by('-id')
            else:
                keywords = Keyword.objects.all().order_by('-id')
            page = self.paginate_queryset(keywords)
            if page is not None:
                serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
                return Response(
                    response_standard(response_data=serializer.data, message=None, _status=200),
                    status=status.HTTP_200_OK,
                )
            else:
                serializer = self.serializer_class(keywords, many=True)
                return Response(
                    response_standard(response_data=serializer.data, message=None, _status=200),
                    status=status.HTTP_200_OK,
                )

        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


class GetKeywordById(APIView, PaginationHandlerMixin):
    """
    GetKeywordById Class

    This view performs GET operation for Keyword

    Parameters
    ----------
    APIView : rest_framework.views
    """
    serializer_class = KeywordSerializer

    @swagger_auto_schema(
        responses={
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
    )
    def get(self, request, pk):
        """
        HTTP GET request

        An HTTP endpoint that returns specific Keyword

        Parameters
        ----------
        request : django.http.request

        Returns
        -------
        rest_framework.response
            returns HTTP 200 status if data returned successfully,error message otherwise
        """
        try:
            keywords = Keyword.objects.get(pk=pk)
            serializer = KeywordSerializer(keywords)
            return Response(
                response_standard(response_data=serializer.data, message=None, _status=200), status=status.HTTP_200_OK
            )
        except Keyword.DoesNotExist:
            return Response(
                response_standard(response_data=None, message=f"Keyword Object not exist against id {pk}", _status=400),
                "400",
            )
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


class EducationLevel(APIView):

    @swagger_auto_schema(
        request_body=EducationLevelSerializer,

        responses={
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        """
        HTTP POST request

        An HTTP endpoint that saves a keyword in DB

        Parameters
        ----------
        request : django.http.request

        Returns
        -------
        rest_framework.response
            returns success message if data saved successfully,error message otherwise
        """
        try:

            serializer = EducationLevelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(response_standard(response_data=serializer.data, message=None, _status=201), "201")
            else:
                return Response(
                    response_standard(response_data=None, message=error_fields_finding(serializer.errors), _status=400),
                    "400",
                )
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")

    def get(self, request):
        """
        HTTP PUT request

        An HTTP endpoint that updates a keyword for provided PK

        Parameters
        ----------
        request : django.http.request

        pk : integer

        Returns
        -------
        rest_framework.response
            returns success message if data updated successfully,error message otherwise
        """
        try:
            levels_obj = EducationLevels.objects.all()
            serializer = EducationLevelSerializer(levels_obj, many=True)

            return Response(response_standard(response_data=serializer.data, message=None, _status=200), "200")

        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")


# class IndustryClassifier(APIView):
#
#     @swagger_auto_schema(
#         request_body=IndustrySerializer,
#
#         responses={
#             200: "OK",
#             400: "Bad Request",
#             401: "Unauthorized",
#             500: "Internal Server Error",
#         },
#     )
#     def post(self, request):
#         """
#         HTTP POST request
#
#         An HTTP endpoint that saves a keyword in DB
#
#         Parameters
#         ----------
#         request : django.http.request
#
#         Returns
#         -------
#         rest_framework.response
#             returns success message if data saved successfully,error message otherwise
#         """
#         try:
#
#             serializer = IndustrySerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(response_standard(response_data=serializer.data, message=None, _status=201), "201")
#             else:
#                 return Response(
#                     response_standard(response_data=None, message=error_fields_finding(serializer.errors), _status=400),
#                     "400",
#                 )
#         except Exception as e:
#             return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")
#
#     def get(self, request):
#         """
#         HTTP PUT request
#
#         An HTTP endpoint that updates a keyword for provided PK
#
#         Parameters
#         ----------
#         request : django.http.request
#
#         pk : integer
#
#         Returns
#         -------
#         rest_framework.response
#             returns success message if data updated successfully,error message otherwise
#         """
#         try:
#             levels_obj = IndustryDataset.objects.all()
#             serializer = IndustrySerializer(levels_obj, many=True)
#
#             return Response(response_standard(response_data=serializer.data, message=None, _status=200), "200")
#
#         except Exception as e:
#             return Response(response_standard(response_data=None, message=e.args[0], _status=500), "500")
