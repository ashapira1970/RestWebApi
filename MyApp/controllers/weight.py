import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class WeightController:
    @api_view(["POST"])
    def IdealWeight(self):
        try:
            height = json.loads(self.body)
            weight = str(height * 10)
            return JsonResponse("Ideal weight should be:" + weight + " kg", safe=False)
        except ValueError as e:
            from rest_framework.response import Response
            from rest_framework import status
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

    @api_view(["GET"])
    def BMI(self):
        try:
            if not self.body:
                return Response("bad params", status.HTTP_400_BAD_REQUEST)
            input_param = json.loads(self.body)
            if not input_param:
                return Response("bad params", status.HTTP_400_BAD_REQUEST)
            height = int(input_param['height'])
            weight = int(input_param['weight'])
            return JsonResponse("BMI is:" + str(weight / ((height / 100) ** 2)), safe=False)
        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
