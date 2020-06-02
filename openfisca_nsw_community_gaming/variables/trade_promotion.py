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

    def formula(organisation, period, parameters):
        return (
            (organisation('gaming_activity_is_trade_promotion', period) * (organisation('participation_obtained_by_purchasing_goods', period))
            * (organisation('gaming_activity_has_business_principal_consent', period)) * (organisation('total_prize_value_of_all_prizes_from_single_gaming_session', period) <= parameters(period).permitted_games.trade_promotion.max_total_single_session)))


class trade_promotion__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "If the trade promotion is a permitted gaming activity, is an authority required to conduct it?"

    def formula(organisation, period, parameters):
        return (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) > parameters(period).permitted_games.trade_promotion.max_total)


class gaming_activity_has_business_principal_consent(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Has the written consent of a principal in the bnusiness benefitting from the gaming activity been obtained to conduct the gaming activity?"


class participation_obtained_by_purchasing_goods(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Is the right to participate in the gaming activity obtained by purchasing goods or services, with no additional cost or other actions relating to participation?"
