         pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Define image name and tag, adjust as needed
                    def imageName = 'myapp:latest'

                    // Build the Docker image
                    // Assumes Dockerfile is in the root of the project
                    docker.build(imageName)
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    def imageName = 'myapp:latest'
                    def app = docker.image(imageName)

                    // Run the Docker container
                    // Adjust the run arguments as per your requirements
                    app.run("--name myapp-container -d -p 80:80")
                }
            }
        }
    }

    post {
        always {
            // Cleanup
            script {
                docker.image('myapp:latest').remove(force: true)
                sh "docker rm -f myapp-container || true"
            }
            echo 'Post-build cleanup done.'
        }
    }
}
