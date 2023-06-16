class Toaster:
    def __init__(self):
        self.state = False
        self.temperature = 0
        self.time = 0

    def turn_on(self):
        if not self.state:
            self.state = True
            print("Toaster is now turned on.")
        else:
            print("Toaster is already on.")

    def turn_off(self):
        if self.state:
            self.state = False
            print("Toaster is now turned off.")
        else:
            print("Toaster is already off.")

    def toast(self, time, temperature):
        if self.state:
            self.state = True
            self.time = time
            self.temperature = temperature
            print(f"Toaster is toasting for {time} seconds at {temperature}°C.")
        else:
            print("Toaster is not turned on.")

    def check_status(self):
        print(f"Toaster state: {'on' if self.state else 'off'}")
        print(f"Toaster temperature: {self.temperature}°C")
        print(f"Toaster time: {self.time} seconds")


# Utilisation du grille-pain
my_toaster = Toaster()
my_toaster.check_status()

my_toaster.turn_on()
my_toaster.toast(30, 200)
my_toaster.check_status()

# my_toaster.turn_off()
# my_toaster.check_status()
