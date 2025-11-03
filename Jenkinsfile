pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NataliiaRom/Hillel_QAautoPython_learning'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''#!/bin/bash
                set -e
                apt-get update
                apt-get install -y python3 python3-dev python3-venv python3-pip
                rm -rf venv
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''#!/bin/bash
                set -e
                source venv/bin/activate
                pytest --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
