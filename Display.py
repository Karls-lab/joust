class headsUpDisplay():
    def __init__(self):
        self.fuelAmount = 100
        text = "Fuel"
        font = pygame.font.Font('freesansbold.ttf', 20)
        self.img = font.render(text, True, WHITE)
       
        self.fuel = pygame.Surface([self.fuelAmount, 20])
        self.fuel.fill(WHITE)

    def updateFuel(self, amount):
        self.fuelAmount -= amount
        
    def updateHUD(self):
         screen.blit(self.img, (800, 20))
         screen.blit(self.fuel, (850, 20))


