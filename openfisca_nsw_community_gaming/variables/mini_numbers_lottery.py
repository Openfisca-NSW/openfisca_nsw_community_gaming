# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This formula is used to calculate whether an organisation meets criteria for conducting a mini numbers lottery
class mini_numbers_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a mini numbers lottery are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            ((organisation('is_charity', period) + organisation('is_not_for_profit', period)) * organisation('gaming_activity_is_mini_numbers_lottery', period) * ((organisation('proceeds_to_benefitting_organisation', period) >= parameters(period).permitted_games.mini_numbers_lottery.min_gross_proceeds_percent_to_benefit_org) * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.mini_numbers_lottery.max_value_of_prize_per_session) * (organisation('total_prize_value_from_single_gaming_session', period) >= parameters(period).permitted_games.housie.max_value_of_prizes_per_gross_proceeds * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('ticket_cost', period) <= parameters(period).permitted_games.mini_numbers_lottery.max_ticket_cost)))
