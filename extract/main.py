from API.cotation_collector import CotationCollector

lista = ['ITUB4', 'SUZB3']

result = CotationCollector().start(acoes=lista)
print(result)