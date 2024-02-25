
params = 'id=1&category=10'

res = params.split('&')

for item in res:
    k, v = item.split('=')
    print(k)
    print(v)