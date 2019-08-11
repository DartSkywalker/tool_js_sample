from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import requests
# Create your views here.
from django.shortcuts import render_to_response
import re
import json
from django.core import serializers

temp = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

<title>AJAX Test</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
</head>
<body>

<script type="text/javascript">
    $(document).ready(function () {
        $("#ajax-text-me").click(function() {
            $.ajax({
                type: 'GET',
                async: true,
                url: '/ajax/',
                data: "param1=value1&param2=value2;",
                success: function(data) {
                    $("#more-text-here1").append(data['first-text']);
                    $("#more-text-here2").append(data['second-text']);
                },
                dataType: 'json',
            });
        });
    });
</script>

<center><h1><a href="#" id="ajax-text-me">Press me boy I`m AJAX :)</a></h1></center>
<center><div id="more-text-here1"><br></div></center>
<center><div id="more-text-here2"></div></center>
</body>
</html>"""


def form(request):

    return render_to_response('dev.html')

#GET /ajax/?{%22area_name%22:%22AREA%20SEVERAL%20LETTER%22,%22domain_name%22:%22sad%22,%22feature_id%22:%22asd%22,%22feature_name%22:%22asdd%22} HTTP/1.1" 200 106

def add_area_ajax(request):
    if request.is_ajax():

        # print(request)
        data_to_parse = str(request)
        print(data_to_parse)
        area_name = re.search('area_name%22:%22(.*)%22,%22domain_name', data_to_parse).group(1).replace('%20', " ")
        domain_name = re.search('domain_name%22:%22(.*)%22,%22feature_id', data_to_parse).group(1).replace('%20', " ")
        feature_id = re.search('feature_id%22:%22(.*)%22,%22feature_name', data_to_parse).group(1).replace('%20', " ")
        feature_name = re.search('feature_name%22:%22(.*)%22', data_to_parse).group(1).replace('%20', " ")
        print(area_name, domain_name, feature_id, feature_name)
        #Here query to DB to check if its present in database


        #tamplate for OK response (reload the page)

        #if success:
        # response = {'status' : 'success'}

        #if fail:
        response = {'status' : 'failed'}

        return JsonResponse(response)
    else:
        raise Http404

def add_domain_ajax(request):
    if request.is_ajax():

        # print(request)
        data_to_parse = str(request)
        print(data_to_parse)
        area_name = re.search('area_name%22:%22(.*)%22,%22domain_name', data_to_parse).group(1).replace('%20', " ")
        domain_name = re.search('domain_name%22:%22(.*)%22,%22feature_id', data_to_parse).group(1).replace('%20',
                                                                                                           " ")
        feature_id = re.search('feature_id%22:%22(.*)%22,%22feature_name', data_to_parse).group(1).replace('%20',
                                                                                                           " ")
        feature_name = re.search('feature_name%22:%22(.*)%22', data_to_parse).group(1).replace('%20', " ")
        print(area_name,domain_name,feature_id,feature_name)
        # Here query to DB to check if its present in database

        # template for OK response (reload the page)

        # if success:
        # response = {'status' : 'success'}

        # if fail:
        response = {'status' : 'failed'}

        return JsonResponse(response)
    else:
        raise Http404

def add_feature_ajax(request):
    if request.is_ajax():

        # print(request)
        data_to_parse = str(request)
        print(data_to_parse)
        area_name = re.search('area_name%22:%22(.*)%22,%22domain_name', data_to_parse).group(1).replace('%20', " ")
        domain_name = re.search('domain_name%22:%22(.*)%22,%22feature_id', data_to_parse).group(1).replace('%20',
                                                                                                           " ")
        feature_id = re.search('feature_id%22:%22(.*)%22,%22feature_name', data_to_parse).group(1).replace('%20',
                                                                                                           " ")
        feature_name = re.search('feature_name%22:%22(.*)%22', data_to_parse).group(1).replace('%20', " ")
        print(area_name,domain_name,feature_id,feature_name)
        # Here query to DB to check if its present in database

        # template for OK response (reload the page)

        # if success:
        # response = {'status' : 'success'}

        # if fail:
        response = {'status': 'failed'}

        return JsonResponse(response)
    else:
        raise Http404