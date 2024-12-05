pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/faizan413/Pipeline_Project'
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv env'
                sh 'source env/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Data Preparation') {
            steps {
                sh 'python data_preparation.py'
            }
        }

        stage('Model Training') {
            steps {
                sh 'python train_model.py'
            }
        }

        stage('Model Validation') {
            steps {
                sh 'python validate_model.py'
            }
        }

        stage('Deployment') {
            steps {
                sh 'python deploy_model.py'
            }
        }
    }
}
