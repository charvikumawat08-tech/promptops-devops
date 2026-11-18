pipeline {
    agent any
    stages {
        stage('Setup & Install') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test (CI Enhancement)') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }
        stage('Package Artifact') {
            steps {
                sh 'tar -czf promptops-build.tar.gz app.py requirements.txt'
            }
        }
    }
    post {
        success {
            archiveArtifacts artifacts: 'promptops-build.tar.gz', fingerprint: true
        }
    }
}