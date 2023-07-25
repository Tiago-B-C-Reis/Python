class TempConverter:
    def __init__(self, C: float, F: float):
        self.C = C
        self.F = F

    def read_fahrenheit(self) -> float:
        return f'{self.F:.2f}'  # Use f-string formatting for fixed precision

    def read_celsius(self) -> float:
        return f'{self.C:8.2f}'  # Use f-string formatting for fixed precision

    def show_temp(self):
        print(f'Celsius = {self.read_celsius()} °C\nFahrenheit = {self.read_fahrenheit()} °')


if __name__ == '__main__':
    temperature_celsius = float(input('What is the temperature in Celsius? '))
    T = TempConverter(temperature_celsius, (temperature_celsius * 1.8) + 32)
    T.show_temp()