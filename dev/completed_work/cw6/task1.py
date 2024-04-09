# Задание 1
def time_conv(value: float = 0.0, unit_in: str = 'ms', unit_out: str = 'ms') -> str:
    """
    Конвертирует еденицы измерения времени.

    :param value: любое положительное число и ноль
    :param unit_in: принимает: ms, s, min, h
    :param unit_out: принимает: ms, s, min, h
    :return: <знаечние(value)><единица измерения(unit_out)>
    """

    if value < 0:
        raise ValueError('параметр "value" принимает только положительные значения')

    multipliers = {
        'ms':  {'ms': 1,       's': 1/1000, 'min': 1/60000, 'h': 1/3600000},
        's':   {'ms': 1000,    's': 1,      'min': 1/60,    'h': 1/3600},
        'min': {'ms': 60000,   's': 60,     'min': 1,       'h': 1/60},
        'h':   {'ms': 3600000, 's': 3600,   'min': 60,      'h': 1}
    }

    value *= multipliers[unit_in][unit_out]

    return f'{value}{unit_out}'


print(time_conv(45000, unit_out='min'))
