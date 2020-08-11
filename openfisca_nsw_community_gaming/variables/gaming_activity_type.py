# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR


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
    sweep_or_calcutta = u'Sweep or Calcutta'
    other_gaming_activity = u'Other Gaming Activity'


class DurationOfAuthority(Enum):
    one_year = u'One Year'
    three_years = u'Three Years'
    five_years = u'Five Years'


# The duration of authority can be 1, 3 or 5 years
class duration_of_authority(Variable):
    value_type = Enum
    possible_values = DurationOfAuthority
    default_value = DurationOfAuthority.one_year
    entity = Organisation
    definition_period = MONTH
    label = "The number of years for which the applicant has applied for authority (Can be 1, 3 or 5 years)"
    reference = "XXX FIXME"


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


class gaming_activity_authority_fee_str(Variable):
    value_type = str
    entity = Organisation
    definition_period = ETERNITY
    label = "Fee for gaming activity"

    def formula(organisation, period, parameters):
        rt = organisation('return_type', period)
        RT = rt.possible_values
        DA = DurationOfAuthority
        if organisation('gaming_activity_result', period) != RT.permitted_with_authority:
            return ""
        fee_unit = parameters(period).permitted_games.permits.fee_unit

        one_year_processing = parameters(period).permitted_games\
            .permits.authority_fee[DA.one_year._name_].processing_component
        one_year_fixed = parameters(period).permitted_games\
            .permits.authority_fee[DA.one_year._name_].fixed_component
        total1 = fee_unit * (one_year_fixed + one_year_processing)

        three_year_processing = parameters(period).permitted_games\
            .permits.authority_fee[DA.three_years._name_].processing_component
        three_year_fixed = parameters(period).permitted_games\
            .permits.authority_fee[DA.three_years._name_].fixed_component
        total3 = fee_unit * (three_year_fixed + three_year_processing)

        five_year_processing = parameters(period).permitted_games\
            .permits.authority_fee[DA.five_years._name_].processing_component
        five_year_fixed = parameters(period).permitted_games\
            .permits.authority_fee[DA.five_years._name_].fixed_component
        total5 = fee_unit * (five_year_fixed + five_year_processing)

        result_str = "The cost of obtaining an Authority for one year is ${0}, for three years is ${1} and for five years is ${2}."
        return result_str.format(total1, total3, total5)


class gaming_activity_is_free_to_enter(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Whether gaming activity is free for participants to enter"


class gaming_activity_solely_for_social_purposes(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Is the gaming activity being operated only for social purposes?"


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


class gaming_activity_on_authority_of_reg_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Is the gaming activity conducted by or on the authority of a registered club?"


class gaming_activity_organised_for_patronage(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Will the gaming activity be conducted for the purpose of attracting patronage to the club's facilities?"
    reference = CGR["2", "11"].json()
