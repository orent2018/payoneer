# payoneer
Simple web counter app


A jenkins server was deployed that listens on port 8443

Firewalld was used to create a rule to forward incoming traffic on port 443 to port 8443

A certificate and key were created converted to p12 format and added to a jenkins key store

The jenkins configuration was updated to add the HTTPS port and listen addresss as well as

keystore location and password

A simple python app webcount.py was created to count and report the number of POST requests upon

a GET request

Persistance was added to maintain the count through restarts using a file which is maintained in the docker volume
and will not change even upon image updates.

A docker file to build an image to run the python app was created

A jenkins multibranch pipeline was created to:

    - Checkout the code
    - Build the docker image
    - Test the functioning of the docker container created from the above image
    - A stage to publish the image to dockerhub was added in a comment but not implemented
    - The deploy to production stage was added to be carried out only on the main branch

Matrix-based security was enabled to allow a user "payuser" (with the same as the password) to connect to 
the Jenkins UI for view purposes aat the Jenkins URL at:   
 https://ec2-18-194-132-45.eu-central-1.compute.amazonaws.com/ 
 
Branch protection was set in github to prevent merging to main branch without a PR and its approval
A github check to verify the success of the jenkins pipeline should be added as a requirement to merging to the main branch

The application should be accessible through the URL:  http://ec2-18-194-132-45.eu-central-1.compute.amazonaws.com/


Notes:  In order to verify that the service is up a docker-compose file needs to be created with a healthcheck to curl the
        application at a predefined interval and triggering restarts if the application crashes as well as alerting upon
        such an issue.

        The docker image was run with root user due to an issue that prevented it from running on this centos machine
        Once the issue is resolved the change to webcounter user (USER webcounter) in the Dockerfile should be uncommented
        following the security practice of running images as a non root user.
