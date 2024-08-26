pipeline {
    agent any
    environment {
        GCP_PROJECT = 'lustrous-bit-313410'
        GCS_BUCKET = 'ad-payload-bucket'
        INPUT_TOPIC = 'input_topic'
        OUTPUT_TOPIC = 'output_topic'
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Clone Repository') {
            steps {
                deleteDir()
                git 'https://github.com/ad201125/cloudfunction-jenkins.git'
            }
        }
        stage('Fetch Payloads from GCS') {
            steps {
                sh 'python Get_Payload.py --gcs_bucket $GCS_BUCKET --gcs_folder input_folder --payload input.json'
                sh 'python Get_Payload.py --gcs_bucket $GCS_BUCKET --gcs_folder expected_output_folder --payload expected_output.json'
            }
        }
        stage('Publish Payload to Pub/Sub') {
            steps {
                sh 'python PubSub_Publisher.py --topic $INPUT_TOPIC --payload input.json'
            }
        }
        stage('Listen to Output Topic') {
            steps {
                sh 'python PubSub_Listener.py --topic $OUTPUT_TOPIC --subscription output_subscription'
            }
        }
        stage('Verify Output') {
            steps {
                sh 'python Verify_Payload.py --expected expected_output.json --actual actual_output.json'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/*.json', allowEmptyArchive: true
        }
        success {
            echo 'Test Passed'
        }
        failure {
            echo 'Test Failed'
        }
    }
}

