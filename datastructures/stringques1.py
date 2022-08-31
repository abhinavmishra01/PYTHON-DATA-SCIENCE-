from itertools import count
from string import ascii_lowercase

msg = 'Life Before Death, Hope before Despair, Journey before Destination'
for char in ascii_lowercase:
    print(f'{char}- {msg.count(char)}')

    