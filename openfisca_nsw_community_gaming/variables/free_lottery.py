# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *

# This is used to calculate whether an organisation is eligible to conduct a progressive lottery


class free_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a free lottery are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            organisation('gaming_activity_is_free_lottery', period)
            * not_(organisation('gaming_activity_is_trade_promotion', period)) * not_(organisation('gaming_activity_is_progressive_lottery', period)) * (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) <= parameters(period).permitted_games.free_lottery.max_total_prize_value) * organisation('participation_is_free', period) * organisation('no_prize_consists_of_money', period))
