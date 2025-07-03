pipeline {
    agent any

    environment {
        PACKAGE_NAME = "pingrequest"
        VERSION = "1.0.1"
        ARTIFACT_NAME = "${env.PACKAGE_NAME}-${env.VERSION}-${env.BUILD_NUMBER}.deb"
    }

    stages {
        stage('Prep') {
            steps {
                sh 'chmod +x utility.py'
            }
        }

        stage('Build .deb with fpm') {
            steps {
                sh '''
                    fpm -s dir -t deb \
                      -n pingrequest \
                      -v $VERSION \
                      utility.py=/usr/local/bin/pingrequest
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '*.deb', fingerprint: true
            }
        }

        stage('Docker: Build Image') {
            steps {
                sh 'docker build -t pingrequest'
            }
        }

        stage('Docker: Run Container') {
            steps {
                sh 'docker run --rm pingrequest'
            }
        }
    }
}
