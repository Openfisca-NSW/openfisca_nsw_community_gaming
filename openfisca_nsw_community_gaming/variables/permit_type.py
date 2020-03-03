# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class has_authority(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Does the person conducting the gaming activity hold authority to do so that is in force and the activity is conducted in accordance with the authority?"
