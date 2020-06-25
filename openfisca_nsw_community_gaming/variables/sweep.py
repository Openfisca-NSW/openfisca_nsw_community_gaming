# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT


# This is used to calculate whether an organisation is eligible to conduct a sweep
class sweep(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = ""

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class sweep__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a sweep are being met by the organisation"

    def formula(organisation, period, parameters):
        is_sweep = organisation('gaming_activity_type', period) ==\
            GT.sweep
        return (
            is_sweep
            and (organisation('is_approved_fund_raising_organisation', period)
            or (organisation('distribution_of_gross_proceeds', period)
            and organisation('gaming_activity_for_social_purpose', period)))
            and organisation('no_payment_for_right_to_participate', period)
            and organisation('reasonable_amount_to_benefiting_org', period)
            and organisation('excess_proceeds_to_benefiting_org', period))


class sweep__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "If the sweep or calcutta is a permitted gaming activity, is an authority required to conduct it?"

    def formula(organisation, period, parameters):
        return (
            (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) > parameters(period).permitted_games.sweep.total_prize_threshold))
