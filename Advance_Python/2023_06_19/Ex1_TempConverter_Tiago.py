class TempConverter:
    """
    A temperature converter class that converts Celsius to Fahrenheit.

    Usage:
    - Initialize an instance of TempConverter with a Celsius temperature value.
    - Call the show_temp() method to print the Celsius and Fahrenheit temperatures.
    """
    def __init__(self, C: float, F: float):
        self.C = C
        self.F = F

    def read_fahrenheit(self) -> float:
        """
        Read the Fahrenheit temperature.

        Returns:
        - The Fahrenheit temperature.
        """
        return f"{self.F:.2f}"  # Use f-string formatting for fixed precision

    def read_celsius(self) -> float:
        """
        Read the Celsius temperature.

        Returns:
        - The Celsius temperature.
        """
        return f"{self.C:.2f}"  # Use f-string formatting for fixed precision

    def show_temp(self):
        """
        Print the Celsius and Fahrenheit temperatures.
        """
        print(f"C = {self.read_celsius()}  |  F = {self.read_fahrenheit()}")


if __name__ == "__main__":
    temperature_celsius = float(input("What is the temperature in Celsius? "))
    T = TempConverter(temperature_celsius, (temperature_celsius * 1.8) + 32)
    T.show_temp()
