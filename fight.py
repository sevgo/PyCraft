from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell


class Fight():
    def __init__(self, hero, enemy):
        self.hero = hero
        self.hero.learn(Spell('a', 20, 20, 2))
        # hero = Hero()
        self.enemy = enemy
        self.enemy.learn(Spell('b', 25, 20, 2))
        # enemy = Enemy()

    def start(self):
        start_battle = "A fight is started between our Hero(health={}, mana={})"
        start_battle += " and Enemey(health={}, mana={}, damage={})"
        print(start_battle.format(self.hero.get_health(), self.hero.get_mana(),
              self.enemy.get_health(), self.enemy.get_mana(), self.enemy.damage))
        while self.hero.is_alive() and self.enemy.is_alive():
            hero_attack = self.hero.attack()
            self.enemy.take_damage(hero_attack[1])
            if hero_attack[0] == 'spell':
                spell_text = 'Hero casts a {}, hits enemy for {} dmg. Enemy health is {}'
                print(spell_text.format(self.hero.spell.name, hero_attack[1], enemy.health))
            if self.enemy.is_alive():
                enemy_attack = self.enemy.attack()
                if enemy_attack[0] == 'spell':
                    spell_text = 'Enemy casts a {}, hits hero for {} dmg. Hero health is {}'
                    print(spell_text.format(self.enemy.spell.name, enemy_attack[1], enemy.health))
                self.hero.take_damage(enemy_attack[1])
        return self.hero if self.hero.is_alive() else self.enemy


if __name__ == '__main__':
    weapon = Weapon('name', 2)
    spell = Spell('name', 0, 0, 0)
    hero = Hero()
    hero.equip(weapon)
    enemy = Enemy()
    Fight(hero, enemy).start()
