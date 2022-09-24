
import json

with open('TeamRCB.json') as f:
   data = json.load(f)
   ls=data["player"]
   lts=[]
   ltss=[]
   i=0
   foreigner_count=0
   total_count=0
   counter=0

   for x in ls:
      useful = x.values()
      if "India" not in useful:
         foreigner_count=foreigner_count+1
   print ("total count of foreign players:"+str(foreigner_count))

   for x in ls:
      usefull = x.values()
      if "Wicket-keeper" in usefull:
         counter=counter+1

   if counter>0:
      print("there is atleast one wicketkeeper")
      print("total count of wicketkeepers in list is:" +str(counter))









