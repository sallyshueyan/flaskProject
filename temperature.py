from flask import Flask

app = Flask(__name__)


@app.route('/temperature_in_faherenheit/100.2')
def temperature_in_faherenheit(celsius=float("100.2")):
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"celsius = {celsius}\n fahrenheit = {fahrenheit}"


@app.route('/temperature_in_celsius/212.36')
def temperature_in_celsius(fahrenheit=float("212.36")):
    celsius = 5 / 9 * (fahrenheit - 32)
    return f"fahrenheit = {fahrenheit}\ncelsius = {celsius:.1f}"


if __name__ == '__main__':
    app.run()
