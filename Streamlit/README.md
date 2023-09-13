Here, webapp_startup.py is the streamlit web app file visualising the startup india scraped data and basic EDA

To Run this streamlit app on AWS EC2 and without ending server while disconnecting ssh connection
```
  nohup streamlit run yourscript.py
```
To kill the process in your next ssh session
```
    ps aux | grep streamlit  # ps command to find process id
    kill PID
```
    
