# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.organisation_type import OrganisationType as OT
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT


class mini_numbers_lottery(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = ""

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


# This formula is used to calculate whether an organisation meets criteria for
# conducting a mini numbers lottery
class mini_numbers_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a mini numbers lottery \
    are being met by the organisation"

    def formula(organisation, period, parameters):
        is_charity = organisation('organisation_type', period) ==\
            OT.charitable_organisation
        is_non_profit = organisation('organisation_type', period) ==\
            OT.non_profit_organisation
        is_mini_numbers_lottery = organisation('gaming_activity_type', period) ==\
            GT.mini_numbers_lottery
        gross_proceeds = organisation('gross_proceeds_from_gaming_activity', period)
        single_session_prize = organisation('total_prize_value_from_single_gaming_session', period)
        return (
            (is_charity or is_non_profit)
            and is_mini_numbers_lottery
            and ((organisation('proceeds_to_benefiting_organisation', period)
                >= parameters(period).permitted_games.mini_numbers_lottery.
                min_gross_proceeds_percent_to_benefit_org) * gross_proceeds)
            and (single_session_prize
                <= parameters(period).permitted_games.mini_numbers_lottery.
                max_value_of_prize_per_session)
            and (single_session_prize
                >= parameters(period).permitted_games.mini_numbers_lottery.
                max_total_prizes_per_gross_proceeds
                * gross_proceeds))


class mini_numbers_lottery__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the mini numbers lottery is a permitted gaming activity, is an authority required to conduct it?"
