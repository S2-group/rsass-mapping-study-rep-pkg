import csv
import numpy as np
import os
robotics_entries = []
architecture_entries = []
adaptive_entries = []

print("In this version of the script, only the final selection for the second revision i.e. including the keyword reconfiguration, and three new SE journals, relative to the original branch are made.")
print("Please modify the script to fully recreate the previous phases true to the time at which they were done.")


SEED = 1337
DATA_SOURCE = "data/all_pilot.csv"
PILOT_SIZE = 120
np.random.seed(SEED)

studies_from_pilot = []

def create_reviewer_file(final_path, file_name, reviewer_studies):
    os.makedirs(final_path,exist_ok=True)

    csv_file = open(final_path + "/" + file_name+'.csv', 'w', encoding='utf-8', newline="")

    fieldnames =  list(reviewer_studies[0].keys())
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for study in reviewer_studies:
        studies_from_pilot.append(study['ee']) #this will also happen for the final, but with no side-effect.
        writer.writerow(study)
    
    csv_file.close()


category_to_list = {
    "Software_Architecture" : architecture_entries,
    "Robotics" : robotics_entries,
    "Self-Adaptive_Systems" : adaptive_entries
}



def create_pilot(pilot_path):
    os.makedirs(pilot_path,exist_ok=True)
    one_third_chunk = int(PILOT_SIZE/3)

    robot_selection = list(np.random.choice(robotics_entries,one_third_chunk,replace=False))
    archi_selection = list(np.random.choice(architecture_entries,one_third_chunk,replace=False))
    adapt_selection = list(np.random.choice(adaptive_entries,one_third_chunk,replace=False))

    pilot_studies = robot_selection + archi_selection + adapt_selection

    np.random.shuffle(pilot_studies)


    REVIEWER1 = pilot_studies[:one_third_chunk]
    REVIEWER2 = pilot_studies[one_third_chunk:2*one_third_chunk]
    REVIEWER3 = pilot_studies[2*one_third_chunk:]


    create_reviewer_file(pilot_path, "/reviewer1b",REVIEWER1)
    create_reviewer_file(pilot_path, "/reviewer2b",REVIEWER2)
    create_reviewer_file(pilot_path, "/reviewer3b",REVIEWER3)

    #PILOT 2
    for selected in robot_selection: robotics_entries.remove(selected)
    for selected in archi_selection: architecture_entries.remove(selected)
    for selected in adapt_selection: adaptive_entries.remove(selected)



# with open(DATA_SOURCE, 'r', encoding='utf-8', newline="") as csvfile:
#     venue_reader = csv.DictReader(csvfile)
#     #next(venue_reader) #skip header

#     for row in venue_reader:
#         del row['hit num']
#         category_to_list[row["venue_category"]].append(row)


# all_entries_before_pilots = architecture_entries + robotics_entries + adaptive_entries
# identifiers_before_pilots = []
# for entry in all_entries_before_pilots:
#     identifiers_before_pilots.append(entry['ee'])


# create_pilot("selection/pilots/pilot_one")

# create_pilot("selection/pilots/pilot_two")

# new_stuff = []

# with open("data/all_filtered_by_title.csv", 'r', encoding='utf-8', newline="") as csvfile:
#     venue_reader = csv.DictReader(csvfile)
#     #next(venue_reader) #skip header
#     for row in venue_reader:
#         del row['hit num']
#         new_stuff.append(row)


# to_be_removed = []
# for entry in new_stuff: 
#     try:
#         if(entry['ee'] in identifiers_before_pilots):
#             to_be_removed.append(entry)
#     except ValueError:
#         print("err")

# for to_remove in to_be_removed: new_stuff.remove(to_remove)

# remaining_after_pilots = robotics_entries + architecture_entries + adaptive_entries

# final_set = remaining_after_pilots + new_stuff


# np.random.shuffle(final_set)

# total_num = len(final_set)

# equal_part = int(total_num/6)

# first_share = equal_part * 3 #Elvin does the work of 3
# print(len(final_set))
# ELVIN = final_set[:first_share]

# REVIEWER1 = final_set[first_share:first_share+equal_part] #reviewer1 does 1/6th
# REVIEWER2 = final_set[first_share+equal_part:first_share+equal_part+equal_part] #reviewer 2 does the 1/6th after that
# REVIEWER3 = final_set[first_share+equal_part+equal_part:] #the remaining 1/6th or so goes to reviewer3


#In the pilots, Elvin did the same selection as the other 3 so there are only 3 files each time. However, for the final selection Elvin selected from unique papers not done by the other three..
# create_reviewer_file("selection/final_selection", "finalreviewerE",ELVIN)
# create_reviewer_file("selection/final_selection", "finalreviewer1",REVIEWER1)
# create_reviewer_file("selection/final_selection", "finalreviewer2",REVIEWER2)
# create_reviewer_file("selection/final_selection", "finalreviewer3",REVIEWER3)

####REVISION - I want to cleanly separate what was originally done and the revision, so I handle the it as a separate file below.

# revision_papers = []
# venue_reader = None
# with open("data/revision.csv", 'r', encoding='utf-8', newline="") as csvfile:
#     venue_reader = csv.DictReader(csvfile)
#     #next(venue_reader) #skip header
#     for row in venue_reader:
#         del row['hit num']
#         revision_papers.append(row)

# np.random.shuffle(revision_papers)

# total_num = len(revision_papers)

# equal_part = int(total_num/6)

# first_share = equal_part * 3 #Elvin does the work of 3
# print(len(revision_papers))

# ELVIN = revision_papers[:first_share]

# REVIEWER1 = revision_papers[first_share:first_share+equal_part] #reviewer1 does 1/6th
# REVIEWER2 = revision_papers[first_share+equal_part:first_share+equal_part+equal_part] #reviewer 2 does the 1/6th after that
# REVIEWER3 = revision_papers[first_share+equal_part+equal_part:] #the remaining 1/6th or so goes to reviewer3

# create_reviewer_file("selection/revision_selection", "finalreviewerE",ELVIN)
# create_reviewer_file("selection/revision_selection", "finalreviewer1",REVIEWER1)
# create_reviewer_file("selection/revision_selection", "finalreviewer2",REVIEWER2)
# create_reviewer_file("selection/revision_selection", "finalreviewer3",REVIEWER3)

####REVISION - I want to cleanly separate what was originally done and the second revision, so I handle the it as a separate file below.
np.random.seed(SEED) #resetting the seed so I don't need to rerun the above.
revision_papers = []
venue_reader = None
with open("data/second_revision.csv", 'r', encoding='utf-8', newline="") as csvfile:
    venue_reader = csv.DictReader(csvfile)
    #next(venue_reader) #skip header
    
    for row in venue_reader:
        del row['hit num']
        revision_papers.append(row)

np.random.shuffle(revision_papers)

total_num = len(revision_papers)

equal_part = int(total_num/6)

first_share = equal_part * 3 #Elvin does the work of 3
print(len(revision_papers))

ELVIN = revision_papers[:first_share]

REVIEWER1 = revision_papers[first_share:first_share+equal_part] #reviewer1 does 1/6th
REVIEWER2 = revision_papers[first_share+equal_part:first_share+equal_part+equal_part] #reviewer 2 does the 1/6th after that
REVIEWER3 = revision_papers[first_share+equal_part+equal_part:] #the remaining 1/6th or so goes to reviewer3

create_reviewer_file("selection/sssecond_revision_selection", "finalreviewerE",ELVIN)
create_reviewer_file("selection/sssecond_revision_selection", "finalreviewer1",REVIEWER1)
create_reviewer_file("selection/sssecond_revision_selection", "finalreviewer2",REVIEWER2)
create_reviewer_file("selection/sssecond_revision_selection", "finalreviewer3",REVIEWER3)