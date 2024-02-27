from zeep import Client

client= Client ("https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL")

result = client.service.NumberToDollars(1)
print(result)