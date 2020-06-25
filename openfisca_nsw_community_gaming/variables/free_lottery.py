# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT


# This is used to calculate whether an organisation is eligible to
# conduct a free lottery
class free_lottery(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = ""

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class free_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a free lottery are being met by the organisation"

    def formula(organisation, period, parameters):
        is_free_lottery = organisation('gaming_activity_type', period) ==\
            GT.free_lottery
        return (
            is_free_lottery
            and (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period)
            <= parameters(period).permitted_games.free_lottery.
                max_total_prize_value)
            and organisation('participation_is_free', period)
            and organisation('no_prize_consists_of_money', period))


class free_lottery__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the free lottery is a permitted gaming activity, is an authority required to conduct it?"
