import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns
from cycler import cycler
import sys
import matplotlib.colors as mcolors
import os
SHOW = True
SAVE = False

years = []
paper_id = []




adap_purp_poss = ["Recover from errors/faults", "Optimize resource usage","Deal with environmental changes","Keep meeting quality requirements at runtime","Change functional behavior","Optimize system performance","Recover from attacks"]
qa_poss = ["performance efficiency","reliability","safety","functional suitability","security"]
monitor_poss = ["Environment", "Managed System", "Mission"]
analyze_poss = ["Comparison to threshold(s)", "Done during Plan", "Analyzing/Aggregating data", "Task/User-driven", "System State Anomaly Detection", "Logical Inference", "Other"]
plan_poss = ["Using AI Planning Languages","Determining the optimal choice","Relying on Design-time Rules/Models"]
execute_poss = ["Component Redeployment ","Addition &/or Removal of Component(s)","Change in Relationship(s) Between Components","Reparameterization of Component(s)"]
logic_poss = ["search procedure","constraint solving/model checking","ontological reasoning","application-specific logic","AI planner","numerical optimization","graph transformation", "design-time rules"]

eval_poss = ["Quality","Mission Performance","Overhead (Introduced)","Domain-specific Performance", "Resource Consumption"]

MISSION_NAME = "I0 Mission"
MISSION_EVO = "I1.1 Metadata"
ROBO_SW = "I4 Robo SW"
ROBO_MODEL = "I3 Robot Type"
DEPLOY = "I7 Deployment Realness"
REALISM = "I7 Mission Realness"
EVAL_METRIC = "I8 Evaluation"
EVAL_DEPTH = "Experiment Method"

CHANGE_SOURCE = "I1.2 Source of Change" 
CHANGE_TYPE = "I1.2 Type of Change" 
CHANGE_ANTI =  "I1.2 Anticipation of Change"
CHANGE_FREQ = "I1.2 Frequency of Change"

MECH_TYPE = "I1.3 Type of Mechanism"
MECH_ORG = "I1.3 Organization of Mechanism"
MECH_SCOPE = "I1.3 Scope of Mechanism"
MECH_DUR = "I1.3 Duration of Mechanism"
MECH_TIME = "I1.3 Timeliness of Mechanism"
MECH_TRIG = "I1.3 Trigger of Mechanism"

EFFECT_CRIT = "I1.4 Criticality of Effects" 
EFFECT_PRED = "I1.4 Predictability of Effects"
EFFECT_OVHD = "I1.4 Overhead of Effects"
EFFECT_RESI =  "I1.4 Resilience of Effects" 


INDEPEND = "I6 Independence"
ADAP_PURP = "I2 Adap. Purpose" 
QUAL_ATT = "I5 QA" 

MAPE_MON = "I10 Monitor" 
MAPE_ANA = "I11 Analyze"
MAPE_PLN = "I12 Plan" 
MAPE_EXE = "I13 Execute" 
MAPE_KNO = "I14 Knowledge"

ADAP_LOG = "I9 Adap. Logic"
YEARS = "year"

REPLICATION = "I15 Replication"

MULTIPLICITOUS = [CHANGE_SOURCE,CHANGE_TYPE,MECH_TYPE,MECH_SCOPE,EFFECT_PRED,ADAP_PURP,QUAL_ATT,EVAL_METRIC,ADAP_LOG,MAPE_MON,MAPE_ANA,MAPE_PLN,MAPE_EXE]

horizontal_pairs = [
    (MISSION_NAME,CHANGE_SOURCE),
    (MISSION_NAME,MECH_ORG),
    (CHANGE_SOURCE,ADAP_PURP),
    (CHANGE_SOURCE,MECH_TYPE),
    (MECH_TYPE,QUAL_ATT),
    (MECH_SCOPE,QUAL_ATT),
    (INDEPEND,QUAL_ATT),
    (INDEPEND,EFFECT_CRIT),
    (INDEPEND,EFFECT_PRED),
    (INDEPEND,EFFECT_OVHD),
    (INDEPEND,CHANGE_FREQ),
    (MISSION_NAME,DEPLOY),
    (MISSION_NAME,REALISM),
    (ADAP_LOG,MECH_TYPE),
    (ADAP_LOG,MECH_ORG),
    (ADAP_LOG,MECH_SCOPE),
    (ADAP_LOG,EFFECT_CRIT),
    (ADAP_LOG,EFFECT_PRED),
    (ADAP_LOG,QUAL_ATT),
    (EVAL_METRIC,DEPLOY),
    (EVAL_METRIC,REALISM),
    (ADAP_LOG,DEPLOY),
    (ADAP_LOG,REALISM),


]

show_or_save = SAVE

csv_data = {
    MISSION_NAME: [],
    MISSION_EVO : [],
    ROBO_MODEL : [],
    DEPLOY : [],
    REALISM : [],
    EVAL_METRIC :[],
    EVAL_DEPTH : [],
    CHANGE_SOURCE : [],
    CHANGE_TYPE : [],
    CHANGE_ANTI : [],
    CHANGE_FREQ : [],
    MECH_TYPE: [],
    MECH_ORG: [],
    MECH_SCOPE: [],
    MECH_DUR : [],
    MECH_TIME: [],
    MECH_TRIG: [],
    EFFECT_CRIT: [],
    EFFECT_PRED: [],
    EFFECT_OVHD: [],
    EFFECT_RESI: [],
    ROBO_SW : [],
    INDEPEND : [],
    ADAP_PURP: [],
    QUAL_ATT : [],
    MAPE_MON: [],
    MAPE_ANA : [],
    MAPE_PLN: [],
    MAPE_EXE : [],
    MAPE_KNO : [],
    ADAP_LOG: [],
    YEARS: [],
    REPLICATION: [],
}

csv_title_to_plot_title = {
    MISSION_NAME: "Mission",
    MISSION_EVO : "Mission Evolution",
    ROBO_MODEL : "Type of Robots",
    DEPLOY : "System Deployment",
    REALISM : "System Realism",
    EVAL_METRIC : "Evaluation Metric",
    EVAL_DEPTH : "Evaluation Depth",
    CHANGE_SOURCE : "Source of Change",
    CHANGE_TYPE : "Type of Change",
    CHANGE_ANTI : "Anticipation of Change",
    CHANGE_FREQ : "Frequency of Change",
    MECH_TYPE : "Type of Mechanism",
    MECH_ORG : "Organization of Mechanism",
    MECH_DUR : "Duration of Mechanism",
    MECH_SCOPE : "Scope of Mechanism",
    MECH_TIME : "Timeliness of Mechanism",
    MECH_TRIG : "Trigger of Mechanism",
    EFFECT_PRED: "Predictability of Effects",
    EFFECT_CRIT: "Criticality of Effects",
    EFFECT_OVHD: "Overhead of Effects",
    EFFECT_RESI: "Resilience of Effects",
    ROBO_SW : "Software Platform",
    INDEPEND : "Managing System Independence",
    ADAP_PURP: "Adaptation Goal",
    QUAL_ATT : "Quality Attributes",
    MAPE_MON: "MAPE-K: Monitor",
    MAPE_ANA : "MAPE-K: Analyze",
    MAPE_PLN: "MAPE-K: Plan",
    MAPE_EXE : "MAPE-K: Execute",
    MAPE_KNO : "MAPE-K: Knowledge",
    ADAP_LOG: "Mechanism Approach",
    REPLICATION: "Replication Package Linked"
}

plt.style.use('ggplot')

# Retrieve the color cycle iterator
color_cycle = iter(plt.rcParams['axes.prop_cycle'])

# Advance the color cycle iterator to the next color
next_color = next(color_cycle)['color']
next_color = next(color_cycle)['color']
next_color = next(color_cycle)['color']




plt.rcParams['axes.prop_cycle'] = cycler('color', [next_color])



def plot_plot(title):
    plt.tight_layout()
    if(show_or_save == SAVE):
        plt.savefig(title)
    if(show_or_save == SHOW):
        plt.show()


def RQ11():
    multi_df_plot(adap_purp_poss,csv_data[ADAP_PURP], csv_title_to_plot_title[ADAP_PURP], "plots/Adaptation Purposes.pdf", plot_type="barh")
    multi_df_plot(qa_poss,csv_data[QUAL_ATT], csv_title_to_plot_title[QUAL_ATT], "plots/Quality Attributes.pdf", plot_type="barh")

    barplot_paper_id_by_x(csv_data[INDEPEND],"plots/plot_by_indepedence.pdf",csv_title_to_plot_title[INDEPEND], _kind='barh')

def RQ12():
    mech_dimension(bar_type="barh")
    mapek_parts(bar_type="barh")
    multi_df_plot(logic_poss,csv_data[ADAP_LOG], csv_title_to_plot_title[ADAP_LOG], "plots/Adaptation Logics.pdf", plot_type="barh")

def RQ13():
    barplot_paper_id_by_x(csv_data[MISSION_NAME],"plots/Missions.pdf",csv_title_to_plot_title[MISSION_NAME], _kind="barh")
    barplot_paper_id_by_x(csv_data[MISSION_EVO],"plots/Mission Evolution.pdf",csv_title_to_plot_title[MISSION_EVO], _kind="barh")
    change_dimension(bar_type="barh")
    effect_dimension(bar_type="barh")
    barplot_paper_id_by_x(csv_data[ROBO_SW],"plots/Software Platform.pdf",csv_title_to_plot_title[ROBO_SW], _kind="barh")
    barplot_paper_id_by_x(csv_data[ROBO_MODEL],"plots/Types of Robots.pdf",csv_title_to_plot_title[ROBO_MODEL], _kind="barh")

def RQ2():
    barplot_paper_id_by_x(csv_data[DEPLOY],"plots/System Deployment.pdf",csv_title_to_plot_title[DEPLOY], _kind="barh")
    barplot_paper_id_by_x(csv_data[REALISM],"plots/System Realism.pdf",csv_title_to_plot_title[REALISM], _kind="barh")

    multi_df_plot(eval_poss,csv_data[EVAL_METRIC], csv_title_to_plot_title[EVAL_METRIC], "plots/Evaluation Strategies.pdf", plot_type="barh")
    barplot_paper_id_by_x(csv_data[EVAL_DEPTH],"plots/Evaluation Depth.pdf",csv_title_to_plot_title[EVAL_DEPTH],  _kind="barh")
    barplot_paper_id_by_x(csv_data[REPLICATION],"plots/Replication Package.pdf", csv_title_to_plot_title[REPLICATION],_kind="barh")

    
labels_too_long = {
    "Keep meeting quality requirements at runtime" : "Keep meeting QRs at runtime",
    "performance efficiency" : "Performance Efficiency",
    "reliability" : "Reliability",
    "safety" : "Safety",
    "functional suitability" : "Functional Suitability",
    "security" : "Security",
    "search procedure"  : "Search Procedure", 
    "constraint solving/model checking" : "Constraint Solving/Model Checking", 
    "ontological reasoning" : "Ontological Reasoning",
    "domain-specific algorithm" : "Domain-Specific Algorithm",
    "AI planner" :  "AI Planner",
    "utility calculation" : "Utility Calculation",
    "Comparison to threshold(s)" : "Comparison to Threshold(s)",
    "numerical optimization" : "Numerical Optimization",
    "DoForeseen" : "Foreseen",
    "DoFrequent" : "Frequent",
    "DoShort" : "Short",
    "DoCentralized" : "Centralized",
    "DoSignificant" : "Significant",
    "DoResilient" : "Resilient",
    "dependent" : "Dependent",
    "Addition &/or Removal of Component(s)" : "Addition and/or Removal of Component(s)"
}

    
    




def effect_dimension(bar_type='bar'):

    standard_fields = [EFFECT_CRIT, EFFECT_OVHD,EFFECT_RESI]

    for i, field_name in enumerate(standard_fields):

        eff_elem = csv_data[field_name]

        barplot_paper_id_by_x(eff_elem,"plots/" +  csv_title_to_plot_title[field_name] + ".pdf",csv_title_to_plot_title[field_name], _kind=bar_type)



    pred_poss = ["Deterministic", "Non-deterministic"]

    multi_df_plot(pred_poss,csv_data[EFFECT_PRED],csv_title_to_plot_title["I1.4 Predictability of Effects"], "plots/" + csv_title_to_plot_title["I1.4 Predictability of Effects"] + ".pdf",plot_type=bar_type)

def mech_dimension(bar_type='bar'):

    standard_fields = [MECH_ORG, MECH_DUR, MECH_TIME, MECH_TRIG]

    for i, field_name in enumerate(standard_fields):
        mech_elem = csv_data[field_name]
        barplot_paper_id_by_x(mech_elem,"plots/" +  csv_title_to_plot_title[field_name] + ".pdf",csv_title_to_plot_title[field_name], _kind=bar_type)



    multi_df_plot(["Structural", "Parametric"],csv_data[MECH_TYPE],"Type of Mechanism", "plots/Type of Mechanism.pdf",plot_type=bar_type)
    multi_df_plot(["Global", "Local"],csv_data[MECH_SCOPE], "Scope of Mechanism", "plots/Scope of Mechanism.pdf",plot_type=bar_type)


def change_dimension(bar_type='bar'):


    change_source_poss = ["Internal", "External"]
    change_type_poss = ["Technological", "Non-functional", "Functional"]
    multi_df_plot(change_source_poss,csv_data[CHANGE_SOURCE], "Source of Change", "plots/Source of Change.pdf",plot_type="barh")

    multi_df_plot(change_type_poss,csv_data[CHANGE_TYPE], "Type of Change", "plots/Type of Change.pdf",plot_type=bar_type)

    for i, change_elem in enumerate([CHANGE_ANTI, CHANGE_FREQ]):

        barplot_paper_id_by_x(csv_data[change_elem],"plots/" +  csv_title_to_plot_title[change_elem] + ".pdf",csv_title_to_plot_title[change_elem], _kind=bar_type)





def mapek_parts(bar_type="bar"):
    multi_df_plot(monitor_poss,csv_data[MAPE_MON], csv_title_to_plot_title[MAPE_MON], "plots/MAPEK Monitor.pdf", plot_type=bar_type)
    multi_df_plot(analyze_poss,csv_data[MAPE_ANA], csv_title_to_plot_title[MAPE_ANA], "plots/MAPEK Analyze.pdf", plot_type=bar_type)
    multi_df_plot(plan_poss,csv_data[MAPE_PLN], csv_title_to_plot_title[MAPE_PLN], "plots/MAPEK Plan.pdf", plot_type=bar_type)
    multi_df_plot(execute_poss,csv_data[MAPE_EXE], csv_title_to_plot_title[MAPE_EXE], "plots/MAPEK Execute.pdf", plot_type=bar_type)
    barplot_paper_id_by_x(csv_data[MAPE_KNO],"plots/MAPEK Knowledge.pdf",csv_title_to_plot_title[MAPE_KNO],_kind=bar_type)



def multi_df_plot(possibilities, original_data, subject_title, plot_title, plot_type="bar"):

    occurrences_of_type = [0] * len(possibilities)

    for i, some__type in enumerate(possibilities):
        for type_occ in original_data:
            # if(some__type in type_occ): 
                # occurrences_of_type[i]+=1
            occurrences_of_type[i]+=type_occ.count(some__type)
            


    for i, poss in enumerate(possibilities):
        if(poss in labels_too_long):

            possibilities[i] = labels_too_long[poss]
        
    type_df = pd.DataFrame(data={subject_title: possibilities, 'Num. Occurrences': occurrences_of_type})
    type_df.sort_values(by='Num. Occurrences', ascending=True, inplace=True)
    print(type_df)
    if(plot_type == "bar"):
        smt = type_df.plot(kind=plot_type, legend=False, ylabel='Num. Occurrences', xlabel=subject_title, color=next_color)
        smt.bar_label(smt.bar(list(range(len(type_df['Num. Occurrences']))),list(type_df['Num. Occurrences'])),label_type="center", fontweight = "medium", fontsize = "large")
        smt.set_xticklabels(type_df[subject_title])
    elif(plot_type == "barh"):
        smt = type_df.plot(kind=plot_type, legend=False, xlabel='Num. Occurrences', ylabel="", color=next_color)
        smt.bar_label(smt.barh(list(range(len(type_df['Num. Occurrences']))),list(type_df['Num. Occurrences'])),label_type="center", fontweight = "medium", fontsize = "large")

        smt.set_yticklabels(type_df[subject_title], wrap=True)

    plot_plot(plot_title)


def barplot_paper_id_by_x(x, plot_filename, x_title, _kind='bar'):
    x_df = pd.DataFrame(data={'ID': paper_id, x_title: x})

    count_by_x_df =  x_df.groupby(x_title).count()
    count_by_x_df.drop("_", inplace=True, errors="ignore")

    count_by_x_df.sort_values(by='ID', ascending=True, inplace=True)

    count_by_x_df.rename(index=labels_too_long, inplace=True)
    # for replace_word in list(labels_too_long.keys()):
    #     count_by_x_df.replace(to_replace=labels_too_long, inplace=True)
    # print(count_by_x_df.index)

    print(count_by_x_df)
    if(_kind == "bar"):
        if(x_title == "Publication Year"):
            count_by_x_df.sort_values(by='Publication Year', ascending=True, inplace=True)

            smt = count_by_x_df.plot(kind=_kind, legend=False, ylabel="Number of Studies", yticks = [1,2,3,4], title="")
        else:
            smt = count_by_x_df.plot(kind=_kind, legend=False, ylabel="Number of Studies", title="")
        smt.bar_label(smt.bar(list(range(len(count_by_x_df['ID']))),list(count_by_x_df['ID'])),label_type="center", fontweight = "medium", fontsize = "large")

    elif(_kind == "barh"):
        smt = count_by_x_df.plot(kind=_kind, legend=False, xlabel="Number of Studies", ylabel="")
        smt.bar_label(smt.barh(list(range(len(count_by_x_df['ID']))),list(count_by_x_df['ID'])),label_type="center", fontweight = "medium", fontsize = "large")



    # plot = count_by_x_df.plot(kind=_kind, legend=False, ylabel="Number of Studies")

    plot_plot(plot_filename)

def plot_by_year():
    barplot_paper_id_by_x([int(yea) for yea in csv_data[YEARS]], "plots/plot_by_year.pdf", "Publication Year", _kind = "bar")








def test_horizontal(param_one, param_two):

    col1 = csv_data[param_one]
    col2 = csv_data[param_two]
    indices_to_remove = []
    for i in range(len(col1)):
        if(col1[i] == "_" or col2[i] == "_"):
            indices_to_remove.append(i)
    
    col1_cleaned = [col1[i] for i in range(len(col1)) if i not in indices_to_remove]
    col2_cleaned = [col2[i] for i in range(len(col2)) if i not in indices_to_remove]
    print(col1_cleaned)
    print(col2_cleaned)

    testpd = pd.crosstab(col1_cleaned,col2_cleaned)

    print(testpd)

    sns.heatmap(testpd, annot=True)

    plt.show()





if __name__ == "__main__":
    
    passed_options = sys.argv[1:]

    if("--show") in passed_options:
        show_or_save = SHOW
        
    with open('data/cleaned_data.csv', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for i, row in enumerate(csv_reader):
            paper_id.append(row['Paper ID'])

            for data_key in list(csv_data.keys()):
                csv_data[data_key].append(row[data_key])
            
        os.makedirs("plots/",exist_ok=True)
        plot_by_year()

        RQ11()
        RQ12()
        RQ13()
        RQ2()
    

            
            

