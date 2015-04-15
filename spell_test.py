from spell import Spell
import unittest


class spell_test(unittest.TestCase):
    def setUp(self):
        self.spell = Spell("Spell name", 100, 20, 3)

    def test_init(self):
        self.assertEqual(self.spell.name, "Spell name")
        self.assertEqual(self.spell.damage, 100)
        self.assertEqual(self.spell.mana_cost, 20)
        self.assertEqual(self.spell.cast_range, 3)

if __name__ == '__main__':
    unittest.main()
