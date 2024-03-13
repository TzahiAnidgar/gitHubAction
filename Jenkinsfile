pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out source code from version control
                checkout scm
            }
        }
        stage('Setup python'){
           steps{
           withPythonEnv('/usr/bin/python3.8') {
                sh 'echo "Job is starting" '
            }
            }
         }
        stage('Setup Environment') {
            steps {
                // Install dependencies, e.g., Selenium
                // This can be customized based on your project's requirements
                sh 'pip3 install selenium'
            }
        }
        stage('Run Tests') {
            steps {
                // Run your Selenium test script
                sh 'python test.py'
            }
        }
    }
    post {
        always {
            // Collect test reports or perform cleanup
            echo 'Tests completed'
        }
    }
}
