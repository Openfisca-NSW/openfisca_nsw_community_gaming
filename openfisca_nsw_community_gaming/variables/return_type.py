# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class ReturnType(Enum):
    permitted = 0
    permitted_with_authority = 1
    not_permitted = 2


class return_type(Variable):
    value_type = Enum
    possible_values = ReturnType
    default_value = ReturnType.not_permitted
    entity = Organisation
    definition_period = ETERNITY
    label = u""
    reference = 'Community Gaming Regulation 2020 Part 2'
