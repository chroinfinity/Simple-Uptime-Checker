pipeline {
    agent any

    environment {
        PACKAGE_NAME = "hello"
        VERSION = "1.0.0"
    }

    stages {
        stage('Prep') {
            steps {
                sh 'chmod +x hello.py'
            }
        }

        stage('Build .deb with fpm') {
            steps {
                sh '''
                    fpm -s dir -t deb \
                      -n pingrequest \
                      -v 1.0.0 \
                      hello.py=/usr/local/bin/pingrequest
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '*.deb', fingerprint: true
            }
        }
    }
}
