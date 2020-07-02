# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
from openfisca_nsw_community_gaming.variables.return_type import ReturnType


# This is used to calculate whether an organisation is eligible to conduct a sweep
class sweep(Variable):
    value_type = Enum
    entity = Organisation
    definition_period = ETERNITY
    default_value = ReturnType.not_permitted
    possible_values = ReturnType
    label = "Whether the Sweep is a permitted gaming activity?"
    reference = ""

    def formula(organisation, period, parameters):
        return organisation('gaming_activity_result', period)


class sweep__authority_required(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "If the calcutta is a permitted gaming activity, "\
        "is an authority required to conduct it?"

    def formula(organisation, period, parameters):
        return organisation('sc__authority_required', period)


class sweep__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "If the sweep is a permitted gaming activity, "\
        "is an authority required to conduct it?"
