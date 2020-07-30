from openfisca_nsw_community_gaming.variables.regulation_reference import Regulation, PartType as PT

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

part3 = community_gaming_reg.add_part("3", PT.PART, "Authorities")
part3.add_parts([
    ("15", PT.CLAUSE, "Applications for authorities"),
    ("16", PT.CLAUSE, "Duration of registration"),
    ("17", PT.CLAUSE, "Amendment of Licensing and Registration (Uniform Procedures) Act 2002 No 28"),
    ("18", PT.CLAUSE, "Application for authority to conduct art union gaming activity"),
    ("19", PT.CLAUSE, "Time period for restoration of authorities"),
    ("20", PT.CLAUSE, "Condition of authority—rules to be given to Secretary"),
    ("21", PT.CLAUSE, "Register of authorities")])

part4 = community_gaming_reg.add_part("4", PT.PART, "Requirements for conduct of permitted gaming activities")
div1 = part4.add_part("1", PT.DIVISION, "Offences")
div1.add_parts([
    ("22", PT.CLAUSE, "Offences"),
    ("23", PT.CLAUSE, "Return of ticket-butts and drawing-dockets")])

div2 = part4.add_part("2", PT.DIVISION, "General requirements for gaming activities")
div2.add_parts([
    ("24", PT.CLAUSE, "Fairness"),
    ("25", PT.CLAUSE, "Rules of gaming activities—transparency"),
    ("26", PT.CLAUSE, "Rules of gaming activities to be made available"),
    ("27", PT.CLAUSE, "Display of authority number on advertising material"),
    ("28", PT.CLAUSE, "Changes to gaming activities to be notified by authority holders"),
    ("29", PT.CLAUSE, "Maximum cost of remote participation"),
    ("30", PT.CLAUSE, "Records"),
    ("31", PT.CLAUSE, "Deposit of proceeds"),
    ("32", PT.CLAUSE, "Commission and other payments for gaming activities requiring authority"),
    ("33", PT.CLAUSE, "Prohibited commissions"),
    ("34", PT.CLAUSE, "Deduction of expenses of conducting gaming activities"),
    ("35", PT.CLAUSE, "Benefiting organisation must authorise conduct of gaming activity"),
    ("36", PT.CLAUSE, "Consecutive or concurrent gaming activities"),
    ("37", PT.CLAUSE, "Payment of gross proceeds of progressive lotteries")])

div3 = part4.add_part("3", PT.DIVISION, "Prizes and prize winners")
div3.add_parts([
    ("38", PT.CLAUSE, "Errors not to affect availability of prizes"),
    ("39", PT.CLAUSE, "Liquor prizes"),
    ("40", PT.CLAUSE, "Liquor prizes and minors"),
    ("41", PT.CLAUSE, "Prohibited prizes"),
    ("42", PT.CLAUSE, "Defence—entitlement of winner to prize"),
    ("43", PT.CLAUSE, "Payment of monetary prizes"),
    ("44", PT.CLAUSE, "Changes to prizes"),
    ("45", PT.CLAUSE, "Maintenance of prizes comprising real property"),
    ("46", PT.CLAUSE, "Preservation of prizes"),
    ("47", PT.CLAUSE, "Scrutiny of determination of prizes"),
    ("48", PT.CLAUSE, "Unclaimed prizes where authority required")])

part5 = community_gaming_reg.add_part("5", PT.PART, "Miscellaneous")
part5.add_parts([
    ("49", PT.CLAUSE, "Conduct of gaming activity"),
    ("50", PT.CLAUSE, "Proceeds requirements may be varied by Secretary"),
    ("51", PT.CLAUSE, "Fees"),
    ("52", PT.CLAUSE, "Advertising of gaming activities"),
    ("53", PT.CLAUSE, "Audit of conduct of gaming activities"),
    ("54", PT.CLAUSE, "Secretary’s power to waive, reduce, postpone or refund fees")])


sched1 = community_gaming_reg.add_part("s1", PT.SCHEDULE, "Fees")

sched2 = community_gaming_reg.add_part("s2", PT.SCHEDULE, "Penalty notice offences")

notes = community_gaming_reg.add_part("Historical Notes", PT.NOTES, "Historical Notes")


# print(community_gaming_reg["2", "10"].json())
# print(community_gaming_reg)
# print(community_gaming_reg["2"])
# print(community_gaming_reg["2"]["10"])
