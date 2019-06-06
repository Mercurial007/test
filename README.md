# Run database and application in minikube

## Process flow

### Step 1:-  Created a Python web application by using flask framework to connect to my database to fetch the info "Hello World" from MySQL Database
 Note: Once you run the application you'll get the url like #http://localhost:5000 it will display the content inside the db table.
 
### Step 2:- Created a docker file which contains serveral commands to install required plugins and, made an entry point to python application code. I.e like a monolithic application as this API call will connect to DB and provide the result.
 Note: Please refer dockerfile to deploy application into the image.

### Step 3: Run the below command to build an image
      #docker build -t your-image-id .

### Step 4: If you want to test locally in your docker before deploying into kubernetes, Please run below command
      #docker run --name flaskapp2 -v$PWD:/app -p5000:5000 your-image-id:tag
      
### Step 5: Please refer deployment.yml and service.yml to deploy in kubernetes
      #kubectl create -f pod-service.yaml

## Conclusion
As VTX is not eabled in my laptop/desktop, i am unable to launch minikube tool. So that, I have implemented in kubernetes due to time constaint. If you want me to do it in minikube, i need couple of days to do it as i need to get it enabled form my IT service. 

