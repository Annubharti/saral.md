import requests
#Requests is a Python HTTP library, released under the Apache2 License.
# The goal of the project is to make HTTP requests simpler and more human-friendly.
def request(url):
        resp = requests.get(url)
        return resp.json()


#Now, we have a Response object called resp.
#We can get all the information we need from this object.
#In data1 response is converted into JSON format.

course_json = request("http://saral.navgurukul.org/api/courses")

#we are calling request function by giving paramater of courses url.
id_list= []
# id_list is a varible in which a new list is assigned to store id of the courses.
index = 0
# using while loop to retrive all course_id

while index < len(course_json['availableCourses']):
        course = course_json['availableCourses'][index]
        course_name = course['name']
        #in cousre_name variable I have assigned name of courses which is 
        # available inside availableCourses and inside name of it that too index wise. 
        course_id = course['id']
        # as we are storing course_name in the same way we are storing course_id. 
        print(index,course_name)
        # printed index even so that course_name come along with number wise series.
        id_list.append(course_id)
        #in id_list we are storing all the ids by appendind it inside the loop
        index=index+1
print ("************************************************************************")
choose_course = int(input("Choose the Course number which you want to learn."))


chosen_course = id_list[choose_course]
# jb choose_course id_list ke index number ke barabr ho  to a

exercise_json = request("http://saral.navgurukul.org/api/courses/"+str(chosen_course)+"/exercises")

# Throws error if the retu3rned data is an empty list

slug_list = []
index2 = 0
while index2 < len(exercise_json['data']):
        exercise = exercise_json ['data'][index2]
        parent_exerciseId = exercise['parentExerciseId']
        if parent_exerciseId == None:
                exercise_name = exercise['name']
                exercise_slug = exercise['slug']
                slug_list.append(exercise_slug)
                print (str(index2)+ ". " + exercise_name)
        elif parent_exerciseId != None:
                exercise_name = exercise['name']
                exercise_slug = exercise['slug']
                slug_list.append(exercise_slug)
                print (str(index2)+ ") " + exercise_name)

                index2_1 = 0
                while index2_1 < len(exercise['childExercises']):
                        child_exercise_name = exercise['childExercises'][index2_1]['name']
                        child_exercise_slug = exercise['childExercises'][index2_1]['slug']
                        slug_list.append(child_exercise_slug)
                        print ("\t" + str(index2_1) + ") " + child_exercise_name)
                        index2_1 = index2_1 + 1
        index2 =  index2 + 1

print ("------------------------------------------------------------------------------")
choose_exercise = input("Enter the topic number you want to learn : ")










# import pprint
# pprint.pprint(exercise_json)


#child_exercise = request("http://saral.navgurukul.org/api/courses/"+str(chosen_exercise)+"/exercise/getBySlug?slug=slug=python__WhatDoComputersDo")
