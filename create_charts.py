import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Set style for professional-looking charts
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create figure with subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Nanoplastics: Key Data Visualizations', fontsize=16, fontweight='bold')

# 1. Global Plastic Output Growth (2000-2025)
years = [2000, 2005, 2010, 2015, 2020, 2025]
plastic_output = [180, 230, 280, 350, 400, 460]  # Million tons

ax1.plot(years, plastic_output, marker='o', linewidth=3, markersize=8, color='#1f77b4')
ax1.fill_between(years, plastic_output, alpha=0.3, color='#1f77b4')
ax1.set_title('Global Plastic Production Growth', fontweight='bold', fontsize=12)
ax1.set_xlabel('Year')
ax1.set_ylabel('Million Tons')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 500)

# Add trend annotation
ax1.annotate('156% increase\n2000-2025', xy=(2025, 460), xytext=(2010, 400),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=10, fontweight='bold', color='red')

# 2. U.S. Autoimmune Disease Prevalence
years_auto = [2000, 2005, 2010, 2015, 2020, 2025]
prevalence = [5, 5.5, 6, 6.5, 7.5, 8]  # Percentage

ax2.bar(years_auto, prevalence, color='#ff7f0e', alpha=0.7, edgecolor='black', linewidth=1)
ax2.set_title('U.S. Autoimmune Disease Prevalence', fontweight='bold', fontsize=12)
ax2.set_xlabel('Year')
ax2.set_ylabel('Prevalence (%)')
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_ylim(0, 10)

# Add percentage increase annotation
ax2.annotate('60% increase\n2000-2025', xy=(2025, 8), xytext=(2015, 6.5),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=10, fontweight='bold', color='red')

# 3. Research Funding Timeline
funding_years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
epa_funding = [100, 95, 90, 85, 80, 75, 70, 65, 60]  # Relative funding levels
nih_funding = [100, 98, 95, 92, 88, 85, 82, 78, 75]

ax3.plot(funding_years, epa_funding, marker='s', linewidth=2, markersize=6, label='EPA Environmental Health', color='#2ca02c')
ax3.plot(funding_years, nih_funding, marker='^', linewidth=2, markersize=6, label='NIH Environmental Health', color='#d62728')
ax3.set_title('Research Funding Trends (2016-2024)', fontweight='bold', fontsize=12)
ax3.set_xlabel('Year')
ax3.set_ylabel('Relative Funding Level (%)')
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_ylim(50, 105)

# Add funding cut annotations
ax3.annotate('EPA: -40%', xy=(2024, 60), xytext=(2020, 50),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=9, fontweight='bold', color='red')
ax3.annotate('NIH: -25%', xy=(2024, 75), xytext=(2020, 65),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=9, fontweight='bold', color='red')

# 4. Nanoplastic Detection in Human Tissues
tissues = ['Blood', 'Placenta', 'Stool', 'Breast Milk', 'Brain*']
detection_rates = [100, 100, 100, 75, 60]  # Percentage of samples with detection
colors = ['#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']

bars = ax4.bar(tissues, detection_rates, color=colors, alpha=0.7, edgecolor='black', linewidth=1)
ax4.set_title('Nanoplastic Detection in Human Tissues', fontweight='bold', fontsize=12)
ax4.set_xlabel('Tissue Type')
ax4.set_ylabel('Detection Rate (%)')
ax4.grid(True, alpha=0.3, axis='y')
ax4.set_ylim(0, 110)

# Add percentage labels on bars
for bar, rate in zip(bars, detection_rates):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'{rate}%', ha='center', va='bottom', fontweight='bold')

# Add note for brain data
ax4.text(0.5, 0.02, '*Brain data: Emerging research, limited human studies', 
         transform=ax4.transAxes, ha='center', fontsize=9, style='italic', color='gray')

# Adjust layout and save
plt.tight_layout()
plt.savefig('nanoplastics_charts.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("Charts created successfully! Saved as 'nanoplastics_charts.png'")

# Create additional specialized charts
fig2, (ax5, ax6) = plt.subplots(1, 2, figsize=(16, 6))

# 5. Economic Impact Timeline
economic_years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
autoimmune_costs = [70, 75, 80, 85, 90, 95, 98, 100, 102, 105, 110]  # Billions USD

ax5.plot(economic_years, autoimmune_costs, marker='o', linewidth=3, markersize=8, color='#e377c2')
ax5.fill_between(economic_years, autoimmune_costs, alpha=0.3, color='#e377c2')
ax5.set_title('U.S. Autoimmune Disease Treatment Costs', fontweight='bold', fontsize=14)
ax5.set_xlabel('Year')
ax5.set_ylabel('Cost (Billions USD)')
ax5.grid(True, alpha=0.3)
ax5.set_ylim(60, 120)

# Add cost annotation
ax5.annotate('$110B annually\nby 2025', xy=(2025, 110), xytext=(2020, 95),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=10, fontweight='bold', color='red')

# 6. Policy Timeline
policy_events = ['1973 SPI Memo', '1990s Recycling\nPromotion', '2016 EPA Cuts', '2020 NIH\nReductions', '2024 Global\nPlastics Treaty', '2025 Sept 18\nDeadline']
policy_years = [1973, 1995, 2016, 2020, 2024, 2025]
event_importance = [8, 6, 7, 7, 9, 10]  # Scale 1-10

colors_policy = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

scatter = ax6.scatter(policy_years, event_importance, s=[s*100 for s in event_importance], 
                      c=colors_policy, alpha=0.7, edgecolors='black', linewidth=1)

ax6.set_title('Key Policy Events Timeline', fontweight='bold', fontsize=14)
ax6.set_xlabel('Year')
ax6.set_ylabel('Policy Importance (1-10)')
ax6.grid(True, alpha=0.3)
ax6.set_ylim(0, 12)

# Add event labels
for i, (year, importance, event) in enumerate(zip(policy_years, event_importance, policy_events)):
    ax6.annotate(event, (year, importance), xytext=(5, 5), textcoords='offset points',
                 fontsize=8, ha='left', va='bottom')

plt.tight_layout()
plt.savefig('nanoplastics_policy_charts.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("Policy charts created successfully! Saved as 'nanoplastics_policy_charts.png'") 