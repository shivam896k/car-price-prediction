from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from rest_framework.viewsets import ModelViewSet
import pickle
import os

path = os.getcwd()
model = pickle.load(open(f'{path}/endpoints/random_forest_regression_model.pkl', 'rb'))

@api_view(['GET'])
@schema(None)
def view(request):
    data = request.query_params.dict()
    Present_Price = int(data.get('Present_Price'))
    Kms_Driven2 = int(data.get('Kms_Driven2'))
    Owner = int(data.get('Owner'))
    Year = int(data.get('Year'))
    Fuel_Type_Diesel = int(data.get('Fuel_Type_Diesel'))
    Fuel_Type_Petrol = int(data.get('Fuel_Type_Petrol'))
    Seller_Type_Individual = int(data.get('Seller_Type_Individual'))
    Transmission_Mannual = int(data.get('Transmission_Mannual'))
    Year = 2020-Year

    price = model.predict([[Present_Price, Kms_Driven2, Owner, Year, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
    return Response({"Selling Price": price})



'''
Payload:
{
    "Present_Price": "10",
    "Kms_Driven2": "24000",
    "Owner": "4",
    "Year": "2013",
    "Fuel_Type_Diesel": "0",
    "Fuel_Type_Petrol": "1",
    "Seller_Type_Individual": "0",
    "Transmission_Mannual": "1"
}


'''