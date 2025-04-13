class GameCharacter:
    """Base class for all game characters"""
    def __init__(self, name, health, attack_power):
        self._name = name          # Protected attribute
        self._health = health      # Protected attribute
        self._attack_power = attack_power  # Protected attribute
        self.__secret_ability = "Unknown"  # Private attribute

    def attack(self):
        """Public method to attack"""
        return f"{self._name} attacks with {self._attack_power} damage!"

    def take_damage(self, damage):
        """Public method to handle damage"""
        self._health -= damage
        if self._health <= 0:
            return f"{self._name} has been defeated!"
        return f"{self._name} has {self._health} health remaining."

    def get_secret_ability(self):
        """Getter for private attribute"""
        return self.__secret_ability

    def set_secret_ability(self, ability):
        """Setter for private attribute"""
        self.__secret_ability = ability

    def __str__(self):
        return f"{self._name} (Health: {self._health}, Attack: {self._attack_power})"


class Hero(GameCharacter):
    """Hero class inheriting from GameCharacter"""
    def __init__(self, name, health, attack_power, hero_class):
        super().__init__(name, health, attack_power)
        self.hero_class = hero_class  # New attribute
        self._special_charges = 3     # Protected attribute
        self.set_secret_ability("Divine Protection")

    def special_attack(self):
        """Hero-specific method"""
        if self._special_charges > 0:
            self._special_charges -= 1
            return f"{self._name} uses {self.hero_class} special attack! {self._special_charges} charges left."
        return "No special charges remaining!"

    def heal(self):
        """Hero-specific method"""
        self._health += 20
        return f"{self._name} heals for 20 HP. Current health: {self._health}"


class Enemy(GameCharacter):
    """Enemy class inheriting from GameCharacter"""
    def __init__(self, name, health, attack_power, enemy_type):
        super().__init__(name, health, attack_power)
        self.enemy_type = enemy_type  # New attribute
        self.set_secret_ability("Dark Aura")

    def enrage(self):
        """Enemy-specific method"""
        self._attack_power += 5
        return f"{self._name} becomes enraged! Attack power increased to {self._attack_power}."

    def __str__(self):
        """Polymorphism - overriding parent method"""
        return f"{self.enemy_type} {self._name} (Health: {self._health}, Attack: {self._attack_power})"


# Testing our classes
if __name__ == "__main__":
    # Create instances
    knight = Hero("Sir Gallahad", 120, 15, "Paladin")
    dragon = Enemy("Smaug", 200, 25, "Dragon")

    # Demonstrate functionality
    print(knight)
    print(dragon)
    print(knight.attack())
    print(dragon.attack())
    print(knight.special_attack())
    print(dragon.enrage())
    print(knight.take_damage(30))
    print(knight.heal())
    print(f"Knight's secret ability: {knight.get_secret_ability()}")