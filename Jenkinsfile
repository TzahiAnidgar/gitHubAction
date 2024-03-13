pipeline {
    agent any

    environment {
        // Optionally set path to include ChromeDriver if installed in a custom location
        PATH = "$PATH:/tzahianidgar/local/bin"
    }

    stages {
        stage('Preparation') {
            steps {
                // Checkout SCM
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Selenium
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install selenium
                '''
                // Download and extract ChromeDriver using curl
                sh 'curl -O https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip'
                sh 'unzip chromedriver_linux64.zip -d /usr/local/bin/'
                sh 'rm chromedriver_linux64.zip'
                // Verify ChromeDriver installation
                sh 'chromedriver --version'
            }
    }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                python3 -m pytest test.py
                '''
            }
        }
    }
    post {
        always {
            echo 'Cleaning up'
            // Clean up any actions necessary after pipeline execution
            sh 'rm -rf venv'
        }
    }
}
