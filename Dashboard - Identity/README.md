# Dashboard-Identity

This project is a Dash-based interactive dashboard that displays data and generates HTML reports.

## How to Run:

https://hnc25.pythonanywhere.com/

## Details of scope

## Header: Identity Insights and Reporting Dashboard Requirements

Overview: 

The Identity Reporting Dashboard in Connect 2.0 is designed to provide clients with actionable insights into their audience universe and unique reach across various channels. The reporting experience allows users to select a time range (1 Month, 3 Months, or 6 Months) and view dynamically updated metrics, graphs, and visualizations.
________________________________________
Goals
1.	Business Goal 1: How many unique individuals and households exist in my universe?
2.	Business Goal 2: How much unique reach do I have across my owned marketing channels?
3.	Business Goal 3: How much unique reach do I have in Epsilon’s digital channels?
________________________________________
Shared User Experience
1.	Navigation: Users access the dashboard by navigating to:
Reports → Identity Reporting
2.	Time Range Selection:
o	Dropdown menu at the top of the page allows users to select a reporting period: 
	1 Month
	3 Months
	6 Months
3.	Dynamic Refresh:
o	Metrics, graphs, and visualizations update automatically when a new time range is selected.
4.	Export Capability:
o	Users can export metrics as: 
PDF: For sharing visual insights.
CSV: For deeper analysis and external reporting.
________________________________________
Total Profiles
Description
Displays the total number of audience profiles ingested into the system, along with matched individuals and households, accounting for duplication.
Business Goal
How many unique individuals and households exist in my universe?
Metrics Displayed
Metric	Value	Description
Total Profiles	Dynamic	Total number of audience profiles ingested.
Matched csCoreID	Dynamic	Total unique individuals matched (de-duplicated).
Matched csHHId	Dynamic	Total unique households matched.
Duplicate Records	Dynamic (%)	Percentage of duplicate records in the system.
User Experience
•	Metrics are displayed in individual tiles for clarity.
•	Each tile dynamically updates based on the selected time range.
________________________________________
Channel Distribution
Description
Breaks down the total audience reach across owned marketing channels (Address, Email, and Phone) and highlights unique reach percentages.
Business Goal
How much unique reach do I have across my owned marketing channels?
Metrics Displayed
Channel	Total Identifiers	Unique Identifiers	Unique Channel Reach (%)
Address	Dynamic	Dynamic	Dynamic
Email	Dynamic	Dynamic	Dynamic
Phone	Dynamic	Dynamic	Dynamic
Visualizations
1.	Bar Graph 1: Total Identifiers vs Unique Identifiers
o	Compares total audience counts to de-duplicated unique counts for each channel.
o	Bars are grouped side by side for easy comparison.
o	Values are displayed above each bar.
2.	Bar Graph 2: Unique Channel Reach (%)
o	Displays the percentage of unique identifiers relative to total identifiers for each channel.
o	Values (percentages) are displayed above each bar.
________________________________________
CoreID Match Reach
Description
Highlights audience reach in Epsilon's digital channels by showing match rates, actual reach, and performance percentages.
Business Goal
How much unique reach do I have in Epsilon's digital channels?
Metrics Displayed
Metric	Value	Description
Total Profiles	Dynamic	Total audience profiles available for matching.
Matched CoreID	Dynamic	Profiles successfully matched to CoreIDs.
CoreID Match Rate	Dynamic (%)	Formula: Matched CoreID ÷ Total Profiles.
Actual Reach	Dynamic	Number of matched profiles successfully reached.
Reach Rate	Dynamic (%)	Formula: Actual Reach ÷ Matched CoreID.
Visualizations
1.	Odometer Gauge 1: CoreID Match Rate
o	Displays the percentage of profiles matched to CoreIDs.
2.	Odometer Gauge 2: Reach Rate
o	Displays the percentage of matched CoreIDs successfully reached.
Layout:
•	Gauges are displayed side by side for easy comparison.
•	Percent signs (%) are displayed next to the numeric values.
________________________________________
Dynamic Data Aggregation
•	All data (metrics, graphs, and visualizations) dynamically updates based on the selected time range: 
o	1 Month
o	3 Months
o	6 Months
________________________________________
User Flow
1.	Step 1: Navigate to Reports → Identity Reporting.
2.	Step 2: Select a time range (1, 3, or 6 months) using the dropdown menu.
3.	Step 3: View the following sections: 
o	Total Profiles: Tiles displaying dynamic audience metrics.
o	Channel Distribution: 
	Bar Graph 1: Total Identifiers vs Unique Identifiers.
	Bar Graph 2: Unique Channel Reach (%).
o	CoreID Match Reach: 
	Two odometer-style gauges for CoreID Match Rate and Reach Rate.
4.	Step 4: Export the report as PDF or CSV.
