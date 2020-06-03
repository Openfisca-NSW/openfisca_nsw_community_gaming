# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


# The code below is used to calculate whether an organisation is meeting the conditions for conducting a housie. A housie or bingo means a gaming activity—
# (a) that is played by 1 or more participants using cards or a device with numbered spaces or symbols, and
# (b) during which numbered spaces or symbols identified randomly and announced are marked off by each participant who has a card or device on which the numbered space or symbol is displayed, and
# (c) that is won by the participant who is first able to mark off all numbered spaces or symbols on the card or device that are required to be marked off for a win.or symbols on the card or device that are required to be marked off on a win

# This formula is used to calculate whether an organisation meets criteria for conducting a charity housie
class charity_housie__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a charity housie are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            organisation('is_charity', period) * organisation('gaming_activity_is_charity_housie', period) * (organisation('proceeds_to_benefitting_organisation', period) >= parameters(period).permitted_games.housie.min_gross_proceeds_to_benefit_org * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('total_expenses_for_conducting_gaming_activity', period) <= parameters(period).permitted_games.housie.max_expenses.charity_housie * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.housie.max_value_of_prize_per_session.charity_housie) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.housie.max_value_of_prizes_per_gross_proceeds * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('number_of_tickets', period) <= parameters(period).permitted_games.housie.max_no_of_tickets))


class charity_housie__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the charity housie is a permitted gaming activity, is an authority required to conduct it?"


# This formula is used to calculate whether an organisation meets criteria for conducting a social housie
class social_housie__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a social housie are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            organisation('gaming_activity_is_social_housie', period) * organisation('gaming_activity_solely_for_social_purposes', period) * not_(organisation('venue_is_licensed_premises', period)) * organisation('net_proceeds_returned_to_participants', period) * (organisation('value_of_jackpot_prize', period) <= parameters(period).permitted_games.housie.max_value_of_jackpot_prize) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.housie.max_value_of_prize_per_session.social_housie))


class social_housie__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the social housie is a permitted gaming activity, is an authority required to conduct it?"


# This formula is used to calculate whether an organisation meets criteria for conducting a club bingo
class club_bingo__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a club bingo are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_registered_club', period) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.housie.max_value_of_prize_per_session.club_bingo) * (organisation('value_of_bonus_prize', period) <= parameters(period).permitted_games.housie.max_bonus_prize) * organisation('no_prize_consists_of_money', period)))


class club_bingo__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the club bingo is a permitted gaming activity, is an authority required to conduct it?"
