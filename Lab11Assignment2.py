import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('recruitment_data.csv')

companies = data['Company']
recruitments = data['Recruitments']

plt.figure(figsize=(10,5))
plt.bar(companies, recruitments, color='skyblue')
plt.title('New Recruitments in Companies')
plt.xlabel('Companies')
plt.ylabel('Number of Recruitments')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(7,7))
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title('Recruitment Distribution')
plt.show()

colors = ['gold','lightcoral','lightskyblue','yellowgreen','pink','cyan','orange','violet']
explode = [0.1 if c == 'IBM' or c == 'Amdocs' else 0 for c in companies]

plt.figure(figsize=(7,7))
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', colors=colors, explode=explode, shadow=True, startangle=140)
plt.title('Customized Pie Chart')
plt.show()

plt.figure(figsize=(7,7))
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Doughnut Chart')
plt.show()

ibm_value = data[data['Company'] == 'IBM']['Recruitments'].values[0]
amdocs_value = data[data['Company'] == 'Amdocs']['Recruitments'].values[0]

plt.figure(figsize=(6,5))
plt.bar(['IBM','Amdocs'], [ibm_value, amdocs_value], color=['blue','green'])
plt.title('IBM vs Amdocs Recruitments')
plt.ylabel('Number of Recruitments')
plt.show()
