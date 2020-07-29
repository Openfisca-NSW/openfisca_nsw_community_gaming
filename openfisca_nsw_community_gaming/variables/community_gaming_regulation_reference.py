from openfisca_nsw_community_gaming.variables.regulation_reference import Regulation, PartType as PT
import json

community_gaming_reg = Regulation("Community Gaming Regulation 2020", "1 July 2020",
        "26 June 2020")


part1 = community_gaming_reg.add_part("1", PT.PART, "Preliminary")
part1.add_parts([("1", PT.CLAUSE, "Name of Regulation"),
              ("2", PT.CLAUSE, "Commencement"),
              ("3", PT.CLAUSE, "Definitions")])

part2 = community_gaming_reg.add_part("2", PT.PART, "Permitted gaming activities")
part2.add_parts([
    ("4", PT.CLAUSE, "Art union gaming activities"),
    ("5", PT.CLAUSE, "Housie or bingo"),
    ("6", PT.CLAUSE, "Draw lotteries"),
    ("7", PT.CLAUSE, "No-draw lotteries"),
    ("8", PT.CLAUSE, "Mini-numbers lotteries"),
    ("9", PT.CLAUSE, "Progressive lotteries"),
    ("10", PT.CLAUSE, "Free lotteries"),
    ("11", PT.CLAUSE, "Promotional raffles conducted by registered clubs"),
    ("12", PT.CLAUSE, "Other gaming activities for charitable purposes"),
    ("13", PT.CLAUSE, "Sweeps and calcuttas"),
    ("14", PT.CLAUSE, "Trade promotion gaming activities")])


def cg_json_str(reference):
    community_gaming_dict = community_gaming_reg.parts
    refs_json = str(reference)
    clause = json.loads(refs_json)
    ret = {"rule": community_gaming_dict,
           "clause": clause
           }
    return json.dumps(ret, indent=4, sort_keys=True, default=str)


print(community_gaming_reg["2", "10"].json())

# print(community_gaming_reg)
# print(community_gaming_reg["2"])
# print(community_gaming_reg["2"]["10"])
