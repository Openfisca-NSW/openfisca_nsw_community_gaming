# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType


class art_union_gaming_activity(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = ""

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class art_union_gaming_activity__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "The eligibility conditions for organising an art union gaming \
    activity are being met by the organisation"
    reference = "Part 2 (4) - Community Gaming Regulation 2020"

    def formula(organisation, period, parameters):

        OT = organisation('organisation_type', period).possible_values
        is_art_union = organisation('organisation_type', period) ==\
            OT.art_union
        GT = organisation('gaming_activity_type', period).possible_values
        is_gaming_activity_type = organisation('gaming_activity_type', period) ==\
            GT.art_union_gaming_activity

        return (
            is_art_union and is_gaming_activity_type
            and (organisation(
                 'total_prize_value_of_all_prizes_from_gaming_activity',
                 period) > parameters(
                 period
                 ).permitted_games.
                 art_union_gaming_activity.
                min_total_value_of_all_prizes)
            and (organisation(
                 'proceeds_to_benefiting_organisation', period)
                 >= ((organisation('gross_proceeds_from_gaming_activity',
                  period)
                * parameters(period).permitted_games.
                art_union_gaming_activity.
                min_gross_proceeds_percent_to_benefit_org)))
            and (organisation(
                 'money_payable_as_separate_prize', period)
                 <= parameters(period).permitted_games.
                 art_union_gaming_activity.max_money_for_separate_prize)
            and organisation('organisation_type', period)) == OT.art_union


class art_union_gaming_activity__authority_required(Variable):
    """
    Authority is required for all art union gaming activities, which
    is why this is always True.
    """

    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    default_value = True
    label = "If the art union gaming activity is a permitted gaming activity,\
    is an authority required to conduct it?"
    reference = "Part 2 (4) - Community Gaming Regulation 2020"
