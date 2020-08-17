# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR


class trade_promotion__gaming_activity_type(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Is it a trade promotion gaming activity?"
    reference = CGR["2", "14"].json()

    def formula(organisation, period, parameters):
        gt = organisation('gaming_activity_type', period)
        GT = gt.possible_values
        return gt == GT.trade_promotion


# This is used to calculate whether an organisation is permitted to conduct a
# trade promotion gaming activity
class trade_promotion__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "The eligibility conditions for organising a trade promotion are\
    being met by the organisation"
    reference = CGR["2", "14"].json()

    def formula(organisation, period, parameters):
        return (
            organisation('trade_promotion__gaming_activity_type', period)
            * not_(organisation('participation_fees', period))
            * organisation('business_consent',
                period))


# This variable is only needed when the trade promotion is a permitted gaming
# activity and is used to calculate whether an authority is required to conduct
# the trade promotion.
class trade_promotion__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Is an authority required for this permitted trade promotion?"
    reference = CGR["2", "14"].json()

    def formula(organisation, period, parameters):
        return (organisation
        ('total_prize_value_of_all_prizes_from_gaming_activity', period)
            > parameters(period).permitted_games.trade_promotion.max_total)


class business_consent(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Will written consent be obtained from an authorised person?"
    reference = CGR["2", "14"].json()


class trade_promotion(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = CGR["2", "14"].json()

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)
