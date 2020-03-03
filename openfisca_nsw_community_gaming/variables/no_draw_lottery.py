# -*- coding: utf-8 -*-

# This file defines the formula for calculating whether an organisation meets the conditions
# for conducting a no-draw-lottery as stipulated in the Community Gaming Regulation 2019

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This is used to calculate whether an organisation is fulfilling the conditions for organising a no-draw lottery
class no_draw_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a no-draw lottery are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_charity', period) + organisation('is_not_for_profit', period))
            * (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) <= parameters(period).permitted_games.no_draw_lottery.max_total_value_of_all_prizes)
            * (organisation('proceeds_to_benefitting_organisation', period) >= (organisation('gross_proceeds_from_gaming_activity', period) * parameters(period).permitted_games.no_draw_lottery.min_gross_proceeds_percent_to_benefit_org))
            * (organisation('number_of_tickets', period) <= parameters(period).permitted_games.no_draw_lottery.max_number_of_tickets)
            * (organisation('ticket_cost', period) <= parameters(period).permitted_games.no_draw_lottery.max_ticket_cost))
