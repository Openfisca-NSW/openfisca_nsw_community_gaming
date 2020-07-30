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
    entity = Organisation
    definition_period = ETERNITY
    label = u"What type of Organisation is running the Gaming Activity?"
    reference = 'XXX'


class is_approved_fund_raising_organisation(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = '''If the sweep or calcutta is a permitted
    gaming activity, is an authority required to conduct it?'''

    def formula(organisation, period, parameters):
        is_charity = organisation('organisation_type', period) ==\
            OrganisationType.charitable_organisation
        is_not_for_profit = organisation('organisation_type', period) ==\
            OrganisationType.non_profit_organisation
        is_political_party = organisation('organisation_type', period) ==\
            OrganisationType.political_party
        is_trade_union = organisation('organisation_type', period) ==\
            OrganisationType.trade_union
        is_registered_club = organisation('organisation_type', period) ==\
            OrganisationType.registered_club
        is_racing_club = organisation('organisation_type', period) ==\
            OrganisationType.racing_club
        is_greyhound_racing_club = organisation('organisation_type', period) ==\
            OrganisationType.greyhound_racing_club
        is_harness_racing_club = organisation('organisation_type', period) ==\
            OrganisationType.harness_racing_club
        return (
            is_charity or is_not_for_profit or is_political_party
            or is_trade_union or is_registered_club or is_racing_club
            or is_greyhound_racing_club or is_harness_racing_club)
