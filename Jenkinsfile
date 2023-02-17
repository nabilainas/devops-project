pipeline {
    agent any
    environment {
        FLASK_APP = "app.py"
        FLASK_ENV = "development"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nabilainas/devops-project/']]])
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r ./backend/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest test.py'
            }
        }
        stage('Run API') {
            steps {
                sh 'python app.py &'
            }
        }
        stage('Merge to Dev') {
            steps {
                sh 'git checkout Dev && git merge origin/master'
            }
        }
        stage('Deploy to Dev') {
            steps {
                sh 'echo "http://localhost:5000"'
            }
        }
    }
}
