import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Define filePath
# ---------------------- #
root = tk.Tk()
root.withdraw()
filePath = filedialog.askopenfilename()
fileName = os.path.basename(filePath)
fileDir = os.path.dirname(filePath)
outputFileName = fileDir.split('/')[-1]
outputFile = f'{fileDir}/{outputFileName}.png'

print("Location:", filePath)
print("File: ", fileName)
print("Dir:", fileDir)

raw_data = pd.read_csv(filePath, sep=",", header=[3, 4], encoding='ISO-8859-1')
print(raw_data.head())

filter_ = np.argwhere(np.array(raw_data['OP Speed 1']) < 5).flatten().tolist()
# filter_ = raw_data[raw_data['OP Speed 1'] > 10].index
raw_data.drop(filter_, inplace=True)
raw_data.reset_index(drop=True, inplace=True)

raw_data['AxleTorque'] = raw_data['OP Torque 1'] + raw_data['OP Torque 2']
# print(filter_.head())


# print(filtered_data.head())

fig, ax = plt.subplots(3, figsize=(16, 9))

ax[0].plot(
    raw_data['Event Time'],
    raw_data['IP Speed 1'],
    color="green",
    label="IP Speed [rpm]",
    marker=None
)
# ax[0].plot(
#     raw_data['Event Time'],
#     raw_data['OP Speed 2'],
#     color="blue",
#     label="RH OP Speed [rpm]",
#     marker=None
# )
axSecondary = ax[0].twinx()
axSecondary.plot(
    raw_data['Event Time'],
    raw_data['1306 Oil In - TCM_SumpoilTBas'],
    color="magenta",
    label="Oil Temperature [degC]",
    marker=None
)
axSecondary.set_ylim([0, 100])
axSecondary.legend(loc=1)

ax[0].set_title("Shaft Speeds", loc='left')
ax[0].grid()
ax[0].legend(loc=4)
# ax[0].set_xlim([0, max_data_EventTime])
ax[0].set_xlabel("Time [s]")
ax[0].set_ylim([0, 3000])

# ax[1].plot(
#     raw_data['Event Time'],
#     raw_data['TCM MaiShaftNBas'],
#     color="red",
#     label="Mainshaft Speed [rpm]",
#     marker=None
# )
# ax[1].set_title("Mainshaft Speed", loc='left')
# ax[1].grid()
# ax[1].legend(loc=4)
# # ax[0].set_xlim([0, max_data_EventTime])
# ax[1].set_xlabel("Time [s]")
# ax[1].set_ylim([0, 2000])

ax[1].plot(
    raw_data['Event Time'],
    raw_data['IP Torque 1'],
    color="purple",
    label="IP Torque [Nm]",
    marker=None
)
# ax[1].plot(
#     raw_data['Event Time'],
#     raw_data['OP Torque 2'],
#     color="orange",
#     label="RH OP Torque [Nm]",
#     marker=None
# )

ax[1].set_title("Input Torque", loc='left')
ax[1].grid()
ax[1].legend(loc=4)
# ax[0].set_xlim([0, max_data_EventTime])
ax[1].set_xlabel("Time [s]")
# ax[1].set_ylim([0, 2000])

ax[2].plot(
    raw_data['Event Time'],
    raw_data['AxleTorque'],
    color="orange",
    label="Axle Torque [Nm]",
    marker=None
)

ax[2].set_title("Axle Torque (LH + RH)", loc='left')
ax[2].grid()
ax[2].legend(loc=4)
# ax[0].set_xlim([0, max_data_EventTime])
ax[2].set_xlabel("Time [s]")
# ax[1].set_ylim([0, 300])

#
# ax[3].plot(
#     raw_data['Event Time'],
#     raw_data['OP Torque 1'],
#     color="red",
#     label="LH OP Torque [Nm]",
#     marker=None
# )
# ax[2].plot(
#     raw_data['Event Time'],
#     raw_data['OP Torque 2'],
#     color="orange",
#     label="RH OP Torque [Nm]",
#     marker=None
# )
#
# ax[2].set_title("Output Torque", loc='left')
# ax[1].grid()
# ax[1].legend(loc=2)
# # ax[0].set_xlim([0, max_data_EventTime])
# ax[1].set_xlabel("Time [s]")
# # ax[1].set_ylim([0, 300])

fig.suptitle(f'{fileDir}', fontsize=10)
plt.subplots_adjust(left=0.05, bottom=0.07, right=0.965, top=0.9, wspace=0.2, hspace=0.4)
plt.savefig(outputFile, format='png', bbox_inches='tight', dpi=150)
plt.show()
