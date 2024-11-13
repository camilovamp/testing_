# Used Vehicle Market Web Application

Description of the project:
This project aims to understand the relationship between data and how to implement and present data on a web platform using Python and Streamlit. We aim to display a few analyses of the used vehicle markets of the world's leading vehicle manufacturers while simulating multiple data points on a web platform. 

To implement this project few a key libraries were necessary such as Streamlit and Ploty.express, Pandas Library, and Altair. 

To implement this project on your local machine, a few requirements must be satisfied:

1. A GitHub account is a requirement to be able to connect to online services such as Render in our case. Furthermore, a render account is needed to be able to host your application web browser. Render offers a free subscription service level which is more than enough for this project, but feel free to upgrade if you wish. 

2. Within your director, a few files are needed to execute this project. First and foremost, you need an app.py file which will contain your code for the application building, you will also need a database of your choosing as long as it's in CSV format. Additionally, you will need to create a file called requirement.txt which will have all the libraries listed within so the application can use the library. Lastly, you will need a configuration directory with your directory, and this this direct must be called .streamlit, and within this directory, you will create a file called config.toml.


To effectively run this app effectively, there several key compponent on how to set up the repository. Within the repository, you will find a Jupyter noteboo director with file called EDA.ipynb containing foundational analysis of the data and explored some potential visualization that can implemented. The repository also contains .stream file and requirements.txt file; both of which are important file to be able to run the application as the file contains service configeration and  important package the applicatio will need to operate. You will also find the app.py file containing the Python code for the application. 

To host web application online, fork the project to your own Github account so you can connect render to your GitHub. Sign up for render account with your Github account containing the project repository, once this step is complete, your ready to deploy on render. 

To delpoy on render, click on new web service:
1. In the **Build Command** section,  add `pip install streamlit & pip install -r requirements.txt`
2. In the **Start Command** section, add `streamlit run app.py'
3. Click the button the bottom to launch the application
After it’s finished, you can open the application URL at `https://{APP_NAME}.onrender.com` or by clicking the URL on the top of deloying page in render. This should open the application on your web browser.

# Conclusion
This project offered a foundation understanding on the dataset vehicle_us.csv and ultize modern web service deployment through render. We were able to deploy web application with render and perform foundamental analysis on the used vehicles market data. 