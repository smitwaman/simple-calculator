pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker') // Jenkins credentials ID for Docker Hub
        DOCKER_IMAGE_NAME = 'smitwaman/python-app' // Docker Hub repository name
        DOCKER_IMAGE_TAG = "${env.BUILD_NUMBER}" // Tagging the Docker image with the Jenkins build number
    }

    stages {
        stage('Build Artifact') {
            steps {
                // Checkout the code from your repository
                git 'https://github.com/smitwamn/simple-calculator.git'

                // Build the Python artifact (e.g., wheel, egg, or tarball)
                sh 'python setup.py sdist bdist_wheel'
            }
        }

        stage('Test Artifact') {
            steps {
                // Run tests on the Python artifact
                sh 'python -m unittest discover'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image with Dockerfile
                script {
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", "-f Dockerfile .")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                // Log in to Docker Hub
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIALS, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                            // Push Docker image to Docker Hub
                            docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").push()
                        }
                    }
                }
            }
        }
    }
}
