from modLevy import Levy
from Levenshtein import distance

s='конь'
pairs=['лена', 'лень',
    'огонь','конница',
    'кобыла','конюшня',
    'конёк','компьютеризация',
]

for t in pairs:
    print(s, t, Levy(s,t), distance(s,t))

