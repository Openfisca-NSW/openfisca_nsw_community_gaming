# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR
from openfisca_nsw_community_gaming.variables.organisation_type import OrganisationType as OT


# This is used to calculate whether an organisation is eligible to conduct other gaming activity for charitable purposes


class other_gaming_activity(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = CGR["2", "12"].json()

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class other_gaming_activity__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising other gaming activity\
    (that is not an art union gaming activity, housie, lottery, sweep\
    or calcutta) is being met by the organisation"
    reference = CGR["2", "12"].json()

    def formula(organisation, period, parameters):
        is_other_gaming_activity = organisation('gaming_activity_type', period) ==\
            GT.other_gaming_activity
        is_charity = organisation('organisation_type', period) ==\
            OT.charitable_organisation
        return (
            is_other_gaming_activity and is_charity
            and (organisation('proceeds_to_benefiting_organisation', period)
            >= (organisation('gross_proceeds_from_gaming_activity', period)
            * parameters(period).permitted_games.other_gaming_activity.
                min_gross_proceeds_percent_to_benefit_org))
            and (organisation('total_prize_value_from_single_gaming_session', period)
            <= parameters(period).permitted_games.other_gaming_activity.
            max_value_of_prize_per_session))


class other_gaming_activity__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the other gaming activity is a permitted gaming activity, is an authority required to conduct it?"
    reference = CGR["2", "12"].json()
