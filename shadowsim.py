class Spells:
    """Stats for direct damage spells"""
    def __init__(self, sp_weight, cast_time, cooldown, insanity_gen, insanity_cost):
        self.spell_damage = sp_weight*intellect
        self.cast_time = cast_time/(1+haste_percent)
        # Does haste effect cooldowns?
        self.cooldown = cooldown
        self.insanity_gen_on_cast = insanity_gen
        self.insanity_cost = insanity_cost


class Dots:
    """Stats for damage-over-time spells"""
    def __init__(self, sp_weight, dot_duration, hit_interval, cast_time, cooldown, insanity_gen_on_cast):
        self.spell_damage = sp_weight*intellect*(1+haste_percent)
        self.dot_duration = dot_duration
        self.dot_hit_interval = hit_interval / (1+haste_percent)
        self.cast_time = cast_time/(1+haste_percent)
        # Check to see if cooldowns change with haste
        self.cooldown = cooldown
        self.insanity_gen_on_cast = insanity_gen_on_cast


class Channeled:
    """Stats for channeled spells"""
    def __init__(self, sp_weight, dot_duration, hit_interval, insanity_gen):
        self.spell_damage = sp_weight*intellect
        self.dot_duration = dot_duration
        self.hit_interval = hit_interval / (1+haste_percent)
        self.insanity_gen_per_hit = insanity_gen / self.hit_interval


class Timeline:
    now = 0
    vampiric_touch_hit = float('inf')
    vampiric_touch_end = 0
    shadowfiend_hit = float('inf')
    shadowfiend_end = 0
    shadowfiend_off_cd = 0
    void_eruption_hit = float('inf')
    void_eruption_off_cd = 0
    void_bolt_hit = float('inf')
    void_bolt_off_cd = 0
    devouring_plague_dd_hit = float('inf')
    devouring_plague_dot_hit = float('inf')
    devouring_plague_end = 0
    sw_pain_dd_hit = float('inf')
    sw_pain_dot_hit = float('inf')
    sw_pain_end = 0
    mind_blast_hit = 0
    mind_blast_off_cd = 0
    mind_flay_hit = float('inf')
    mind_flay_end = 0
    sw_death_hit = float('inf')
    sw_death_off_cd = 0
    vampiric_embrace_end = 0
    vampiric_embrace_off_cd = 0


intellect = 350
crit_rating = 155
haste_rating = 174
mastery_rating = 72
versatility_rating = 49

crit_chance = crit_rating*0.1415/155
haste_percent = haste_rating*0.1729/174
mastery_percent = mastery_rating*0.0337/72
versatility_percent = versatility_rating*0.0402/49

void_eruption = Spells(1.3, 1.5, 90, 4, 0)
void_bolt = Spells(0.815, 0, 4.5, 15, 0)
devouring_plague_dd = Spells(0.85, 0, 0, 0, 50)
pain_dd = Spells(0.154, 0, 0, 0, 0)
mind_blast = Spells(0.98, 1.5, 7.5, 8, 0)
sw_death = Spells(0.9, 0, 20, 0, 0)

timeline = Timeline
insanity = 0

print(timeline.shadowfiend_end)
print(mind_blast.cast_time)
print(f'Haste %: {haste_percent}')
print(f'Crit chance: {crit_chance}')
print(f'Mastery %: {mastery_percent}')
print(f'Versatility %: {versatility_percent}')

