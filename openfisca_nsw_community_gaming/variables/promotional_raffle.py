# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This is used to calculate whether an organisation is fulfilling the conditions for organising a promotional raffle
class promotional_raffle__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a promotional raffle are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            organisation('is_registered_club', period) * organisation('venue_is_registered_club', period) * organisation('gaming_activity_organised_for_patronage', period) * (organisation('proceeds_used_for_meeting_cost_of_prizes', period) >= parameters(period).permitted_games.promotional_raffle.min_gross_proceeds_for_prizes * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('ticket_cost', period) <= parameters(period).permitted_games.promotional_raffle.max_ticket_cost) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.promotional_raffle.max_value_of_prize_per_session) * organisation('no_prize_consists_of_money', period) * (organisation('gaming_activity_session_duration', period) <= parameters(period).permitted_games.promotional_raffle.max_session_duration) * not_(organisation('prize_paid_between_specific_timings', period)))


class gaming_activity_organised_for_patronage(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The gaming activity will be conducted for the purpose of attracting patronage to the club's facilities"


class gaming_activity_session_duration(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The duration of a session of raffles"


class prize_paid_between_specific_timings(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Will any prize be paid between the hours of 10pm and 8am?"
