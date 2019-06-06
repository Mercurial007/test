# Run database and application in minikube

## Process

### Step 1:-  Created a Python web application by using flask framework to connect to my database to fetch the info "Hello World" from MySQL Database
 Note: Once you run the application you'll get the url like #http://localhost:5000 it will display the content inside the db table.
 
### Step 2:- Created a docker file which contains serveral commands to install required plugins and, made an entry point to python application code. I.e like a monolithic application as this API call will connect to DB and provide the result.
 Note: Please refer dockerfile to deploy application into the image.

### Step 3: Run the below command to build an image
      #docker build -t your-image-id .

### Step 4: If you want to test locally in your docker before deploying into kubernetes, Please run below command
      #docker run --name flaskapp2 -v$PWD:/app -p5000:5000 your-image-id:tag
      
### Step 5: Please refer deployment.yml and service.yml to deploy in kubernetes
      #kubectl create -f deployment.yml
      #kubectl create -f service.yml
 Note: Actually, I have used service network as node port that's why it'd provide random port numbers from 30000-36000
 
## Conclusion
As per the test case, I have provided all the files including docker file, application code file, readme file except heml file. I've not exploring at this moment on helm due to time constaint. Thanks for giving this opportunity and kindly provide the feedback.

