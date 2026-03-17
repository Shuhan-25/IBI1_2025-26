#population growth rate analysis
import matplotlib.pyplot as plt
import numpy as np

#population data (in millions)
countries = ['UK', 'China', 'Italy', 'Brazil', 'USA']
pop2020 = [66.7, 1426, 59.4, 208.6, 331.6]
pop2024 = [69.2, 1410, 58.9, 212.0, 340.1]

#calculate changes
changes = []
for i in range(len(countries)):
    change = ((pop2024[i] - pop2020[i]) / pop2020[i]) * 100
    changes.append(change)
    print(f"{countries[i]}: {change:.2f}%")

#sort
sorted_data = sorted(zip(countries, changes), key=lambda x: x[1], reverse=True)

print("Sorted:")
for country, change in sorted_data:
    print(f"{country}: {change:.2f}%")

print(f"\nLargest increase: {sorted_data[0][0]} ({sorted_data[0][1]:.2f}%)")
print(f"Largest decrease: {sorted_data[-1][0]} ({sorted_data[-1][1]:.2f}%)")


#chart
plt.figure(figsize=(10, 6))
names = [x[0] for x in sorted_data]
values = [x[1] for x in sorted_data]

bars = plt.bar(names, values, color=['green' if v>0 else 'red' for v in values])

#add data labels on bars
for i, (bar, val) in enumerate(zip(bars, values)):
    height = bar.get_height()
    if val > 0:
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{val:.2f}%', ha='center', va='bottom', fontsize=10)
    else:
        plt.text(bar.get_x() + bar.get_width()/2., height - 0.8,
                f'{val:.2f}%', ha='center', va='top', fontsize=10)

plt.title('Population Change')
plt.xlabel('Country')
plt.ylabel('Change (%)')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='black', linewidth=0.5)  # Add line at zero
plt.tight_layout()
plt.show()
