# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *

# This is used to calculate whether an organisation is eligible to conduct other gaming activity for charitable purposes


class other_gaming_activity__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising other gaming activities for charitable purposes are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('gaming_activity_clause', period) + ((organisation('proceeds_to_benefitting_organisation', period) >= (organisation('gross_proceeds_from_gaming_activity', period) * parameters(period).permitted_games.other_gaming_activity.min_gross_proceeds_percent_to_benefit_org)) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.other_gaming_activity.max_value_of_prize_per_session) * organisation('gaming_activity_other_for_charitable_purposes', period))))


class gaming_activity_clause(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether this gaming activity is an art union gaming activity, housie, lottery, sweep or calcutta?"


class other_gaming_activity__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the other gaming activity is a permitted gaming activity, is an authority required to conduct it?"
