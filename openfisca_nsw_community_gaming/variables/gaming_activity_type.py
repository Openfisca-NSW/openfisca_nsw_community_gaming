# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class GamingActivityType(Enum):
    art_union_gaming_activity = u'Art Union Gaming Activity'
    charity_housie = u'Charity Housie'
    social_housie = u'Social Housie'
    club_bingo = u'Club Bingo'
    draw_lottery = u'Draw Lottery'
    no_draw_lottery = u'No Draw Lottery'
    mini_numbers_lottery = u'Mini Numbers Lottery'
    progressive_lottery = u'Progressive Lottery'
    free_lottery = u'Free Lottery'
    promotional_raffle = u'Promotional Raffle'
    trade_promotion = u'Trade Promotion'
    sweep = u'Sweep'
    calcutta = u'Calcutta'
    other_gaming_activity = u'Other Gaming Activity'


class gaming_activity_type(Variable):
    value_type = Enum
    possible_values = GamingActivityType
    default_value = GamingActivityType.other_gaming_activity
    entity = Organisation
    definition_period = ETERNITY
    label = u"What type of gaming activity would be conducted?"
    reference = 'Community Gaming Regulation 2020 Part 2'


class gaming_activity_is_art_union_gaming(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Art Union Gaming Activity"


class gaming_activity_is_charity_housie(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Charity Housie"


class gaming_activity_is_social_housie(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Social Housie"


class gaming_activity_is_club_bingo(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Club Bingo"


class gaming_activity_is_draw_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Draw Lottery"


class gaming_activity_is_no_draw_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "No Draw Lottery"


class gaming_activity_is_mini_numbers_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Mini numbers lottery"


class gaming_activity_is_progressive_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Progressive Lottery"


class gaming_activity_is_free_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Free Lottery"


class gaming_activity_is_promotional_raffle(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Promotional Raffle"


class gaming_activity_is_sweep(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Sweep"


class gaming_activity_is_calcutta(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Calcutta"


class gaming_activity_is_other(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Other Gaming Activity"


class gaming_activity_is_free_to_enter(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether gaming activity is free for participants to enter"


class gaming_activity_solely_for_social_purposes(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting this gaming activity solely for social purposes?"


class gaming_activity_other_for_charitable_purposes(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting other gaming activity for charitable purposes?"


class gaming_activity_solely_or_partly_for_fundraising(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting this gaming activity solely for entertainment purposes? (Totally non-charitable purposes)"
