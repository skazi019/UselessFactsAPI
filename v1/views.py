from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import random
import json
import pandas as pd


class FactView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    manual_parameters = [
        openapi.Parameter(
            "Authorizarion",
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description="obtained after successful login or regisration, click on the lock icon(right) in the header above and pass value for 'Token' as 'Token <token received after login/registration>'",
        ),
    ]

    response_schema_dict = {
        "200": openapi.Response(
            description="Returns status and the fact along with the fact id",
            examples={
                "application/json": {
                    "status": "success",
                    "data": {"id": "<fact_id>", "fact": "some useless fact"},
                }
            },
        ),
        "401": openapi.Response(
            description="Invalid Authorization",
            examples={
                "application/json": {
                    "detail": "Invalid token/Authentication credentials not provided",
                }
            },
        ),
        "500": openapi.Response(
            description="Some error in backend",
            examples={
                "application/json": {
                    "status": "error",
                }
            },
        ),
    }

    @swagger_auto_schema(
        manual_parameters=manual_parameters,
        operation_summary="Returns a useless fact at random",
        operation_description="After successful authentication by passing the Token, return a useless fact with it's id",
        responses=response_schema_dict,
    )
    def post(self, request, *args, **kwargs):
        try:
            with open("./facts.json", "rb") as f:
                all_facts = json.load(f)

            fact = random.choice(all_facts["facts"])
            return Response(
                {
                    "status": "success",
                    "data": {"id": fact["id"], "fact": fact["fact"]},
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class FactIDView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    manual_parameters = [
        openapi.Parameter(
            "Authorizarion",
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description="obtained after successful login or regisration, click on the lock icon(right) in the header above and pass value for 'Token' as 'Token <token received after login/registration>'",
        ),
    ]

    response_schema_dict = {
        "200": openapi.Response(
            description="Returns status and the fact along with the fact id",
            examples={
                "application/json": {
                    "status": "success",
                    "data": {"id": "<fact_id>", "fact": "some useless fact"},
                }
            },
        ),
        "401": openapi.Response(
            description="Invalid Authorization",
            examples={
                "application/json": {
                    "detail": "Invalid token/Authentication credentials not provided",
                }
            },
        ),
        "500": openapi.Response(
            description="Some error in backend",
            examples={
                "application/json": {
                    "status": "error",
                }
            },
        ),
    }

    @swagger_auto_schema(
        manual_parameters=manual_parameters,
        operation_summary="Returns a useless fact for that paticular ID",
        operation_description="""
        After successful authentication by passing the Token, return a useless fact with it's id
        Note - click the "Example Value" button for each response to check how the sample value would look like, by default it would show a loader.
        """,
        responses=response_schema_dict,
    )
    def post(self, request, id):
        try:
            with open("./facts.json", "rb") as f:
                all_facts = json.load(f)

            all_facts_df = pd.DataFrame.from_records(all_facts["facts"])
            fact = all_facts_df[all_facts_df["id"] == id]
            fact = json.loads(fact.to_json(orient="records"))[0]

            return Response(
                {
                    "status": "success",
                    "data": {"id": fact["id"], "fact": fact["fact"]},
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print(f"Error in id view: {e}")
            return Response(
                {
                    "status": "error",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
