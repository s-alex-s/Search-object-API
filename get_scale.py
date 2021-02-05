def get_spn(toponym_spn):
    lowerC = list(map(float, toponym_spn['lowerCorner'].split()))
    upperC = list(map(float, toponym_spn['upperCorner'].split()))
    return f'{upperC[0] - lowerC[0]},{upperC[1] - lowerC[1]}'
