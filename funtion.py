#There are two ypes of number 
  # Perform an tasks
  # Retern values

def getGreeting(name):
    return f"Hi {name}"

msg = getGreeting("Hello Dushan")
file = open("content.txt", "w")
file.write( msg)