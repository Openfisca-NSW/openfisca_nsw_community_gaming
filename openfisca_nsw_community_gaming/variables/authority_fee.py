# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class total_fee_in_dollars(Variable):
    value_type = int
    entity = Organisation
    definition_period = MONTH
    label = "The total fee in dollars for application for authority"

    def formula(organisation, period, parameters):
        return (
            parameters(period).permitted_games.permits.fee_unit * organisation('total_fee_in_units', period))


class total_fee_in_units(Variable):
    value_type = int
    entity = Organisation
    definition_period = MONTH
    label = "The total fee in units for application for authority"

    def formula(organisation, period, parameters):
        return (
            (organisation('fixed_component_fee_in_units', period) + organisation('processing_component_fee_in_units', period)))


class fixed_component_fee_in_units(Variable):
    value_type = int
    entity = Organisation
    definition_period = MONTH
    label = "The fixed component of the authority fee in units based on the number of years the applicant has applied for"

    def formula(organisation, period, parameters):
        duration = organisation('duration_of_authority', period)
        return (
            (parameters(period).permitted_games.permits.authority_fee[duration].fixed_component))


class processing_component_fee_in_units(Variable):
    value_type = int
    entity = Organisation
    definition_period = MONTH
    label = "The processing component of the authority fee based on the number of years the applicant has applied for"

    def formula(organisation, period, parameters):
        duration = organisation('duration_of_authority', period)
        return ((parameters(period).permitted_games.permits.authority_fee[duration].processing_component))


# The duration of authority can be 1, 3 or 5 years
class duration_of_authority(Variable):
    value_type = int
    entity = Organisation
    definition_period = MONTH
    label = "The number of years for which the applicant has applied for authority (Can be 1, 3 or 5 years)"
