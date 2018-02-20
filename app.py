from lifxlan import LifxLAN

from flask import Flask, request, render_template
app = Flask(__name__)

lifx = LifxLAN()
lifx.get_devices() # fetch and cache all devices

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/switch', methods=['POST'])
def switch():
    params = request.get_json()
    device_name = params.get('device')
    devices = [lifx.get_device_by_name(device_name)] if device_name else lifx.get_devices()
    power = params.get('power')
    color = params.get('color')
    for device in devices:
        if power: device.set_power(power, 200, True)
        if color: device.set_color([int(n) for n in color.split(',')], 200, True)
    return ''
