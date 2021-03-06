from matplotlib import pyplot as plt
import readFromDatabase as rfd
#Lists used to classify the action
visit = ["visited friends or family for leisure"]
shopping = ["\'special\' shopping for items that you do not regularly buy"]
food = ["went out for a meal", "went on a night out to a bar, pub and/or club"]
entertainment = ["went out for entertainment – to a cinema, concert or theatre",
                "watched live sporting event (not on tv"]
leisure = ["undertook outdoor leisure activities such as walking, cycling, golf, etc.",
            "took part in other leisure activities such as hobbies, evening classes, etc. (outside of your home)",
            "took part in sports, including exercise classes, going to the gym",
            "went to visitor attractions such as a historic house, garden, theme park, museum, zoo, etc.",
            "went on general days out/ to explore an area"]
special_event = ["went to a special public event such as a festival, exhibition, etc.",
                "went to a special event of a personal nature such as a wedding, graduation, christening, etc."]
healthCentre = ["went on days out to a beauty/health centre/spa, etc."]
other = ["went on day trips/excursions for another leisure purpose not mentioned above"]
attributes=['visit friends or family', 'go shopping', 'go for food', 'go for entertainment', 'go for leisure activities',
            'for special event', 'go for health centre', 'other activities']
visitor=['16-24', '25-34', '35-44', '45-54', '55-64', '65+']
select=['visit friends or family', 'go for leisure activities', 'go for food']
#the function used to classify the function
def classifyPurpose(input):
    if input in visit:
        return "visit friends or family"
    elif input in shopping:
        return "go shopping"
    elif input in food:
        return "go for food"
    elif input in entertainment:
        return "go for entertainment"
    elif input in leisure:
        return "go for leisure activities"
    elif input in special_event:
        return "for special event"
    elif input in healthCentre:
        return "go for health centre"
    else:
        return "other activities"
#To show the relation between age and purpose
purpose_data = rfd.readAction('action', 'activity', 'age')
purpose_data['Action'] = purpose_data['Action'].apply(lambda x:classifyPurpose(x))
all_year_purpose = purpose_data.groupby(['Year', 'Action']).sum().reset_index()
plt.figure(figsize=(8, 8))
#Select the data from dataframe based on action.
visitData=all_year_purpose[(all_year_purpose['Action']=='visit friends or family')]
shoppingData=all_year_purpose[(all_year_purpose['Action']=='go shopping')]
foodData=all_year_purpose[(all_year_purpose['Action']=='go for food')]
entertainmentData=all_year_purpose[(all_year_purpose['Action']=='go for entertainment')]
leisureData=all_year_purpose[(all_year_purpose['Action']=='go for leisure activities')]
speicalData=all_year_purpose[(all_year_purpose['Action']=='for special event')]
healthCentreData=all_year_purpose[(all_year_purpose['Action']=='go for health centre')]
otherData=all_year_purpose[(all_year_purpose['Action']=='other activities')]
#Draw the line chart to show the trend of visitors for differnet purposes
plt.plot(visitData['Year'], visitData['Count'], marker='o', linewidth=3)
plt.plot(shoppingData['Year'], shoppingData['Count'], marker='o', linewidth=3)
plt.plot(foodData['Year'], foodData['Count'], marker='o', linewidth=3)
plt.plot(entertainmentData['Year'], entertainmentData['Count'], marker='o', linewidth=3)
plt.plot(leisureData['Year'], leisureData['Count'], marker='o', linewidth=3)
plt.plot(speicalData['Year'], speicalData['Count'], marker='o', linewidth=3)
plt.plot(healthCentreData['Year'], healthCentreData['Count'], marker='o', linewidth=3)
plt.plot(otherData['Year'], otherData['Count'], marker='o', linewidth=3)
plt.legend(attributes)
plt.xlabel('Years', fontsize=15, weight='bold')
plt.ylabel('Visitors(Million)', fontsize=15, weight='bold')
plt.title('Overall Trend of Visitors for Different Purpose', fontsize=15, weight='bold')
plt.xlim(2011, 2019)
plt.ylim(0, 110)
plt.xticks(fontsize=12, weight='bold')
plt.yticks(fontsize=12, weight='bold')
plt.savefig('overAllPurpose.png')
plt.show()
#Calculate the sum of visitors who took different actions in recent 10 years.
component=all_year_purpose.groupby('Action').sum().reset_index()
plt.figure(figsize=(8, 8))
plt.pie(component['Count'], autopct='%0.1f%%', explode=(0, 0, 0.05, 0, 0.05, 0, 0, 0.05))
plt.legend(component['Action'], fontsize=12)
plt.title('The Composition of Visitors for Different Purpose', fontsize=15, weight='bold')
plt.savefig('compositionPurpose.png')
plt.show()
#plt.figure(figsize=(8, 8))
#The age distribution for different purposes
component=purpose_data.groupby(['Action', 'Attribute']).sum().reset_index()
for i in range(1, len(select)+1):
    ax=plt.subplot(3, 1, i)
    tem = component[component['Action'] == select[i - 1]]
    plt.bar(tem['Attribute'], tem['Count'])
    ax.set_title(select[i-1])
    plt.xlabel('Age', weight='bold')
    plt.ylabel('Visitors(Million)')
#plt.savefig('ageDistribution.png')
plt.show()

#To show the relation between purpose and if the visitors has cars
purpose_data = rfd.readAction('action', 'activity', 'cars')
purpose_data['Action'] = purpose_data['Action'].apply(lambda x:classifyPurpose(x))
#Calculate the sum of visitors who took different actions in recent 10 years.
component=purpose_data.groupby(['Action', 'Attribute']).sum().reset_index()
#The car holders distribution for different purposes
plt.figure(figsize=(10, 10))
for i in range(1, len(attributes)+1):
    ax=plt.subplot(4, 2, i)
    tem = component[component['Action'] == attributes[i - 1]]
    plt.bar(tem['Attribute'], tem['Count'])
    plt.title('The Distribution of Car Holder on \"'+attributes[i-1]+'\"', weight='bold')
    plt.xlabel('Car Holder', weight='bold')
    plt.ylabel('Count(Million)', weight='bold')
    plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.savefig('carHolderDistribution.png')
plt.show()


#To show the relation between purpose and the gender of visitors
purpose_data = rfd.readAction('action', 'activity', 'gender')
purpose_data['Action'] = purpose_data['Action'].apply(lambda x:classifyPurpose(x))
#Calculate the sum of visitors who took different actions in recent 10 years.
component=purpose_data.groupby(['Action', 'Attribute']).sum().reset_index()
#The car holders distribution for different purposes
plt.figure(figsize=(10, 10))
for i in range(1, len(attributes)+1):
    ax=plt.subplot(4, 2, i)
    tem = component[component['Action'] == attributes[i - 1]]
    plt.bar(tem['Attribute'], tem['Count'])
    plt.title('The Distribution of Gender on \"'+attributes[i-1]+'\"')
    plt.xlabel('Gender')
    plt.ylabel('Number of Visitors(Million)')
    plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.savefig('genderDistribution.png')
plt.show()


#To show the relation between purpose and the married status of visitors
purpose_data = rfd.readAction('action', 'activity', 'married')
purpose_data['Action'] = purpose_data['Action'].apply(lambda x:classifyPurpose(x))
#Calculate the sum of visitors who took different actions in recent 10 years.
component=purpose_data.groupby(['Action', 'Attribute']).sum().reset_index()
#The car holders distribution for different purposes
plt.figure(figsize=(10, 10))
for i in range(1, len(attributes)+1):
    ax=plt.subplot(4, 2, i)
    tem = component[component['Action'] == attributes[i - 1]]
    plt.bar(tem['Attribute'], tem['Count'])
    plt.title('The Distribution of Married Visitors on \"'+attributes[i-1]+'\"')
    plt.xlabel('Married')
    plt.ylabel('Number of Visitors(Million)')
    plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.savefig('marriedDistribution.png')
plt.show()


#To show the relation between purpose and the social grades of visitors
purpose_data = rfd.readAction('action', 'activity', 'social')
purpose_data['Action'] = purpose_data['Action'].apply(lambda x:classifyPurpose(x))
#Calculate the sum of visitors who took different actions in recent 10 years.
component=purpose_data.groupby(['Action', 'Attribute']).sum().reset_index()
#The car holders distribution for different purposes
plt.figure(figsize=(10, 10))
for i in range(1, len(attributes)+1):
    ax=plt.subplot(4, 2, i)
    tem = component[component['Action'] == attributes[i - 1]]
    plt.bar(tem['Attribute'], tem['Count'])
    plt.title('The Distribution of Social Grades on \"'+attributes[i-1]+'\"')
    plt.xlabel('Social Grade')
    plt.ylabel('Number of Visitors(Million)')
    plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.savefig('socialDistribution.png')
plt.show()


#To show the relation between purpose and the working status of visitors
purpose_data = rfd.readAction('action', 'activity', 'working')
visitor=['employed', 'in education', 'unemployed']
#Add a column named total to show the number of people who took different type of actions.
purpose_data['Action'] = purpose_data['Action'].apply(lambda x:classifyPurpose(x))
#Calculate the sum of visitors who took different actions in recent 10 years.
component=purpose_data.groupby(['Action', 'Attribute']).sum().reset_index()
#The car holders distribution for different purposes
plt.figure(figsize=(10, 10))
component=component.drop(['Year'], axis=1)
for i in range(1, len(attributes)+1):
    ax=plt.subplot(4, 2, i)
    tem = component[component['Action'] == attributes[i - 1]]
    plt.bar(range(len(tem['Attribute'])), tem['Count'])
    ax.set_xticks(range(len(tem['Attribute'])))
    ax.set_xticklabels(visitor)
    plt.title('The Distribution of Working Status on \"'+attributes[i-1]+'\"')
    plt.xlabel('Working Status')
    plt.ylabel('Number of Visitors(Million)')
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.savefig('workingDistribution.png')
plt.show()

#To show the relation between purpose and the working status of visitors
purpose_data = rfd.readAction('action', 'activity', 'children')
purpose_data['Action'] = purpose_data['Action'].apply(lambda x:classifyPurpose(x))
#Calculate the sum of visitors who took different actions in recent 10 years.
component=purpose_data.groupby(['Action', 'Attribute']).sum().reset_index()
#The car holders distribution for different purposes
plt.figure(figsize=(10, 10))
component=component.drop(['Year'], axis=1)
for i in range(1, len(attributes)+1):
    ax=plt.subplot(4, 2, i)
    tem = component[component['Action'] == attributes[i - 1]]
    plt.bar(tem['Attribute'], tem['Count'])
    plt.title('The Distribution of Visitors with Children on \"'+attributes[i-1]+'\"')
    plt.xlabel('Having Children')
    plt.ylabel('Number of Visitors(Million)')
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.savefig('childrenDistribution.png')
plt.show()