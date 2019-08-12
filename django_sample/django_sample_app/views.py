from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import requests
# Create your views here.
from django.shortcuts import render_to_response
import re
import json
from django.core import serializers
import MySQLdb


def form(request):

    return render_to_response('dev.html')

def create_connection():
    try:
        con = MySQLdb.connect(user="root", password='18041997',
                              host='localhost',
                              database='coverage_dev', use_unicode=True, charset="utf8mb4")
        print("Successfully connected to DB (^_^)")
        # print("Please wait for the process to be done.......")
        return con
    except Exception as err:
        if (err):
            print("Oops, Something went wrong. Connection failed :(")
            print(err)
# print(create_connection())

def add_area_ajax(request):
    if request.is_ajax():

        # print(request)
        data_to_parse = str(request)
        area_name = re.search('area_name%22:%22(.*)%22,%22domain_name', data_to_parse).group(1).replace('%20', " ")
        domain_name = re.search('domain_name%22:%22(.*)%22,%22feature_id', data_to_parse).group(1).replace('%20', " ")
        feature_id = re.search('feature_id%22:%22(.*)%22,%22feature_name', data_to_parse).group(1).replace('%20', " ")
        feature_name = re.search('feature_name%22:%22(.*)%22', data_to_parse).group(1).replace('%20', " ")
        print(area_name, domain_name, feature_id, feature_name)

        #Here query to DB to check if its present in database
        is_duplicate_query = "select * from Area where Area_Name=" + "'" + area_name + "'"
        con = create_connection()
        cur = con.cursor()
        cur.execute(is_duplicate_query)
        is_duplicate_result = [item[0] for item in cur.fetchall()]
        print(is_duplicate_result)
        #check if no duplicates - go ahead
        if not is_duplicate_result:
            insert_area_query = "insert into Area (Area_Name) values (" + "'" + area_name + "'" + ")"
            cur.execute(insert_area_query)
            con.commit()
            print("!!!!INSERTED NEW AREA")


        find_area_id_query = "select Area_ID from Area where Area_Name=" + "'" + area_name + "'"
        cur.execute(find_area_id_query)
        area_id = [item[0] for item in cur.fetchall()]
        print("[!!!!!!!!!]Area ID!", area_id)
        insert_domain_query = "insert into Global_Domain (Area_ID, Domain_Name) values (" + "'" + str(area_id[0]) + "'," + "'" + domain_name + "'" + ")"
        cur.execute(insert_domain_query)
        con.commit()

        find_domain_id_query = "select Domain_ID from Global_Domain where Domain_Name=" + "'" + domain_name + "'"
        cur.execute(find_domain_id_query)
        domain_id = [item[0] for item in cur.fetchall()]
        print("[!!!!!!!!!]DOMAIN ID!", domain_id)
        insert_feature_query = "insert into Feature_ID (Feature_ID, Area_ID, Domain_ID, Feature_Name) " \
                               "values ('%s', %d, %d, '%s')" % (feature_id, area_id[0], domain_id[0], feature_name)
                               # "values (" + "'" + feature_id + "'," + "'" + str(area_id[0]) + "'," + "'" + str(domain_id[0]) + "'," + feature_name + ")"
        cur.execute(insert_feature_query)
        con.commit()


        cur.close()

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