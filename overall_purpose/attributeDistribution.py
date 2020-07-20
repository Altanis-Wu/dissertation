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

attributes=['visit friends or family', 'go shopping', 'go for food', 'go for entertainment', 'go for leisure activities',
            'for special event', 'go for health centre', 'other activities']
purposeData = rfd.readFrom('action', 'activity')
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
for action in attributes:
    for i in range(len(columns)):
        plt.figure(figsize=(8, 8))
        data = purposeData[(purposeData['Visitor']==visitorType[i]) & (purposeData['Action']==action)]
        for column in columns[i]:
            plt.plot(data[data['Attribute'] == column]['Year'], data[data['Attribute'] == column]['Count'], marker='o')
        plt.legend(columns[i])
        plt.title('\"' + action + '\" and ' + visitorType[i])
        plt.xlabel('Year')
        plt.ylabel('Count(Million)')
        plt.savefig(visitorType[i] + '/' + action + '_' + visitorType[i] + '.png')
        plt.show()
