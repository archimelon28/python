class Data:
    def myFunc():
        skill = ['Coding','Eat','Sleep','Study']
        for x in skill:
            print("To do list : " + x)
        print("New list?")
        x = input()
        skill.append(x)
        print(skill)
    myFunc()