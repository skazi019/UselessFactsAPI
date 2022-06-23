from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
import json
import pandas as pd


class FactView(APIView):
    def get(self, request):
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
    def get(self, request, id):
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
