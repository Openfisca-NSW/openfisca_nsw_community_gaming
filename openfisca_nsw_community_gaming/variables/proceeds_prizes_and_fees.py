# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class gross_proceeds_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Gross proceeds from gaming activity"
    definition_period = MONTH


class proceeds_to_benefitting_organisation(Variable):
    value_type = int
    entity = Organisation
    label = u"Proceeds to be given to benefiting organisation"
    definition_period = MONTH


class proceeds_used_for_meeting_cost_of_prizes(Variable):
    value_type = int
    entity = Organisation
    label = u"Proceeds that are used to meet the cost of the prizes in the gaming activity or other similar gaming activities"
    definition_period = MONTH


class total_expenses_for_conducting_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Total value of the expenses of conducting a gaming activity"
    definition_period = MONTH


class net_proceeds_returned_to_participants(Variable):
    value_type = bool
    entity = Organisation
    label = "The total amount invested by participants in a session of the gaming activity, after the cost of prizes and expenses of conducting the session are deducted, is returned to participants"
    definition_period = MONTH


class money_payable_as_separate_prize(Variable):
    value_type = int
    entity = Organisation
    definition_period = MONTH
    label = "The amount of money paid as a separate prize in addition to other prizes of the gaming activity"


class total_prize_value_of_all_prizes_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Total prize value of all prizes in gaming activity"
    definition_period = MONTH


class highest_value_of_individual_prize_in_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Highest value of individual prize in gaming activity"
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
    label = "No salary, wage, fee, commission, percentage or other benefit (other than a prize) is given or paid to or taken by a person in connection with the conduct of the gaming activity."
    definition_period = MONTH


class participation_is_free(Variable):
    value_type = bool
    entity = Organisation
    label = "Whether it is free to participate in the gaming activity?"
    definition_period = MONTH


class is_another_gaming_activity_happening(Variable):
    value_type = bool
    entity = Organisation
    label = "Is another gaming activity being conducted at the same time as a session of the gaming activity?"
    definition_period = MONTH


class total_prize_value_from_single_gaming_session(Variable):
    value_type = int
    entity = Organisation
    label = u"Total prize value of all the prizes for 1 session of the gaming activity"
    definition_period = MONTH


class total_prize_value_of_all_prizes_from_single_gaming_session(Variable):
    value_type = int
    entity = Organisation
    label = u"Total prize value of all prizes from single gaming session"
    definition_period = MONTH


class no_prize_consists_of_money(Variable):
    value_type = int
    entity = Organisation
    label = u"None of the prizes consist of or include money"
    definition_period = MONTH


class no_individual_prize(Variable):
    value_type = int
    entity = Organisation
    label = u"Was there any individual prize that was won as part of the gaming activity?"
    definition_period = MONTH
