# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *

# This is used to calculate whether an organisation is eligible to conduct a progressive lottery


class progressive_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising progessive lotteries are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('value_of_individual_prize', period) <= parameters(period).permitted_games.progressive_lottery.max_value_of_individual_prize)
            * organisation('condition_for_exceeding_total_prize_value', period))


class condition_for_exceeding_total_prize_value(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Does the person conducting the gaming activity hold an authority that is in force if they are exceeding the total value threshold of all the prizes?"

    def formula(organisation, period, parameters):
        return select(
            [(organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) > parameters(period).permitted_games.progressive_lottery.total_prize_value_threshold), (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) <= parameters(period).permitted_games.progressive_lottery.total_prize_value_threshold)], [organisation('has_authority', period), True])
