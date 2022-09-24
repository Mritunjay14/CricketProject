# CricketProject
TEST CASE 1 : Write a test that validate that team has only four foreign players
TES CASE 2 : Write a test taht valiadet that there is atleast onw wicket keeper

import json
#importing json modules
#once we have the json file in directory we use the library commands to open it
with open('TeamRCB.json') as f:
   data = json.load(f)
   ls=data["player"]   # assigning the values of key==player to an empty list ls
   lts=[]
   ltss=[]
   i=0
   foreigner_count=0
   total_count=0
   counter=0

#inititaing the variables required
#now the idea is to traverse the list ls and find values matching 
#India to count foreign players otherwise
#we simply traverse the values of key==player and find if 
#India is part of them..otherwise directing that player is foreigner
   for x in ls:
      useful = x.values()
      if "India" not in useful:
         foreigner_count=foreigner_count+1
   print ("total count of foreign players:"+str(foreigner_count))


# again traversing the list to find whether role values have wicketkeeper or not.
#increasing the counter evertime wicketkeeper is found in values
   for x in ls:
      usefull = x.values()
      if "Wicket-keeper" in usefull:
         counter=counter+1
# putting condition to check if number is more than 0
#and if it is then what is the count
   if counter>0:
      print("there is atleast one wicketkeeper")
      print("total count of wicketkeepers in list is:" +str(counter))
