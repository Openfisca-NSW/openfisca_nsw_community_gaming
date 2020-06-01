# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *

# This is used to calculate whether an organisation is eligible to conduct a progressive lottery


class sweep__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a sweep are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            organisation('is_charity', period)
            * organisation('is_not_for_profit', period)
            * organisation('is_political_party', period)
            * organisation('is_trade_union', period)
            * organisation('is_registered_club', period)
            * organisation('is_racing_club', period)
            * organisation('is_greyhound_racing_club', period)
            * organisation('is_harness_racing_club', period)
            * organisation('distribution_of_gross_proceeds, period')
            * organisation('gaming_activity_for_social_purpose', period)
            * organisation('no_payment_for_right_to_participate', period)
            * organisation('reasonable_amount_to_benefitting_org', period)
            * organisation('distribution_of_gross_proceeds', period)
            * organisation('excess_proceeds_to_benefitting_org', period))


class sweep__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "If the sweep is a permitted gaming activity, is an authority required to conduct it?"

    def formula(organisation, period, parameters):
        return (
            (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) > parameters(period).permitted_games.sweep.total_prize_threshold))


class gaming_activity_for_social_purpose(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Is the gaming activity being conducted for a social purpose?"


class no_payment_for_right_to_participate(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Will there be a benefit or payment payable for a right to participate in the gaming activity? (other than staking money or the usual fee for entry to the venue)"
    reference = "13(1)(b) No payment or benefit is payable for the right to participate in the gaming activity, other than the stake money for the activity. 13(3) Subclause (1)(b) does not apply to the charging of a fee for entry to a venue or function at which a sweep or calcutta is conducted if the fee is not related to the sweep or calcutta and is usually charged for the entry."


class distribution_of_gross_proceeds(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "If the gaming activity is not conducted wholly or partly for a charity, non-profit, political party, trade union, registered club, racing club, greyhound racing club or harness racing club, will the gross proceeds be distributed to holders of the rights in respect of the succesful participants?"
    reference = "If a sweep or calcutta is not conducted wholly or partly for or on behalf of an organisation referred to in subclause (2), the gross proceeds are distributed to the holders of the rights in respect of the successful participants in the event to which the calcutta or sweep relates."


class reasonable_amount_to_benefitting_org(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Will a resonable amount of the gross proceeds be paid to the benefitting organisation (which will be agreed in writing before the gaming activity is conducted)?"
    reference = "If a sweep or calcutta is conducted wholly or partly for or on behalf of an organisation referred to in subclause (2)(a) a reasonable amount of the gross proceeds is paid to the organisation, and (b) the amount is agreed in writing before the sweep or calcutta is conducted."


class excess_proceeds_to_benefitting_org(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Will the amount of proceeds remaining after payment of prize money and the costs and expenses of the gaming activity be paid for the purposes of the organisation, even if that amount exceeds the agreed amount of the gross proceeds?"
    reference = "Despite subclauses (1) and (4), if a sweep or calcutta is conducted wholly or partly for or on behalf of an organisation referred to in subclause (2), the amount of proceeds remaining after payment of prize money and the costs and expenses of the gaming activity may be paid for the purposes of the organisation, even if that amount exceeds the agreed amount of the gross proceeds."
