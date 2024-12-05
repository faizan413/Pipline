pipeline {
    agent any
    stages {
        stage('Checkout Repository') {
            steps {
                git credentialsId: '781f092e-b36a-4435-bdfb-2f9129f96e61', url: 'https://github.com/faizan413/Pipline'
            }
        }
        stage('Setup Environment') {
            steps {
                script {
                    // Ensure python3-venv is installed
                    sh '''
                        if ! dpkg -l | grep -q python3-venv; then
                            sudo apt update
                            sudo apt install -y python3-venv
                        fi
                        python3 -m venv env
                        . env/bin/activate  # Use dot instead of source
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        // Other stages like Data Preparation, Model Training, etc.
    



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
