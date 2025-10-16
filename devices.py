# devices.py - Điều khiển thiết bị (đèn, quạt, rèm)

from gpiozero import OutputDevice

# Gán chân điều khiển
light = OutputDevice(27)  # GPIO27
fan = OutputDevice(22)    # GPIO22

def control_light(state):
    if state == "ON":
        light.on()
    elif state == "OFF":
        light.off()

def control_fan(state):
    if state == "ON":
        fan.on()
    elif state == "OFF":
        fan.off()
