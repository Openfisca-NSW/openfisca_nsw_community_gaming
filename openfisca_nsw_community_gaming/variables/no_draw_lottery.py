# -*- coding: utf-8 -*-

# This file defines the formula for calculating whether an organisation meets the conditions
# for conducting a no-draw-lottery as stipulated in the Community Gaming Regulation 2019

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.organisation_type import OrganisationType as OT
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR

# This is used to calculate whether an organisation is fulfilling the conditions
# for organising a no-draw lottery


class no_draw_lottery(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = CGR["2", "7"].json()

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class no_draw_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a no-draw lottery are being met by the organisation"
    reference = CGR["2", "7"].json()

    def formula(organisation, period, parameters):
        is_charity = organisation('organisation_type', period) ==\
            OT.charitable_organisation
        is_non_profit = organisation('organisation_type', period) ==\
            OT.non_profit_organisation
        is_no_draw_lottery = organisation('gaming_activity_type', period) ==\
            GT.no_draw_lottery
        return (
            (is_charity or is_non_profit)
            and is_no_draw_lottery
            and (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period)
                <= parameters(period).permitted_games.no_draw_lottery.
                max_total_value_of_all_prizes)
            and (organisation('proceeds_to_benefiting_organisation', period)
                >= (organisation('gross_proceeds_from_gaming_activity', period)
                * parameters(period).permitted_games.no_draw_lottery.
                min_gross_proceeds_percent_to_benefit_org))
            and (organisation('number_of_tickets', period)
                <= parameters(period).permitted_games.no_draw_lottery.
                max_number_of_tickets))


class no_draw_lottery__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the no draw lottery is a permitted gaming activity, is an authority required to conduct it?"
    reference = CGR["2", "7"].json()
