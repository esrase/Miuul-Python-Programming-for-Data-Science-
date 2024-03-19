##Görev1-Task1##
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
new_columns = ["NUM_" + col.upper() if df[col].dtype != "object" else col.upper() for col in df.columns]

for col in new_columns:
    print(col)

##Görev2-Task2##
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


kolon=["abbrev", "no_previous"]
list_kolon = [kolon.upper() if "no" in kolon else kolon.upper() + "_FLAG" for kolon in df.columns]

##Görev3-Task3##
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()

