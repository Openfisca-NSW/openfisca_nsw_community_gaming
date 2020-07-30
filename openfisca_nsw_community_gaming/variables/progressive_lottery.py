# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR


# The code below is used to calcluate whether an organisation meets the
# conditions for conducting a progressive lottery
class progressive_lottery(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = CGR["2", "9"].json()

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class progressive_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a progessive lottery are\
    being met by the organisation"
    reference = CGR["2", "9"].json()

    def formula(organisation, period, parameters):
        is_progressive_lottery = organisation('gaming_activity_type', period) ==\
            GT.progressive_lottery
        return (
            (is_progressive_lottery
            and (organisation('money_paid_as_prize', period)
            <= parameters(period).permitted_games.progressive_lottery.
            max_value_of_monetary_prize)))


class progressive_lottery__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the progressive lottery is a permitted gaming activity, is an authority required to conduct it?"

    def formula(organisation, period, parameters):
        return (
            (organisation
            ('total_prize_value_of_all_prizes_from_gaming_activity', period)
            > parameters(period).permitted_games.progressive_lottery.
                total_prize_value_threshold))
