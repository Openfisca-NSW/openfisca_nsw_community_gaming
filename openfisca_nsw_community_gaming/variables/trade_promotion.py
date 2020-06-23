# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class trade_promotion(Variable):
    value_type = int
    entity = Organisation
    definition_period = ETERNITY
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = ""

    def formula(organisation, period, parameters):
        rt = organisation('return_type', period)
        RT = rt.possible_values
        meets_criteria = organisation('trade_promotion__game_meets_criteria',
                                      period)
        if not meets_criteria:
            return RT.not_permitted.value
        else:
            auth_required = organisation('trade_promotion__authority_required',
                                         period)
            if auth_required:
                return RT.permitted_with_authority.value
        return RT.permitted.value


class trade_promotion__gaming_activity_type(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Is it an trade promotion gaming activity"
    reference = "Part 2 (14) - Community Gaming Regulation 2020"

    def formula(organisation, period, parameters):
        gt = organisation('gaming_activity_type', period)
        GT = gt.possible_values
        return gt == GT.trade_promotion


# This is used to calculate whether an organisation is permitted to conduct a
# trade promotion gaming activity
class trade_promotion__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a trade promotion are\
    being met by the organisation"
    reference = "Part 2 (14) of Community Gaming Regulation 2020"

    def formula(organisation, period, parameters):
        return (
            organisation('trade_promotion__gaming_activity_type', period)
            * organisation('no_fee_charged_for_conducting_game', period)
            * organisation('gaming_activity_has_business_consent', period))


# This variable is only needed when the trade promotion is a permitted gaming
# activity and is used to calculate whether an authority is required to conduct
# the trade promotion.
class trade_promotion__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Is an authority required for this permitted trade promotion?"

    def formula(organisation, period, parameters):
        return (organisation
        ('total_prize_value_of_all_prizes_from_gaming_activity', period)
            > parameters(period).permitted_games.trade_promotion.max_total)


class gaming_activity_has_business_consent(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Has written consent been obtained from a person who is authorised\
    by the business benefiting from the gaming activity?"
