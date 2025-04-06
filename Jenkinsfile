pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "microservices"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Tests: Web') {
            steps {
                sh '''
                    docker-compose run --rm web coverage run -m unittest test_app.py
                    docker-compose run --rm web coverage xml -o coverage.xml
                '''
                archiveArtifacts artifacts: 'web/coverage.xml', allowEmptyArchive: true
            }
        }

        stage('Run Tests: Worker') {
            steps {
                sh '''
                    docker-compose run --rm worker coverage run -m unittest test_worker.py
                    docker-compose run --rm worker coverage xml -o coverage.xml
                '''
                archiveArtifacts artifacts: 'worker/coverage.xml', allowEmptyArchive: true
            }
        }

        stage('Start Services') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Post Cleanup') {
            steps {
                sh 'docker-compose down'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
            cleanWs()
        }
    }
}
