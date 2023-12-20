# soap_consumer.py
from zeep import Client

# Specify the URL for the SOAP service
soap_url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'

# Create a Zeep client
client = Client(soap_url)

# Set the 'SOAPAction' header using the 'settings' attribute
client.settings.extra_http_headers = {'SOAPAction': 'http://www.oorsprong.org/websamples.countryinfo/CapitalCity'}

# Specify the method you want to call (e.g., CapitalCity)
response = client.service.CapitalCity(sCountryISOCode='US')

print("Data from SOAP API:")
print(response)
