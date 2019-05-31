###Run databases and microservices applications in Kubernetes 

##Process flow

#Step 1:-  Created a Java web application by using servlet it will connect to our Database to fetch some table info from Database
 Note: Now we can call this servlet using #http://localhost:8080/DatabaseAccess it will display table info.
 
#Step 2:- By Automation build tool maven, we do generate package by using 
      #mvn install
Please refer dockerfile to deploy war into the image.

#Step 3: Run the below command to build an image
docker build -t your-image-id .

#Step 4: Please refer pod.yaml to deploy pod in kubernetes
kubectl create -f pod-service.yaml
