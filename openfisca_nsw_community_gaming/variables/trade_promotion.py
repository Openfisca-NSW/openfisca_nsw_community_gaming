# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


# This is used to calculate whether an organisation is permitted to conduct a trade promotion gaming activity
class trade_promotion__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a trade promotion are being met by the organisation"
    reference = "Part 2 (14) of Community Gaming Regulation 2020"

    def formula(organisation, period, parameters):
        return (
            organisation('gaming_activity_is_trade_promotion', period) * organisation('no_fee_charged_for_conducting_game', period)
            * organisation('gaming_activity_has_business_consent', period))


class trade_promotion__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "If the trade promotion is a permitted gaming activity, is an authority required to conduct it?"

    def formula(organisation, period, parameters):
        return (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) > parameters(period).permitted_games.trade_promotion.max_total)


class gaming_activity_has_business_consent(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Has written consent been obtained from a person who is authorised by the business benefiting from the gaming activity?"
