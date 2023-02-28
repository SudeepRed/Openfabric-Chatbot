## Steps to test
1. Download the pre-trained model from [drive](https://drive.google.com/drive/folders/1OBRAIGMLTM6rckZLY-0vmKPsWeu2JUOn?usp=share_link)
2. Now place this folder in the project root directory
3. make sure you have `poetry 1.1.x` installed
    1. `pip install poetry==1.1.15`
5. run `poetry install` to install all dependencies from `poetry.lock` file, which are required to run the app.
6. to run locally run `sh start.sh`
7. to run using docker
    1. first build the image using `docker build -t chatbot .`
    2. next, run `docker run -p 3000:5000 chatbot`
    3. your app is running on `localhost:3000`

![example api](https://github.com/SudeepRed/Openfabric-Chatbot/blob/main/Screenshot%20from%202023-02-28%2005-45-47.png)
## Project Requirements
The current project has the blueprint structure of an AI App. 

Your mission is to implement an 💬NLP chatbot **answering questions about science**. 

You will add your logic to the `main.py` file inside the `execute` function. 
```python
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:        
        response = '' # <<< --Your magic goes here
        output.append(response)

    return SimpleText(dict(text=output))
```
## Constraints and restrictions
You are free to use any package or library you see feet as long as you follow these rules:
* 👎 You can't call any external service (e.g. chatGPT) 
* 👎 You can't copy and paste from other peoples work 

## Run
The application can be executed in two different ways:
* locally by running the `start.sh` 
* on in a docker container using `Dockerfile` 
