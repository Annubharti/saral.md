import requests
# Requests is a Python HTTP library, released under the Apache2 License.
# The goal of the project is to make HTTP requests simpler and more human-friendly.
<<<<<<< HEAD
BASE_URL = "http://saral.navgurukul.org/api/courses" # Global variable storing api
=======

BASE_URL = "http://saral.navgurukul.org/api/courses" # GLobal Varibale to store api through which gives courses

def request(url):
        '''
        takes a string input which is the url being fetched
        returns the json request after making a get request from the api
        '''
        resp = requests.get(url)
        return resp.json()
>>>>>>> 11dfb6dc71dc93e8183b3f695e09c21958af70d5

courses = [] # Global Variable to store all the courses details
current_course_id = 0
course_exercises = [] # Global Variable to store the exercise for a particular course
current_exercise_slug = ""
course_content = '''Course Content Here'''

<<<<<<< HEAD
def request(url, params = {}):
  resp = requests.get(url)
  return resp.json()
=======
course_json = request(BASE_URL)

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

exercise_json = request(BASE_URL +str(chosen_course)+"/exercises")

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
>>>>>>> 11dfb6dc71dc93e8183b3f695e09c21958af70d5

def space():
  print ("\n\n-----------------------------------------------------\n\n")
  #function for some space between two hea topics.

print ("************************  WELCOME  TO  SARAL  *************************************")

course_json = request(BASE_URL) 
#we are calling request function by giving paramater of courses url.
while True:
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

  space()

  def choose_course():
    user_choice = int(input("Choose the Course number which you want to learn.\n\n Your answer : "))
    chosen_course = id_list[user_choice]
    # jb choose_course id_list ke index number ke barabr ho  to a
    return chosen_course

  courses = choose_course()
  space()
  exercise_json = request(BASE_URL+'/'+str(courses)+"/exercises")
  exercises =(exercise_json)
  slug_list = []

  # Throws error if the returned data is an empty list
  def get_exercise():
    index2 = 0
    while index2 < len(exercise_json['data']):
      exer = exercise_json ['data'][index2]
      parent_exerciseId = exer['parentExerciseId']
      if parent_exerciseId == None:
        exercise_name = exer['name']
        exercise_slug = exer['slug']
        slug_list.append(exercise_slug)
        print (str(index2)+ ". " + exercise_name)
      elif parent_exerciseId != None:
        exercise_name = exer['name']
        exercise_slug = exer['slug']
        slug_list.append(exercise_slug)
        print (str(index2)+ ") " + exercise_name)

        index2_1 = 0
        while index2_1 < len(exer['childExercises']):
          child_exercise_name = exer['childExercises'][index2_1]['name']
          child_exercise_slug = exer['childExercises'][index2_1]['slug']
          slug_list.append(child_exercise_slug)
          print ("\t" + str(index2_1) + ") " + child_exercise_name)
          index2_1 = index2_1 + 1
      index2 = index2 + 1
  space()


  get_exercise()
  space()

  def get_slug(url,params):
    get= requests.get(url, params=params)
    response= get.json()
    return response
  slug_url= BASE_URL+"/"+str(courses)+"/exercise/getBySlug"

  slug_response=get_slug(slug_url,{'slug': slug_list[0]})
  print (slug_response['content'])



  def get_content_from_slug():
    index3=0
    while True:
      choose_exercise= str(input("Enter 'n' to go to next exercise or 'p' to go to previous exercise or to exit enter any key :- "))

      if choose_exercise == "n" and index3 < len(slug_list)-1:
        slug_response=get_slug(slug_url,{'slug': slug_list[index3+1]})
        print (slug_response['content'])
        index3 = index3 + 1
      elif choose_exercise == "p" and index3 >0:
        slug_response= get_slug(slug_url,{'slug': slug_list[index3-1]})
        print (slug_response['content'])
        index3 = index3-1

      elif choose_exercise=="n" and index3==len(slug_list)-1:
        slug_response= get_slug(slug_url,{'slug': slug_list[index3]})
        print (slug_response['content'])
        print ("\n\nNo More Next Exercise.\n")
        
        


      elif choose_exercise=="p" and index3== 0:
        slug_response= get_slug(slug_url,{'slug': slug_list[index3]})
        print (slug_response['content'])

        print ("\n\nNo More Previous Exercise\n")

      else:
        print ("\n\n---------------------You choose exit.------------------------------------\n\n")
        break


  get_content_from_slug()
  exit = input("Enter 'h' to go back to courses or enter any key to exit :-")
  space()
  if exit == "h" or exit == " H":
    continue
  else:
    print ("\n\n-------------------- You Choose to exit. -------------------------------\n\n")
    break

  # import pprint
  # pprint.pprint(exercise_json)
  '''pprint is a predefined function that is used to print whole dictonary and its childs.'''