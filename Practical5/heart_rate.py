#heart rate analysis
import matplotlib.pyplot as plt
import numpy as np

# Heart rate data
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

#number of patients and mean heart rate
patient_number = len(heart_rates)
mean_hr = np.mean(heart_rates)
print("number of patients in the dataset:",patient_number)
print("mean heart rate:",mean_hr)

#categorize heart rates
categories = {
    "Low (<60 bpm)":0,
    "Normal (60-120 bpm)":0,
    "High (>120 bpm)":0
}

for hr in heart_rates:
    if hr < 60:
        categories["Low (<60 bpm)"]+=1
    elif hr >120:
        categories["High (>120 bpm)"]+=1
    else:
        categories["Normal (60-120 bpm)"]+=1

#print category counts and find largest category
print("heart rate categories:")
largest_category = None
largest_count = 0

for category, count in categories.items():
    print(f"{category}: {count} patient(s)")
    if count > largest_count:
        largest_count = count
        largest_category = category

print("largest category:",largest_category,"with",largest_count,"patients")

plt.figure(figsize=(8, 8))

#create pie chart
plt.figure(figsize=(8, 8))

categories_list = list(categories.keys())
counts_list = list(categories.values())

plt.pie(
    counts_list, 
    labels=[f"{cat}\n({count}people)" for cat, count in zip(categories_list, counts_list)],
    autopct='%1.1f%%',
    startangle=90,
    colors=['#ff9999', '#66b3ff', '#99ff99']
)

plt.title('Heart Rate Categories Distribution', fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.show()
