import pyttsx3
import os

while True:
  pyttsx3.speak("Welcome Abhishek")

  print()
  p=input("Chat with me : ")
  if ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("notepad" in p or "editor" in p):
   os.system("notepad")
  elif ("run" in p or "execute" in p or "open" in p or  "launch" in p) and ("edge" in p):
   os.system("msedge")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("player" in p):
   os.system("wmplayer")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("zoom" in p or "meeting" in p or "voice call" in p):
   os.system("zoom")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("firefox" in p):
   os.system("firefox")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("IDM" in p or "idm" in p or "downloader" in p or "download manager" in p):
   os.system("idman")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("VSC" in p or "code" in p or "studio code" in p or "download manager" in p):
   os.system("code")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("VM" in p or "virtual" in p or "box" in p or "machine" in p):
   os.system("virtualbox")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("slack" in p or "query" in p or "ask" in p or "lw" in p):
   os.system("slack")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("calculator" in p or "cal" in p or " calci" in p or "calc" in p):
   os.system("calc")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("camera" in p or "chesse" in p or " click" in p or "click" in p):
   os.system("start microsoft.windows.camera:")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("teamviewer" in p or "sharescreen" in p or "help" in p):
   os.system("teamviewer")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("vlc" in p or "videoplayer" in p or "video" in p):
   os.system("vlc")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("archive" in p or "winrar" in p or "zip" in p):
   os.system("winrar")
  elif ("run" in p or "execute" in p or "launch" in p or "open" in p) and ("onedrive" in p or "backup" in p or "cloud" in p):
   os.system("onedrive")
  elif ("facebook" in p):
   os.system("msedge www.facebook.com")
  elif ("linkedin" in p):
   os.system("msedge www.linkedin.com")
  elif ("youtube" in p):
   os.system("msedge www.youtube.com")
  elif ("google" in p):
   os.system("msedge www.google.com")
   break
  elif("exit" in p or "quit" in p):
    exit()
  else:
   pyttsx3.speak("you Please try again")
