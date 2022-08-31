from sys import set_coroutine_origin_tracking_depth
from tracemalloc import start


sentence= 'this is that and that is this, that that and this is this'
start= 0 
query = ' that'
while True:
    idx = sentence.find(query, start)
    if idx ==-1:
        break
    print(f'{query} at { idx}')
start= idx +1