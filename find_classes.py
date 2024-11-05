import json 
SKIP = "$SKIP$"
SPACE = " "


class Student():
    def __init__(self, completed_path): 
        with open(completed_path, 'r') as f:
            self.completed = json.loads(f.read())
        # self.all_prereqs_that_exist = {} this is for the initial creatiuon of the prereqs list

    def prereqs_met(self, class_object):
        for group in class_object['prerequisite']:
            if SKIP in group: # Case for when there is a longer, non-class prerequisite. 
                group = group[len(SKIP):]
                if group not in self.completed:
                    return False
                 
            elif SPACE not in group and group.strip() not in self.completed: # Case when there's no "or" condition and you didn't do the prereq
                # self.all_prereqs_that_exist[group] = self.all_prereqs_that_exist.get(group, 0) + 1
                return False 

            elif SPACE in group: # Case for when there an "or", you just check if any of them are satisfied
                # for req in group.split(" "): 
                #    self.all_prereqs_that_exist[req] = self.all_prereqs_that_exist.get(req, 0) + 1
                if not any([x in self.completed for x in group.split(" ")]):
                    return False
        return True
            

def main(): 
    # Pull the course data and completed list into memory 
    with open('data/courses.json', 'r') as c:
        courses = json.loads(c.read())
    with open('data/reqs.json', 'r') as r: 
        reqs = json.loads(r.read())

    student = Student('data/completed.json')
    
    # Find courses that work
    available_courses = []
    for course in reqs: 
       if student.prereqs_met(course):
           available_courses.append(course)
    print(available_courses)

    # Create a file of all the prereqs that exist
    #with open('data/all_reqs.json', 'w') as f:
    #    f.write(str(student.all_prereqs_that_exist))
       #print("prereq met!!!")




if __name__ == "__main__":
    main()
