pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning project...'
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    python manage.py test
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build and test successful!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}

