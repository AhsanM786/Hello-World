Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def who_eats_who(zoo):
    whoeatwho = {
    'antelope':('grass'),
    'cow':('grass'),
    'sheep':('grass'),
    'giraffe':('leaves'),
    'panda':('leaves'),
    'bug':('leaves'),
    'chicken':('bug'),
    'big-fish':('little-fish'),    
    'bear':('big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'),        
    'fox':('chicken', 'sheep'),    
    'lion':('antelope', 'cow')    
    }
    survival = zoo.split(",")
    inzoo = zoo.split(",") 
    eats = []
    for x in whoeatwho :
        if x in inzoo:
            for y in inzoo:
                if y in whoeatwho[x]:
                    eats.append((x + ' eats ' + y))
                    survival.remove(y)                    
    eats = eats + survival
    zoo = zoo.split("'") + eats
    return zoo