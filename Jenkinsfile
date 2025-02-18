pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'github-key', url: 'git@github.com:payammirzaei/test_data_project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t test_data_project .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh 'docker run --rm test_data_project'
            }
        }
    }

    post {
        success {
            echo '✅ Build and Test Successful!'
        }
        failure {
            echo '❌ Build or Tests Failed!'
        }
    }
}
