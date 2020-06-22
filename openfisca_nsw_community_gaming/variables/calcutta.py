# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


# This is used to calculate whether an organisation is eligible to conduct
# a calcutta
class calcutta__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a calcutta\
    are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            organisation('gaming_activity_is_calcutta', period)
            * (organisation('is_approved_fund_raising_organisation', period)
            + (organisation('distribution_of_gross_proceeds', period)
            * organisation('gaming_activity_for_social_purpose', period)))
            * organisation('no_payment_for_right_to_participate', period)
            * organisation('reasonable_amount_to_benefitting_org', period)
            * organisation('excess_proceeds_to_benefitting_org', period))


# This variable is only needed when the calcutta is a permitted gaming
# activity and is used to calculate whether an authority is required to conduct
# the calcutta
class calcutta__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "If the calcutta is a permitted gaming activity, is an\
    authority required to conduct it?"

    def formula(organisation, period, parameters):
        return (
            (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) > parameters(period).permitted_games.calcutta.total_prize_threshold))
