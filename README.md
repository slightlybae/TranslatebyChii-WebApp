# AI-Web-App-using-Flask-and-Python
This AI Translation Web App is built with Flask Framework and Python         
This web app can translate up to 15 different Languages

## Sevices Employed
Azure Translator Service     
   This service, is part of Azure Cognitive Services, which will translate to and from dozens of languages. It can automatically detect the source language, and can translate to multiple target languages in one call.

## How to use
#### Write the word/text you want to translate, then select your preferred language and click on Translate
![Screenshot (32)](https://user-images.githubusercontent.com/45470819/221436668-1d9d5779-eaa0-4811-81fa-d96b4c50b7f3.png)

#### Your translated text is shown here.
![Screenshot (33)](https://user-images.githubusercontent.com/45470819/221436672-723c134f-0729-44f1-96a9-553b5730a53f.png)

#### Test the App
https://translatebychii.azurewebsites.net/

## Languages and Framework
> Python

> Html

> Flask & Bootstrap



## Software and Application Used
1. Install Visual Studio Code
Visual Studio Code is an open-source code editor that allows you to create almost any type of application you might like
[Install visual Studio](https://code.visualstudio.com)

2. Install Python
 Install Python 3.6 or later installed on your computer.
 [Install Python](https://learn.microsoft.com/en-us/training/modules/python-install-vscode/3-exercise-install-python3)

3. Create a directory for your code
  Create a directory in the location of your choice. This directory will be your project directory, and will contain all of the code we'll create. You can create a directory from a command or terminal window with one of the following commands:
  ## Windows
 ```
  md contoso
  cd contoso
```

  ## macOS or Linux
 ```  
   mkdir contoso
   cd contoso
```
4. Create a virtual environment
   Use the following commanads
  ## Windows
```
Create the environment
    python -m venv venv
Activate the environment
    .\venv\scripts\activate
```

  ## macOS or Linux
```
Create the environment
   python -m venv venv

Activate the environment
   source ./venv/bin/activate
 ```

5. Install Flask and other libraries
  1. In the command or terminal window, run the following command to open the directory in Visual Studio Code
  ``` 
  code .
  ```
  2. In Visual Studio Code, in the Explorer window, select New File next to the contoso directory

  3. Name the file requirements.txt, and add the following text:
  ```
    flask
    python-dotenv
    requests
 ```
   4. save the file

   5. Return to the command or terminal window and perform the installation by using pip to run the following command:
     > pip install -r requirements.txt  


For more infromation on how to buid an AI Web App using Flask and Python
[Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/python-flask-build-ai-web-app/?wt.mc_id=studentamb_85181) 
