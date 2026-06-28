def calculate_average_volume(candles, period=20):

    volumes = [float(candle[5]) for candle in candles]

    recent_volumes = volumes[-period:]

    return sum(recent_volumes) / len(recent_volumes)


def get_current_volume(candles):

    return float(candles[-1][5])