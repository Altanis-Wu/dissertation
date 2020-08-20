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

attributes=['visit friends or family', 'go for food', 'go for leisure activities',]
#Read data from database
purposeData = rfd.readFrom('action', 'activity')
#List used to classify visitors and draw the figures.
age=['16-24', '25-34', '35-44', '45-54', '55-64', '65+']
cars=['access to car (1+)', 'no access to car (0)']
children=['yes', 'no']
gender=['male', 'female']
married=['married', 'not married']
social=['ab', 'c1', 'c2', 'de']
working=['employed/self-employed (full or part time)',
         'in full or part time education', 'unemployed/not working']
columns=[age, cars, children, gender, social, working, married]
visitorType=['age', 'cars', 'children', 'gender', 'social', 'working', 'married']
purposeData['Action'] = purposeData['Action'].apply(lambda x:classifyPurpose(x))
#Group the based on action as the detailed 15 actions are classified into 8 actions.
purposeData=purposeData.groupby(['Year', 'Action', 'Visitor', 'Attribute']).sum().reset_index()

def classify(x):
    if x=='employed/self-employed (full or part time)':
        return 'working'
    elif x=='in full or part time education':
        return 'education'
    elif x=='unemployed/not working':
        return 'unemployed'
    else:
        return x
#Draw the figures for each action
for action in attributes:
    for i in range(len(visitorType)):
        data=purposeData[(purposeData['Visitor']==visitorType[i]) & (purposeData['Action']==action)].groupby(['Action', 'Attribute']).sum().reset_index()
        data['Attribute']=data['Attribute'].apply(lambda x: classify(x))
        plt.bar(data['Attribute'], data['Count'])
        plt.title('\"' + action + '\" and ' + visitorType[i], fontsize=15, weight='bold')
        plt.xlabel('Visitor', fontsize=15, weight='bold')
        plt.ylabel('Count(Million)', fontsize=15, weight='bold')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.savefig(visitorType[i] + '/' + action + '_' + visitorType[i] + '.png')
        plt.show()