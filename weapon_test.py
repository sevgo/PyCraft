from weapon import Weapon
import unittest


class weapon_test(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon("Weapon name", 20)

    def test_init(self):
        self.assertEqual(self.weapon.name, "Weapon name")
        self.assertEqual(self.weapon.damage, 20)

if __name__ == '__main__':
    unittest.main()
