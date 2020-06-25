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
            and (organisation('is_approved_fund_raising_organisation', period)
            or (organisation('distribution_of_gross_proceeds', period)
            and organisation('gaming_activity_for_social_purpose', period)))
            and organisation('no_payment_for_right_to_participate', period)
            and organisation('reasonable_amount_to_benefiting_org', period)
            and organisation('excess_proceeds_to_benefiting_org', period))


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


"""

        on_behalf_of_fund_raising_org OR for_social_purposes

        and

        no_payment_for_right_to_participate (unless it's an entry fee for venue)

        and

        if prize_value > $30K then authority required

        and if (benefiting_org is fundraising_org) then (reasonable_proceeds_are_paid_to_org and amount_is_agreed_in_writing_beforehand)

        if (benefiting_org is not fundraising_org) then (all_gross_proceeds_are_distributed_to_participants_based_on_stake_held)

        if (benefiting_org is fundraising_org) then net_proceeds may be paid to fundraising_org even_if net_proceeds > agreed_amount

"""
