# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType
from openfisca_nsw_community_gaming.variables.gaming_activity_type import GamingActivityType as GT
from openfisca_nsw_community_gaming.variables.community_gaming_regulation_reference import community_gaming_reg as CGR


class sweep_or_calcutta(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether an gaming activity is permitted, permitted_games"
    reference = CGR["2", "13"].json()

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class sweep_or_calcutta__gaming_activity_type(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Is it a sweep or calcutta?"
    reference = CGR["2", "13"].json()

    def formula(organisation, period, parameters):
        gt = organisation('gaming_activity_type', period)
        GT = gt.possible_values
        return gt == GT.sweep_or_calcutta


class sweep_or_calcutta__fund_raising_game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = """Sweep or calcutta meets conditions for being organised by a fund
            raising organisation"""
    reference = CGR["2", "13"].json()

    def formula(organisation, period, parameters):
        return(
            organisation('is_approved_fund_raising_organisation', period)
            and organisation('sweep_or_calcutta__reasonable_amount_to_benefiting_org', period)
            and organisation('sweep_or_calcutta__amount_paid_will_be_at_least_what_agreed_to', period)
            and organisation('sweep_or_calcutta__amount_agreed_in_writing_beforehand', period))


class sweep_or_calcutta__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "The eligibility conditions for organising a sweep or calcutta are being met by the organisation"

    def formula(organisation, period, parameters):
        is_sweep_or_calcutta = organisation('gaming_activity_type', period) ==\
            GT.sweep_or_calcutta
        no_payment_except_for_entry = organisation('sweep_or_calcutta__no_payment_for_right_to_participate', period)
        return (
            is_sweep_or_calcutta
            and no_payment_except_for_entry
            and (organisation('sweep_or_calcutta__fund_raising_game_meets_criteria', period)
                or organisation('sweep_or_calcutta__social_game_meets_criteria', period)))


class sweep_or_calcutta__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Is Authority required to run the sweep or calcutta?"
    reference = CGR["2", "13"].json()

    def formula(organisation, period, parameters):
        return (
            (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period)
            > parameters(period).permitted_games.sweep_or_calcutta.total_prize_threshold))


class sweep_or_calcutta__social_game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "If the sweep or calcutta is a permitted gaming activity, "\
        "is an authority required to conduct it?"
    reference = CGR["2", "13"].json()

    def formula(organisation, period, parameters):
        return(
            organisation('sweep_or_calcutta__is_social_game', period)
            and organisation('sweep_or_calcutta__all_gross_proceeds_are_distributed_to_participants_based_on_stake_held', period)
            )


class sweep_or_calcutta__is_social_game(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Is the gaming activity being conducted for social purposes?"
    reference = CGR["2", "13"].json()


class sweep_or_calcutta__all_gross_proceeds_are_distributed_to_participants_based_on_stake_held(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Will all the gross proceeds of the gaming activity be distributed to participants based on stake held?"
    reference = CGR["2", "13"].json()


class sweep_or_calcutta__amount_paid_will_be_at_least_what_agreed_to(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Do you agree to pay at least the amount stipulated in the written agreement?"
    reference = CGR["2", "13"].json()


class sweep_or_calcutta__amount_agreed_in_writing_beforehand(Variable):
    value_type = bool
    entity = Organisation
    definition_period = ETERNITY
    label = "Do you have a written agreement stipulating the minimum amount paid to the charitable organisation?"


class sweep_or_calcutta__gaming_activity_for_social_purpose(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Is the gaming activity being conducted for social purposes?"
    reference = CGR["2", "13"].json()


class sweep_or_calcutta__no_payment_for_right_to_participate(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = """Will there be a benefit or payment payable for a right
        to participate in the gaming activity? (other than stake money
        or the usual fee for entry to the venue)"""
    reference = CGR["2", "13"].json()


class distribution_of_gross_proceeds(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = """If the gaming activity is not conducted wholly or partly for a
        charity, non-profit, political party, trade union, registered club, racing
        club, greyhound racing club or harness racing club, will the gross proceeds
        be distributed to holders of the rights in respect of the succesful
        participants?"""
    reference = CGR["2", "13"].json()


class sweep_or_calcutta__reasonable_amount_to_benefiting_org(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = """Will a resonable amount of the gross proceeds be paid to the
            benefiting organisation (which will be agreed in writing before
            the gaming activity is conducted)?"""
    reference = CGR["2", "13"].json()


class excess_proceeds_to_benefiting_org(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = """Will the amount of proceeds remaining after payment of prize money
        and the costs and expenses of the gaming activity be paid for the purposes
        of the organisation, even if that amount exceeds the agreed amount of the
        gross proceeds?"""
    reference = CGR["2", "13"].json()
