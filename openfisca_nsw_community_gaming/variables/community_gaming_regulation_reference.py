from openfisca_nsw_community_gaming.variables.regulation_reference import RegulationReference, Part, PartType as PT
import json

community_gaming_reg = RegulationReference("Community Gaming Regulation 2020", "1 July 2020",
        "26 June 2020")


part1 = Part("1", PT.PART, "Preliminary")
part1.add_parts([Part("1", PT.PART, "Name of Regulation"),
              Part("2", PT.PART, "Commencement"),
              Part("3", PT.PART, "Definitions")])

part2 = Part("2", PT.PART, "Permitted gaming activities")
part2.add_parts([
    Part("4", PT.PART, "Art union gaming activities"),
    Part("5", PT.PART, "Housie or bingo"),
    Part("6", PT.PART, "Draw lotteries"),
    Part("7", PT.PART, "No-draw lotteries"),
    Part("8", PT.PART, "Mini-numbers lotteries"),
    Part("9", PT.PART, "Progressive lotteries"),
    Part("10", PT.PART, "Free lotteries"),
    Part("11", PT.PART, "Promotional raffles conducted by registered clubs"),
    Part("12", PT.PART, "Other gaming activities for charitable purposes"),
    Part("13", PT.PART, "Sweeps and calcuttas"),
    Part("14", PT.PART, "Trade promotion gaming activities")])


def cg_json_str(reference):
    community_gaming_dict = community_gaming_reg.part_dict
    del community_gaming_dict["parts"]
    refs_json = str(reference)
    cgd_json = str(community_gaming_dict)
    ret = {"rule": cgd_json,
           "clause": refs_json
           }
    return json.dumps(ret, indent=4, sort_keys=True, default=str)


community_gaming_reg.add_parts([part1, part2])

print(cg_json_str(community_gaming_reg["2"]["10"]))
