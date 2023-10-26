pipeline {
    agent any
    
    stages{
        stage('Clear docker images'){
            steps{
                script{
                    sh 'docker stop $(docker ps -qa)'
                    sh 'docker rm $(docker ps -qa)'
                    sh 'docker rmi $(docker images -q)'
                }
            }
        }
        stage('Build and run docker-container'){
            steps{
                script{
                    sh 'docker build -f Dockerfile -t api .'
                    sh 'docker run -d -p 5000:5000 api:latest'
                }
            }
        }
    }
}
