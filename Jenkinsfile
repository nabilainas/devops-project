pipeline {
    agent any
    environment {
        FLASK_APP = "app.py"
        FLASK_ENV = "development"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nabilainas/devops-project']]])
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest ./backend/test.py'
            }
        }
        stage('Run API') {
            steps {
                sh 'python3 ./backend/app.py &'
            }
        }
        stage('Merge to Dev') {
            steps {
                sh 'git checkout result-branch && git merge origin/jenkins-ci'
            }
        }
        stage('Deploy to Dev') {
            steps {
                sh 'echo "http://localhost:5000"'
            }
        }
    }
}