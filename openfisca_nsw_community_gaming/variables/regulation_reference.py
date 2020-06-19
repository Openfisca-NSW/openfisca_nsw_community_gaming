# class RegulationReference:
#     def __init__(self, version, regulation_name, parts):
#         self.regulation_name = regulation_name
#         self.parts = parts
#         self.version = version
#
#
#     def print_reference(self, part, clause, subclause):
#         print("%s: %s", % (self.regulation_name, self.parts[part].name, self.parts[part][clause].name, self.parts[clause][subclause].name))
#
#
#
# def Part:
#     def __init__(self, identifier, clauses=None):
#         self.identifier = identifier
#         self.name = name
#         self.clauses = clauses
#
#     def __str__(self):
#         print("Part " + self.identifier)
#
#
# def SubClause:
#     def __init__(self, identifier, name, clauses=None):
#         self.identifier = identifier
#         self.clauses = clauses
#
# def print_subclause(subcluase_ids=[]):
#         print("Subclause: " + self.identifier)
#         for subclause in subclause_ids:
#             self.clauses[subclause_id].print_subclause()) + print_sub
