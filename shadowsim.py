class Spells:
    """The stats for direct damage spells"""
    def __init__(self, sp_weight, cast_time, cooldown, insanity_gen, insanity_cost):
        self.spell_damage = sp_weight*intellect
        self.cast_time = cast_time
        self.cooldown = cooldown
        self.insanity_gen_on_cast = insanity_gen
        self.insanity_cost = insanity_cost


class Dots:
    """Stats for channeled and damage-over-time spells"""
    def __init__(self, sp_weight, sp_bias, dot_duration, cast_time, cooldown, insanity_gen_on_cast,
                 insanity_gen_per_hit, insanity_cost):
        self.dot_duration = dot_duration
        self.dot_hit_interval = 3 / (1 + haste_percent)


intellect = 350
crit_rating = 155
haste_rating = 174
mastery_rating = 72
versatility_rating = 49
crit_chance = crit_rating*0.1415/155
haste_percent = haste_rating*0.1729/174
mastery_percent = mastery_rating*0.0337/72
versatility_percent = versatility_rating*0.0402/49

print(f'Haste %: {haste_percent}')
print(f'Crit chance: {crit_chance}')
print(f'Mastery %: {mastery_percent}')
print(f'Versatility %: {versatility_percent}')
