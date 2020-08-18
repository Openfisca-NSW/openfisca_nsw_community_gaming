# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR


class gross_proceeds_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"What are the gross proceeds from the gaming activity?"
    definition_period = MONTH


class proceeds_to_benefiting_organisation(Variable):
    value_type = int
    entity = Organisation
    label = u"How much of the estimated gross proceeds will the benefiting organisation receive?"
    definition_period = MONTH


class proceeds_used_for_meeting_cost_of_prizes(Variable):
    value_type = int
    entity = Organisation
    label = u"What amount of proceeds would be used to meet the cost of the prizes in the gaming activity or other similar gaming activities?"
    definition_period = MONTH
    reference = CGR["2", "11"].json()


class total_expenses_for_conducting_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"What would be the total value of expenses to conduct this gaming activity?"
    definition_period = MONTH


class net_proceeds_returned_to_participants(Variable):
    value_type = bool
    entity = Organisation
    label = "Would the total amount invested by participants be returned to participants? (after the cost of prizes and expenses in conducting the session are deducted)"
    definition_period = MONTH
    reference = CGR["2", "5"].json()


class money_payable_as_separate_prize(Variable):
    value_type = int
    entity = Organisation
    definition_period = MONTH
    label = "What would be the amount of money payable as a prize? (excluding the value of any other prizes in the same gaming activity)"
    reference = CGR["2", "4"].json()


class total_prize_value_of_all_prizes_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"What is the total prize value of prizes?"
    definition_period = MONTH


class highest_value_of_individual_prize_in_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"What would be the highest value of an individual prize in the gaming activity?"
    definition_period = MONTH


class value_of_jackpot_prize(Variable):
    value_type = int
    entity = Organisation
    label = u"What will the highest value of the jackpot prize in the gaming activity be?"
    definition_period = MONTH
    reference = CGR["2", "5"].json()


class value_of_bonus_prize(Variable):
    value_type = int
    entity = Organisation
    label = u"If there is a bonus prize in the gaming activity, what will its value be?"
    definition_period = MONTH


class value_of_individual_prize(Variable):
    value_type = int
    entity = Organisation
    label = u"Value of individual prize in gaming activity"
    definition_period = MONTH


class participation_fees(Variable):
    value_type = bool
    entity = Organisation
    label = """Will any entry fee or other fee be charged to participate?
    (other than purchasing goods or services at a normal retail price)"""
    definition_period = MONTH
    reference = CGR["2", "14"].json()


class free_participation(Variable):
    value_type = bool
    entity = Organisation
    label = "Will the gaming activity be free to participate in?"
    definition_period = MONTH
    reference = CGR["2", "10"].json()


class total_prize_value_from_single_gaming_session(Variable):
    value_type = int
    entity = Organisation
    label = u"What will be the total prize value of all prizes per session?"
    definition_period = MONTH


class prize_consists_of_money(Variable):
    value_type = bool
    entity = Organisation
    label = u"Do any of the prizes consist of money?"
    definition_period = MONTH


class money_paid_as_prize(Variable):
    value_type = int
    entity = Organisation
    definition_period = MONTH
    label = "What is maximum amount payable as a prize?"
    reference = CGR["2", "9"].json()


class charitable_purpose(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = '''Will the gaming activity be conducted to raise funds for a charity??'''


class charitable_or_non_profit_purpose(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = '''Will the gaming activity be conducted to raise funds for a charity
        or non-profit organisation?'''
