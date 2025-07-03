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
                      -n $PACKAGE_NAME \
                      -v $VERSION \
                      hello.py=/usr/local/bin/$PACKAGE_NAME
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
