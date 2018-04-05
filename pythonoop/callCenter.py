# Create Call Class
class cCall():

    def __init__(self, unique_id, caller_name, caller_phone_num, time_of_call, reason):
        self.id = unique_id
        self.name = caller_name
        self.phone = caller_phone_num
        self.call_time = time_of_call
        self.reason = reason

    def display_all(self):    #  print "ID:", self.unique_id
        print("ID: " + str(self.id))
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("Time of call: " + self.call_time)
        print("Reason: " + self.reason)
        return self

# Create Call Center Class
class callCenter():

    def __init__(self):
        self.calls = []
        self.queue = 0

    def add(self, incall):
        self.calls.append(incall)
        self.queue += 1
        return self

    def remove(self):
        self.calls.pop(0)
        self.queue -=1
        return self

    def removePhone(self, srchnum):
        index = 0
        for x in self.calls:
            if x.phone == srchnum:
                self.calls.pop(index)
                self.queue -= 1
            index += 1
        return self

    def info(self):
        print("There are " + str(self.queue) + " people waiting")
        for x in self.calls:
            print("Name: ", x.name, "Phone: ", x.phone)
            
            
best = callCenter()
caller1 = cCall(32, "Fred", "987-989-9999", "12:30pm", "for a test")
p = caller1.display_all()
best.add(p)
caller2 = cCall(32, "Betty", "987-989-9898", "12:30pm", "for a test")
p = caller2.display_all()
best.add(p)
caller3 = cCall(32, "Betty", "987-989-7777", "12:30pm", "for a test")
p = caller3.display_all()
best.add(p)
caller4 = cCall(32, "Betty", "987-989-9898", "12:30pm", "for a test")
p = caller4.display_all()
best.add(p)
caller5 = cCall(32, "Betty", "987-989-9898", "12:30pm", "for a test")
p = caller5.display_all()
best.add(p)
best.info()
best.remove()
best.info()
best.removePhone("987-989-7777")
best.info()
