from market import get_candles
from volume import calculate_average_volume, get_current_volume

candles = get_candles("BTCUSDT")

avg_volume = calculate_average_volume(candles)
current_volume = get_current_volume(candles)

print("Average Volume:", avg_volume)
print("Current Volume:", current_volume)