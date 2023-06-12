from src.Keyboard import Keyboard, langs_Mixin

kb = Keyboard('Dark Project KD87A', 9600, 5)
assert str(kb) == "Dark Project KD87A"

assert str(kb.language) == "EN"

kb.change_lang()
assert str(kb.language) == "RU"

# Сделали RU -> EN -> RU
kb.change_lang().change_lang()
assert str(kb.language) == "RU"

