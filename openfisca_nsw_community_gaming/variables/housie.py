# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.organisation_type import OrganisationType as OT
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR


# The code below is used to calculate whether an organisation is meeting the
# conditions for conducting a housie. A housie or bingo means a gaming
# activity— (a) that is played by 1 or more participants using cards or a
# device with numbered spaces or symbols, and (b) during which numbered spaces
# or symbols identified randomly and announced are marked off by each
# participant who has a card or device on which the numbered space or symbol is
# displayed, and (c) that is won by the participant who is first able to mark
# off all numbered spaces or symbols on the card or device that are required to
# be marked off for a win.or symbols on the card or device that are required to
# be marked off on a win

class charity_housie(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = CGR["2", "5"].json()

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class charity_housie__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "The eligibility conditions for organising a charity housie are being met by the organisation"
    reference = CGR["2", "5"].json()

    def formula(organisation, period, parameters):
        gross_proceeds = organisation('gross_proceeds_from_gaming_activity', period)
        total_prize = organisation('total_prize_value_from_single_gaming_session', period)
        is_charity = organisation('organisation_type', period) ==\
            OT.charitable_organisation
        is_charity_housie = organisation('gaming_activity_type', period) ==\
            GT.charity_housie

        return (
            is_charity and is_charity_housie
            and (organisation('proceeds_to_benefiting_organisation', period)
                >= parameters(period).permitted_games.housie.min_gross_proceeds_to_benefit_org
                * gross_proceeds)
            and (organisation('total_expenses_for_conducting_gaming_activity', period)
                <= parameters(period).permitted_games.
                housie.max_expenses.charity_housie
                * gross_proceeds)
            and (total_prize <= parameters(period).permitted_games.
                housie.max_value_of_prize_per_session.charity_housie)
            and (total_prize
                <= parameters(period).permitted_games.
                housie.max_value_of_prizes_per_gross_proceeds
                * gross_proceeds)
            and (organisation('number_of_tickets', period)
                <= parameters(period).permitted_games.housie.max_no_of_tickets))


class charity_housie__authority_required(Variable):
    """
    Authority is never required for charity housie.
    """
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    default_value = False
    label = "If the charity housie is a permitted gaming activity, is an authority required to conduct it?"


class social_housie(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = CGR["2", "5"].json()

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


# This formula is used to calculate whether an organisation meets criteria for conducting a social housie
class social_housie__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Are the eligibility conditions for organising social housie being met by the organisation"
    reference = CGR["2", "5"].json()

    def formula(organisation, period, parameters):
        is_social_housie = organisation('gaming_activity_type', period) ==\
            GT.social_housie
        return (
            is_social_housie
            and organisation('gaming_activity_solely_for_social_purposes', period)
            and not_(organisation('venue_is_licensed_premises', period))
            and organisation('net_proceeds_returned_to_participants', period)
            and (organisation('value_of_jackpot_prize', period)
                <= parameters(period).permitted_games.housie.max_value_of_jackpot_prize)
            and (organisation('total_prize_value_from_single_gaming_session', period)
                <= parameters(period).permitted_games.
                housie.max_value_of_prize_per_session.social_housie))


class social_housie__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    default_value = False
    label = "If the social housie is a permitted gaming activity,"\
        "is an authority required to conduct it?"


class club_bingo(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = CGR["2", "5"].json()

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class club_bingo__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "The eligibility conditions for organising a club bingo are being met by the organisation"
    reference = CGR["2", "5"].json()

    def formula(organisation, period, parameters):
        is_club_bingo = organisation('gaming_activity_type', period) ==\
            GT.club_bingo
        return (
            is_club_bingo
            and (organisation('total_prize_value_from_single_gaming_session', period)
               <= parameters(period).permitted_games.housie.
               max_value_of_prize_per_session.club_bingo)
            and (organisation('value_of_bonus_prize', period)
               <= parameters(period).permitted_games.housie.
               max_bonus_prize)
            and organisation('no_prize_consists_of_money', period)
            and organisation('gaming_activity_organised_for_patronage', period)
            and organisation('venue_is_registered_club', period)
            and organisation('gaming_activity_on_authority_of_reg_club', period))


class club_bingo__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    default_value = False
    label = "If the club bingo is a permitted gaming activity, is an authority required to conduct it?"
    reference = CGR["2", "5"].json()
