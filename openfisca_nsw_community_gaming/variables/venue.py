# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class venue_is_licensed_premises(Variable):
    value_type = bool
    entity = Organisation
    label = u"Whether the gaming activity will be conducted on licensed premises"
    definition_period = MONTH


class venue_is_registered_club(Variable):
    value_type = bool
    entity = Organisation
    label = u"Whether the gaming activity will be conducted on the premises of the registered club"
    definition_period = MONTH
