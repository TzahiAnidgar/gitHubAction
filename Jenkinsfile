pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out source code from version control
                checkout scm
            }
        }
        stage('Set Python Env') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                '''
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
                sh 'python3 api_test.py'
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
