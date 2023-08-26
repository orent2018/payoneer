pipeline {

   agent any 

   environment {
     image= "simplecounter"
     container_name="mywebcontainer"
     version_tag= "${env.BUILD_ID}"
     branch= "${env.BRANCH_NAME}"
     image_name= "${image}:${branch}-${version_tag}"
     SERVER_PORT="80"
   }

   stages {

       stage('Checkout') {
            steps {
                // Checkout your Python application code from the version control system
                checkout scm
            }
        }

       stage('Build docker image') {
            steps {
               // Build the docker image for the webcounter python app 
               sh 'docker build -t ${image_name} .'
            }
    
       }

        stage('Run Tests on the Docker Container from the image') {
            steps {
                script {
                    // Run your web counter container
                    def containerId = sh(script: "docker run -d -p $SERVER_PORT:$SERVER_PORT --rm ${image_name}", returnStdout: true).trim()

                    // Wait for the server to start (you can adjust the timeout as needed)
                    sh "sleep 15s"

                    // Send a GET request to the server and check the response
                    def getResponse = sh(script: "curl -s http://localhost:$SERVER_PORT", returnStatus: true)
                    if (getResponse == 0) {
                        echo "GET Request Test Passed"
                    } else {
                        error "GET Request Test Failed"
                    }

                    // Send a POST request to the server and check the response
                    def postResponse = sh(script: "curl -s -X POST http://localhost:$SERVER_PORT", returnStatus: true)
                    if (postResponse == 0) {
                        echo "POST Request Test Passed"
                    } else {
                        error "POST Request Test Failed"
                    }

                    // Stop and remove the container
                    sh "docker stop $containerId"
                }
            }
        }
    
//       stage('Publish image to docker hub') {
//           steps {
//             withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]){
//                   sh '''
//                   docker tag ${image_name} ${image}-main
//                   docker login --username=${USER} -p ${PASS}
//                   docker push ${image}-main
//                   '''
//            }
//           }
//       }
        stage('Deploy to prod') {
          when {
            branch 'main'
          }
          steps {
            input message: "Approve Deploy to prod?", ok: "Deploy"
            sh '''
            docker tag ${image_name} ${image}-main
            docker stop ${container_name} 2> /dev/null
            sleep 20
            docker run --name ${container_name} -d -p ${SERVER_PORT}:${SERVER_PORT} --rm ${image}-main
            ''' 
          }
        }
   }
   post {

      success {
         sh 'echo "Great-SUCCESS"'
      }

      failure {
         sh 'echo "FAILURE"'
      }

   }


}
