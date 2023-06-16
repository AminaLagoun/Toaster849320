class Toaster:
    def __init__(self):
#allumé et eteint sont des booléens
        self.state = False
        self.temperature = 0
        self.time = 0
#l'etat allumé
    def turn_on(self):
        if not self.state:
            self.state = True
            print("Toaster is now turned on.")
        else:
            print("Toaster is already on.")
#l'etat eteint
    def turn_off(self):
        if self.state:
            self.state = False
            print("Toaster is now turned off.")
        else:
            print("Toaster is already off.")

    def toast(self):
        if self.state:
            temperature = float(input("Enter the desired temperature (in °C): "))
#l'utilisateur met la température
            time = float(input("Enter the desired toasting time (in seconds): "))
#l'utilisateur met la durée
            self.temperature = temperature
            self.time = time
            print(f"Toaster is toasting for {time} seconds at {temperature}°C.")

            if temperature < 150:
                print("Toast is cold.")
            elif temperature < 180:
                print("Toast is warm.")
            elif temperature < 200:
                print("Toast is hot.")
            elif temperature < 250:
                if time < 30:
                    print("Toast is warm.")
                elif time < 60:
                    print("Toast is grilled.")
                else:
                    print("Toast is burnt!")
            else:
                print("Risk of fire detected! Switching off toaster.")
#tu vas pas brûler ta cuisine
                self.turn_off()
        else:
            print("Toaster is not turned on.")
#la machine affiche la température et la durée
    def check_status(self):
        print(f"Toaster state: {'on' if self.state else 'off'}")
        print(f"Toaster temperature: {self.temperature}°C")
        print(f"Toaster time: {self.time} seconds")



# Utilisation du grille-pain
my_toaster = Toaster()
my_toaster.check_status()

my_toaster.turn_on()
my_toaster.toast()
my_toaster.check_status()
print('ejecté')

# my_toaster.turn_off()
# my_toaster.check_status()
