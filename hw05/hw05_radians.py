import math

print("각   /라디안   /sin     /cos     /tan   ")

for degree in range(0, 101):
    rad = math.radians(degree)
    sin_value = math.sin(rad)
    cos_value = math.cos(rad)
    tan_value = math.tan(rad)

    print(f"{degree}° / {rad:.4f} / {sin_value:.4f} / {cos_value:.4f} / {tan_value:.4f}")

