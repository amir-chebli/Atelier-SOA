from zeep import Client

# Define the WSDL URL of your Spyne SOAP service
wsdl_url = 'http://localhost:8000/?wsdl'

# Create a Zeep client
client = Client(wsdl_url)

# Call the say_hello operation
response = client.service.say_hello(name='John', times=3)

# Print the response
for greeting in response:
    print(greeting)
