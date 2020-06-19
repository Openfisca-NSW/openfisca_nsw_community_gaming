# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class gross_proceeds_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"What are the gross proceeds from the gaming activity?"
    definition_period = MONTH
    reference = "4(a)"


class proceeds_to_benefitting_organisation(Variable):
    value_type = int
    entity = Organisation
    label = u"What proceeds would the benefitting organisation receive?"
    definition_period = MONTH
    reference = "4(a)"


class proceeds_used_for_meeting_cost_of_prizes(Variable):
    value_type = int
    entity = Organisation
    label = u"What amount of proceeds would be used to meet the cost of the prizes in the gaming activity or other similar gaming activities?"
    definition_period = MONTH
    reference = "11(c)"


class total_expenses_for_conducting_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"What would be the total value of the expenses for conducting the gaming activity?"
    definition_period = MONTH
    reference = "2(c)"


class net_proceeds_returned_to_participants(Variable):
    value_type = bool
    entity = Organisation
    label = "Would the total amount invested by participants in a session of the gaming activity (after the cost of prizes and expenses of conducting the session are deducted), be returned to participants"
    definition_period = MONTH
    reference = "3(e)"


class money_payable_as_separate_prize(Variable):
    value_type = int
    entity = Organisation
    definition_period = MONTH
    label = "What would be the amount of money payable as a separate prize? (in addition to other prizes of the gaming activity)"


class total_prize_value_of_all_prizes_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"What is the total prize value of all the prizes in the gaming activity?"
    definition_period = MONTH
    reference = 'Part 2 - 14 (2)(c) of the Community Gaming Regulation 2020'


class highest_value_of_individual_prize_in_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"What would be the highest value of an individual prize in the gaming activity?"
    definition_period = MONTH


class value_of_jackpot_prize(Variable):
    value_type = int
    entity = Organisation
    label = u"Highest value of jackpot prize in gaming activity"
    definition_period = MONTH


class value_of_bonus_prize(Variable):
    value_type = int
    entity = Organisation
    label = u"Total value of bonus prize in gaming activity"
    definition_period = MONTH


class value_of_individual_prize(Variable):
    value_type = int
    entity = Organisation
    label = u"Value of individual prize in gaming activity"
    definition_period = MONTH


class no_fee_charged_for_conducting_game(Variable):
    value_type = bool
    entity = Organisation
    label = "Other than a prize, is there any salary, wage, fee, commission, percentage or other benefit given or paid to or taken by a person in connection with the conduct of the gaming activity?"
    definition_period = MONTH
    reference = "Part 2 (14)(a) of Community Gaming Regulationm 2020"


class participation_is_free(Variable):
    value_type = bool
    entity = Organisation
    label = "Whether it is free to participate in the gaming activity?"
    definition_period = MONTH


class total_prize_value_from_single_gaming_session(Variable):
    value_type = int
    entity = Organisation
    label = u"Total prize value of all the prizes for 1 session of the gaming activity"
    definition_period = MONTH


class no_prize_consists_of_money(Variable):
    value_type = bool
    entity = Organisation
    label = u"None of the prizes consist of or include money"
    definition_period = MONTH
