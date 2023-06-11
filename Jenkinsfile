pipeline {
    agent any 

    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    // Checking the available Python version
                    sh 'python3 --version'
                }
            }
        }
        stage('install boto3') {
            steps{
                script{
                    sh 'pip install boto3'
                }
            }
        }   
        stage('Run Python script') {
            steps{
                script {
                    // Assuming your Python script is in the same directory as your Jenkinsfile
                    sh 'EBS.py'
                }
            }
        }
    }
}
