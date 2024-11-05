import json 
def main(): 
    # Pull both of them into memory 
    with open('data/courses.json', 'r') as c:
        courses = json.loads(c.read())
    with open('data/reqs.json', 'r') as r: 
        reqs = json.loads(r.read())

    # Check 
    print(courses) 
    print(reqs) 


if __name__ == "__main__":
    main()
