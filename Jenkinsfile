pipeline {

   agent any 

   environment {
     version_tag= "${env.BUILD_ID}"
     branch= "${env.BRANCH_NAME}"
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
               sh 'docker build -t webcounter:${branch}-${version_tag} .'
            }
    
       }

//       stage('Run tests on container from the image created') {
//            steps {
//               sh 'docker run pystache_alpine pystache-test'
//            }
    

//       }
//       stage('Publish image to docker hub') {
//           steps {
//             withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]){
//                   sh '''
//                   docker tag pystache_alpine ${USER}/repo01:pystach_a-${version_tag}
//                   docker login --username=${USER} -p ${PASS}
//                   docker push ${USER}/repo01:pystach_a-${version_tag}
//                   '''
//            }
//           }
//       }
   }
   post {

      success {
         sh 'echo "SUCCESS"'
      }

      failure {
         sh 'echo "FAILURE"'
      }

   }


}
