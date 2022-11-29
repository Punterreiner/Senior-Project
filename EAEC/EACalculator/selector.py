from .data import data, actions, action_description, charities, charity_description, water



class Selector(object):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, age, spare_money, free_time, fitness, near_water):
        self.age = age
        self.spare_money = spare_money
        self.free_time = free_time
        self.fitness = fitness
        self.near_water = near_water
        
    def profileSelector(self, age, spare_money, free_time, fitness):
        points = Selector.agePoints(int(age)) + Selector.moneyPoints(int(spare_money)) + Selector.ftPoints(int(free_time)) + Selector.fPoints(fitness)
        if points <= 6:
            profile = 0
        elif points <= 11:
            profile = 1
        elif points <= 16:
            profile = 2
        elif points <= 22:
            profile = 3
        return profile

    def agePoints(age):
        ap = 0
        if age <= 18:
            ap = 1
        elif (age > 18 & age < 26) or (age > 45):
            ap = 2
        elif age > 26 & age < 45:
            ap = 3 
        return ap

    def moneyPoints(sm):
        mp = 0
        if sm < 50:
            mp = 0
        elif sm < 250:
            mp = 2
        elif sm < 500:
            mp = 4
        elif sm < 1000:
            mp = 6
        elif sm < 2500:
            mp = 8
        elif sm >= 2500:
            mp = 10
        return mp

    def ftPoints(ft):
        ftp = 0
        if ft < 5:
            ftp = 0
        elif ft < 10:
            ftp = 1
        elif ft < 14:
            ftp = 2
        elif ft < 20:
            ftp = 4
        elif ft >= 20:
            ftp = 6
        return ftp

    def fPoints(f):
        fp = 0
        if f == 'poor':
            fp = 0
        elif f == 'ok':
            fp = 1
        elif f == 'good':
            fp = 2
        elif f == 'excellent':
            fp = 3
        return fp

class dataPicker(object):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, profile, near_water):
        self.profile = profile
        self.near_water = near_water
    
    def selectActions(profile, near_water):
        actselections = {}
        acts = actions.get(profile)
        for act in acts:
            desc = action_description.get(act)
            actselections.update({act:desc})
        if near_water == 'yes':
            actselections.update({'Water Cleanup': water})
        return actselections

    def selectCharities(profile):
        charselections = {}
        for i in range(profile + 1):
            chars = charities.get(i)
            for char in chars:    
                desc = charity_description.get(char)
                charselections.update({char:desc})
            chars = tuple()
        return charselections
    
    def Merge(dict1, dict2):
        res = {**dict1, **dict2}
        return res

    def getTable(self, profile, near_water):
        AS = dataPicker.selectActions(profile, near_water)
        CS = dataPicker.selectCharities(profile)
        table = dataPicker.Merge(AS, CS)
        return table
