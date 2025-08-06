def chatbot(user):
  
  if user == "hello":
        return "hi"
   
  elif user == "how are you":
        return "i am fine,thanks"
   
  elif user== "bye":
      return "goodbye"
   
  else:
      return "sorry i don't understand"
  
print("type 'hello' to start the chat type 'bye'to exit")
while True:
   print("welcome user")
   user =input("user: ")
   reply = chatbot(user)
   print("chatbot:",reply) 
   
  
  
  
  

 

  

 
