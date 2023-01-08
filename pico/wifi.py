import time
import network


def connect(ssid='Betelgeuse', password='alphaorion', timeout=None):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    wlan.config(pm=0xa11140)  # Turns off low power mode

    start = time.ticks_ms()
    while not wlan.isconnected() and (timeout is None or time.tick_diff(time.ticks_ms(), start) < timeout * 1000):
        time.sleep(0.1)

    if not wlan.isconnected():
        return False

    status = wlan.ifconfig()
    return status
