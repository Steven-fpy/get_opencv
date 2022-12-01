import requests

# url = 'http://www.naver.com/'
# res = requests.get(url)
# requests.post()

# # print('res: ', res)
# # print('res: ', res.text) #text를 넣으면 utf-8롤 인코딩해서 보여줌
# # print('res: ', res.content) # 바이너리 타입

# url = 'https://pokeapi.co/api/v2/pokemon/'

limit = 50 

while True:

    inputText = input('page number : ')

    if not inputText.isdigit():
        continue

    page = int(inputText)
    
    if page <= 0:
        continue

    url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={limit * (page-1)}'

    res = requests.get(url)
    resonseData = res.json()
    results = resonseData['results']    
    for result in results:
    
        print(result)
# requests.post()

# print('res: ', res)
# print('res: ', res.text) #text를 넣으면 utf-8롤 인코딩해서 보여줌
# print('res: ', res.content) # 바이너리 타입

# dict
# resonseData = res.json()
# print('keys: ', resonseData.keys())

# results = resonseData['results']
# print('results', results)

# for result in results:
#     print(result)

# print('res: ', res.json()) #json


