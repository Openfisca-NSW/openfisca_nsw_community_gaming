# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class gaming_activity_is_art_union_gaming(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting an art union gaming activity?"


class gaming_activity_is_charity_housie(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a charity housie?"


class gaming_activity_is_social_housie(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a social housie?"


class gaming_activity_is_club_bingo(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a club bingo?"


class gaming_activity_is_draw_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a draw lottery?"


class gaming_activity_is_no_draw_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a no-draw lottery?"


class gaming_activity_is_mini_numbers_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a mini-numbers lottery?"


class gaming_activity_is_progressive_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a progressive lottery?"


class gaming_activity_is_free_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a free lottery?"


class gaming_activity_is_promotional_raffle(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a promotional raffle?"


class gaming_activity_is_trade_promotion(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a trade promotion?"


class gaming_activity_is_sweep_calcutta(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a sweep or calcutta?"


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
