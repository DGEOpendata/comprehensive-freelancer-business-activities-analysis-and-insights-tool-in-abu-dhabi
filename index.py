python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('DL06-Freelance-Activities-ADRA-OD-010-AFR.csv')

# Display basic information about the dataset
print("Dataset Summary:")
print(data.info())

# Filter for specific activity categories (e.g., consultancy services)
consultancy_services = data[data['English Name'].str.contains('Consultancy', na=False)]

# Count the number of activities per category
activity_counts = data['English Name'].value_counts()

# Plot the top 10 most common activities
activity_counts.head(10).plot(kind='bar', title='Top 10 Freelancer Activities in Abu Dhabi')
plt.xlabel('Activity')
plt.ylabel('Count')
plt.show()

# Export filtered data to a new CSV
consultancy_services.to_csv('Consultancy_Services.csv', index=False)
