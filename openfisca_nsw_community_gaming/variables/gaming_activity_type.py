# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType


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


class gaming_activity_result_str(Variable):
    value_type = str
    entity = Organisation
    definition_period = ETERNITY
    label = "Results of calculation FIXME"

    def formula(organisation, period, parameters):
        gaming_type = organisation(
            'gaming_activity_type', period).decode_to_str()[0]
        return organisation(gaming_type, period).decode()[0].value


class gaming_activity_result(Variable):
    value_type = Enum
    possible_values = ReturnType
    entity = Organisation
    default_value = ReturnType.not_permitted
    definition_period = ETERNITY
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = ""

    def formula(organisation, period, parameters):
        rt = organisation('return_type', period)
        RT = rt.possible_values
        gaming_activity = organisation('gaming_activity_type', period).decode_to_str()[0]
        meets_criteria_str = gaming_activity + "__game_meets_criteria"
        needs_auth_str = gaming_activity + "__authority_required"

        meets_criteria = organisation(meets_criteria_str, period)
        needs_authority = organisation(needs_auth_str,
                                    period)
        return select(
            [(meets_criteria * needs_authority),
            (meets_criteria * not_(needs_authority)),
            not_(meets_criteria)],
            [RT.permitted_with_authority,
            RT.permitted,
            RT.not_permitted])


class gaming_activity_is_charity_housie(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Charity Housie"


class gaming_activity_is_social_housie(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Social Housie"


class gaming_activity_is_club_bingo(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Club Bingo"


class gaming_activity_is_draw_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Draw Lottery"


class gaming_activity_is_no_draw_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "No Draw Lottery"


class gaming_activity_is_mini_numbers_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Mini numbers lottery"


class gaming_activity_is_progressive_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Progressive Lottery"


class gaming_activity_is_free_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Free Lottery"


class gaming_activity_is_promotional_raffle(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Promotional Raffle"


class gaming_activity_is_sweep(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Sweep"


class gaming_activity_is_calcutta(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Calcutta"


class gaming_activity_is_other(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Other Gaming Activity"


class gaming_activity_is_free_to_enter(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Whether gaming activity is free for participants to enter"


class gaming_activity_solely_for_social_purposes(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Whether organisation is conducting this gaming activity solely for social purposes?"


class gaming_activity_other_for_charitable_purposes(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Whether organisation is conducting other gaming activity for charitable purposes?"


class gaming_activity_solely_or_partly_for_fundraising(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Whether organisation is conducting this gaming activity solely for entertainment purposes? (Totally non-charitable purposes)"
