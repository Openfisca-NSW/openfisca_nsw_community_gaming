# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR
from openfisca_nsw_community_gaming.variables.organisation_type import OrganisationType as OT


class promotional_raffle(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class promotional_raffle__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a promotional raffle are being met by the organisation"
    reference = CGR["2", "11"].json()

    def formula(organisation, period, parameters):
        is_promotional_raffle = organisation('gaming_activity_type', period) ==\
            GT.promotional_raffle
        is_registered_club = organisation('organisation_type', period) ==\
            OT.registered_club
        return (
            is_promotional_raffle and is_registered_club
            and organisation('venue_is_registered_club', period)
            and organisation('gaming_activity_organised_for_patronage', period)
            and (organisation('proceeds_used_for_meeting_cost_of_prizes', period)
                >= parameters(period).permitted_games.promotional_raffle.
                min_gross_proceeds_for_prizes
                * organisation('gross_proceeds_from_gaming_activity', period))
            and (organisation('total_prize_value_from_single_gaming_session', period)
                <= parameters(period).permitted_games.promotional_raffle.
                max_value_of_prize_per_session)
            and organisation('no_prize_consists_of_money', period))


class promotional_raffle__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    default_value = False
    label = "If the promotional raffle is a permitted gaming activity, is an authority required to conduct it?"
    reference = CGR["2", "11"].json()
