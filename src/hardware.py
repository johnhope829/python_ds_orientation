import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# read csv
df = pd.read_csv('data/msds-orientation-survey.csv')

# change timestamp to datetime field
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format = '%m/%d/%y %H:%M')

# filter to 2025 cohort
df = df[df['Timestamp'] >= '6/13/2024'].reset_index()

# write to data folder
df.to_csv('data/msds-orientation-survey-manipulated.csv')

# set up figure
fig, axes = plt.subplots(3,2, constrained_layout=True)
fig.delaxes(axes[2,1])

# ram
plt.subplot(3,2,1)
plt.hist(df['RAM (in GB)'], 10, color='grey', edgecolor='black')
plt.ylabel('Count')
plt.yticks((0,10,20,30,40,50,60))
plt.title('RAM (in GB)')

# cpu cores
plt.subplot(3,2,2)
plt.hist(df['CPU Number of Cores (int)'], 10, color='grey', edgecolor='black')
plt.ylabel('Count')
plt.yticks((0,10,20,30,40,50,60))
plt.title('CPU Number of Cores (int)')

# cpu cycle rate
plt.subplot(3,2,3)
plt.hist(df['CPU Cycle Rate (in GHz)'], 10, color='grey', edgecolor='black')
plt.ylabel('Count')
plt.yticks((0,10,20,30,40,50,60))
plt.title('CPU Cycle Rate (in GHz)')

# hard drive
plt.subplot(3,2,4)
plt.hist(df['Hard Drive Size (in GB)'], 10, color='grey', edgecolor='black')
plt.ylabel('Count')
plt.yticks((0,10,20,30,40,50,60))
plt.title('Hard Drive Size (in GB)')

# gpu cuda cores
plt.subplot(3,2,5)
plt.hist(df['GPU CUDA Number of Cores (int)'], 10, color='grey', edgecolor='black')
plt.ylabel('Count')
plt.yticks((0,10,20,30,40,50,60))
plt.title('GPU CUDA Number of Cores (int)')

plt.suptitle('2025 MSDS Cohort Hardware Measures')

plt.savefig('figures/hardware_histograms.png')