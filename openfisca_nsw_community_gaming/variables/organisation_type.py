# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class OrganisationType(Enum):
    charitable_organisation = u'Charitable Organisation'
    non_profit_organisation = u'Non Profit Organisation'
    art_union = u'Art Union'
    registered_club = u'Registered Club'
    political_party = u'Political Party'
    trade_union = u'Trade Union'
    racing_club = u'Club registered under the Rules of Racing of Racing NSW'
    greyhound_racing_club = u'Greyhound racing club within the meaning'\
        'of the Greyhound Racing Act 2017'
    harness_racing_club = u'Harness racing club within the meaning'\
        'of the Harness Racing Act 2009'


class organisation_type(Variable):
    value_type = Enum
    possible_values = OrganisationType
    default_value = OrganisationType.harness_racing_club
    definition_period = ETERNITY
    entity = Organisation
    label = u"What type of Organisation is running the Gaming Activity?"
    reference = 'XXX'


class is_charity(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Gaming activity is conducted by or on behalf of a charitable organisation"


class is_not_for_profit(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Gaming activity is conducted by or on behalf of a non-profit"


class is_art_union(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Gaming activity is conducted by or on behalf of an art union"


class is_registered_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Gaming activity is conducted by or on behalf of a registered club"


class is_political_party(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Gaming activity is conducted by or on behalf of a political party"


class is_trade_union(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Gaming activity is conducted by or on behalf of a trade union"


class is_racing_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Gaming activity is conducted by or on behalf of a club registered under the Rules of Racing of Racing New South Wales"


class is_greyhound_racing_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Gaming activity is conducted by or on behalf of a greyhound racing club within the meaning of the Greyhound Racing Act 2017"


class is_harness_racing_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Gaming activity is conducted by or on behalf of a harness racing club within the meaning of the Harness Racing Act 2009"


class is_approved_fund_raising_organisation(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether the organisation conducting the gaming activity is an approved fund raising organisation as per Part(2) - 13 ?"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_charity', period)
            + organisation('is_not_for_profit', period)
            + organisation('is_political_party', period)
            + organisation('is_trade_union', period)
            + organisation('is_registered_club', period)
            + organisation('is_racing_club', period)
            + organisation('is_greyhound_racing_club', period)
            + organisation('is_harness_racing_club', period)))
