# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class ticket_cost(Variable):
    value_type = float
    entity = Organisation
    label = u"Cost of each ticket for participating in the gaming activity"
    definition_period = MONTH


class number_of_tickets(Variable):
    value_type = int
    entity = Organisation
    label = u"Total number of tickets produced for the specific gaming activity"
    definition_period = MONTH


class more_than_ten_tickets_sold_to_same_player(Variable):
    value_type = bool
    entity = Organisation
    label = u"Whether more than 10 tickets have been sold to the same player for the gaming activity?"
    definition_period = MONTH
