# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This is used to calculate whether an organisation is permitted to conduct a guessing games
class draw_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a draw lottery are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_charity', period) + organisation('is_not_for_profit', period))
            * (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) <= parameters(period).permitted_games.draw_lottery.max_total_value_of_all_prizes)
            * (organisation('gaming_activity_is_draw_lottery', period))
            * (organisation('proceeds_to_benefitting_organisation', period)) >= ((organisation('gross_proceeds_from_gaming_activity', period) * parameters(period).permitted_games.draw_lottery.min_gross_proceeds_percent_to_benefit_org)))
