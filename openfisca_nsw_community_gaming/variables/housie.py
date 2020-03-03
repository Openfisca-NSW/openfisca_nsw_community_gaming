# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *

# The code below is used to calculate whether an organisation is meeting the conditions for conducting a housie. A housie or bingo is defined in the Community Gaming Regulation 2020 as:
# a) that is played by 1 or more participants using cards or a device with numbered spaces or symbols
# b) during which numbered spaces or symbols identified randomly and announced are marked off by each participant who has a card or device on which the space or symbol is displayed
# c) that is won by the participant who is first able to mark off all spaces or symbols on the card or device that are required to be marked off on a win

# This formula is used to calculate whether an organisation meets criteria for conducting a social housie


class charity_housie__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a charity housie are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_charity', period) * ((organisation('proceeds_to_benefitting_organisation', period) >= parameters(period).permitted_games.housie.min_gross_proceeds_to_benefit_org) * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('total_expenses_for_conducting_gaming_activity', period) <= parameters(period).permitted_games.housie.max_expenses.charity_housie * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.housie.max_value_of_prize_per_session.charity_housie) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.housie.max_value_of_prizes_per_gross_proceeds * organisation('gross_proceeds_from_gaming_activity', period)) * not_(organisation('more_than_ten_tickets_sold_to_same_player', period)) * organisation('ticket_cost', period) <= parameters(period).permitted_games.housie.max_ticket_cost.charity_housie) * organisation('is_another_gaming_activity_happening', period))


# This is used to calculate whether the condition is being met for organising another gaming activity while one session of the charity housie is being conducted
class condition_for_multiple_gaming_activities(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Are eligibility conditions being met for organising another gaming activity while one session of a charity housie is being conducted?"

    def formula(organisation, period, parameters):
        return select(
            [organisation('is_another_gaming_activity_happening', period), not_(organisation('is_another_gaming_activity_happening', period))],
            [(organisation('total_prize_value_from_single_gaming_session') <= parameters(period).permitted_games.housie.max_value_of_prize_per_session.charity_housie), True])


# This formula is used to calculate whether an organisation meets criteria for conducting a social housie
class social_housie__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a social housie are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            ((organisation('gaming_activity_solely_for_social_purposes', period)) * (organisation('ticket_cost', period) <= parameters(period).permitted_games.housie.max_ticket_cost.social_housie) * (organisation('net_proceeds_returned_to_participants', period) * (organisation('condition_for_no_individual_prize', period)))))


# This formula is used to calculate whether the conditions about individual and jackpot prizes are being met when conducting a social housie
class condition_for_no_individual_prize(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Are the conditions being met for: If there are no individual prize, the value of a jackpot prize does not exceed $200, but if there is an individual prize, then total available prizes for 1 session of the gaming activity does not exceed $40"

    def formula(organisation, period, parameters):
        return select(
            [organisation('no_individual_prize', period), not_(organisation('no_individual_prize', period))],
            [(organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).
            permitted_games.housie.max_value_of_prize_per_session.social_housie), (organisation('value_of_jackpot_prize', period) <= parameters(period).
            permitted_games.housie.max_value_of_jackpot_prize)])


# This formula is used to calculate whether an organisation meets criteria for conducting a club bingo
class club_bingo__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a club bingo are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_registered_club', period) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.housie.max_value_of_prize_per_session.club_bingo) * (organisation('value_of_bonus_prize', period) <= parameters(period).permitted_games.housie.max_bonus_prize) * organisation('no_prize_consists_of_money', period) * organisation('ticket_cost', period) <= parameters(period).permitted_games.housie.max_ticket_cost.club_bingo))
