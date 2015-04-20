from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell


class Fight():
    def __init__(self, hero, enemy):
        self.hero = hero
        # hero = Hero()
        self.enemy = enemy
        # enemy = Enemy()

    def start(self):
        start_battle = "A fight is started between our Hero(health={}, mana={})"
        start_battle += " and Enemy(health={}, mana={}, damage={})"
        print(start_battle.format(self.hero.get_health(), self.hero.get_mana(),
              self.enemy.get_health(), self.enemy.get_mana(), self.enemy.damage))
        while self.hero.is_alive() and self.enemy.is_alive():
            if self.hero.can_cast():
                spell = "Hero casts a {}, hits enemy for {} dmg. Enemy health is {}"
                damage = self.hero.attack(by='spell')
                self.enemy.take_damage(damage)
                print(spell.format(self.hero.spell.name,
                                   self.hero.spell.damage, self.enemy.health))
            elif self.hero.weapon != None:
                weapon = "Hero hits with {} for {} dmg. Enemy health is {}"
                damage = self.hero.attack(by='weapon')
                self.enemy.take_damage(damage)
                print(weapon.format(self.hero.weapon.name,
                                    self.hero.weapon.damage, self.enemy.health))
            if enemy.is_alive():
                if self.enemy.can_cast():
                    spell = "Enemy casts a {}, hits hero for {} dmg. Hero health is {}"
                    damage = self.enemy.attack(by='spell')
                    self.hero.take_damage(damage)
                    print(spell.format(self.hero.spell.name,
                                       self.hero.spell.damage, self.enemy.health))
                elif self.enemy.weapon != None:
                    weapon = "Enemy hits with {} for {} dmg. Hero health is {}"
                    damage = self.enemy.attack(by='weapon')
                    self.hero.take_damage(damage)
                    print(weapon.format(self.hero.weapon.name,
                                        self.hero.weapon.damage, self.enemy.health))
                else:
                    hands = "Enemy hits hero for {} dmg. Hero health is {}."
                    damage = self.enemy.attack()
                    self.hero.take_damage(damage)
                    print(hands.format(self.enemy.damage, self.hero.health))

        return self.hero if self.hero.is_alive() else self.enemy


if __name__ == '__main__':
    weapon = Weapon('WW', 2)
    spell = Spell('SS', 5, 40, 2)
    hero = Hero()
    hero.equip(weapon)
    hero.learn(spell)
    enemy = Enemy()
    Fight(hero, enemy).start()
