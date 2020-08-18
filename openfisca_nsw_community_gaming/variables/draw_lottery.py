# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR


# This is used to calculate whether an organisation is permitted to conduct
# a draw lottery
class draw_lottery(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = CGR["2", "6"].json()

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class draw_lottery__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a draw lottery\
    are being met by the organisation"
    reference = CGR["2", "6"].json()

    def formula(organisation, period, parameters):
        is_draw_lottery = organisation('gaming_activity_type', period) ==\
            GT.draw_lottery
        gross_proceeds = organisation('gross_proceeds_from_gaming_activity', period)
        return (
            organisation('charitable_or_non_profit_purpose', period)
            and is_draw_lottery
            and (organisation
            ('total_prize_value_of_all_prizes_from_gaming_activity', period)
                <= parameters(period).permitted_games.draw_lottery.
                max_total_value_of_all_prizes)
            and (organisation('proceeds_to_benefiting_organisation', period)
                >= (gross_proceeds
                * parameters(period).permitted_games.draw_lottery.
                min_gross_proceeds_percent_to_benefit_org)))


class draw_lottery__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the draw lottery is a permitted gaming activity, is an\
    authority required to conduct it?"
    reference = CGR["2", "6"].json()
