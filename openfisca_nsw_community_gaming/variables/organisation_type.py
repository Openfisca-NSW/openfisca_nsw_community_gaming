# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class OrganisationType(Enum):
    charity = u'An incorporated or unincorporated body formed for, or to benefit, a benevolent, philanthropic or patriotic purpose.'
    not_for_profit = u'Not for Profit'
    political_party = u'Political Party'
    trade_union = u'Trade Union'
    registered_club = u'Registered Club'
    racing_club = u'Club registered under the Rules of Racing of Racing New South Wales'
    greyhound_racing_club = u'Greyhound racing club within the meaning of the Greyhound Racing Act 2017'
    harness_racing_club = u'Organisation is a harness racing club within the meaning of the Harness Racing Act 2009'
    art_union = u'Art Union'
    business = u'For profit business'


class organisation_type(Variable):
    value_type = Enum
    possible_values = OrganisationType
    default_value = OrganisationType.charity
    entity = Organisation
    definition_period = MONTH
    label = u"Organisation Type"


class is_charity(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Orgnaisation is a charity"


class is_not_for_profit(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a non-profit"


class is_art_union(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is an art union"


class is_registered_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a registered club"


class is_for_profit_business(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a for-profit business"


class is_political_party(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a political party"


class is_trade_union(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a trade union"


class is_racing_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a club registered under the Rules of Racing of Racing New South Wales"


class is_greyhound_racing_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a greyhound racing club within the meaning of the Greyhound Racing Act 2017"


class is_harness_racing_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a harness racing club within the meaning of the Harness Racing Act 2009"
