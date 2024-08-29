pipeline {
    agent any
    environment {
        GCP_PROJECT_NAME = 'lustrous-bit-313410'
        GCS_BUCKET = 'ad-payload-bucket'
        INPUT_TOPIC = 'input_topic'
        OUTPUT_TOPIC = 'output_topic'
        PYTHON_PATH = '/home/ayush_deep/myenv/bin/python3' // Use python3 explicitly
    }
    stages {
        stage('Clone Repository') {
            steps {
                deleteDir()
                git 'https://github.com/ad201125/cloudfunction-jenkins.git'
            }
        }
        stage('Fetch Payloads') {
            steps {
                sh '''
                    ${PYTHON_PATH} Get_Payload.py --gcp_project_name=${GCP_PROJECT_NAME} --gcs_bucket=${GCS_BUCKET} --gcs_folder=payloads --payload_name=input.json
                    ${PYTHON_PATH} Get_Payload.py --gcp_project_name=${GCP_PROJECT_NAME} --gcs_bucket=${GCS_BUCKET} --gcs_folder=payloads --payload_name=expected_output.json
                '''
            }
        }
        stage('Publish Input Payload') {
            steps {
                sh '''
                    ${PYTHON_PATH} cloudfunction-jenkins/PubSub_Publisher.py --input_topic=${INPUT_TOPIC} --payload=cloudfunction-jenkins/input.json
                '''
            }
        }
        stage('Listen to Output Payload') {
            steps {
                sh '''
                    ${PYTHON_PATH} cloudfunction-jenkins/PubSub_Listener.py --output_topic=${OUTPUT_TOPIC} --output_file=cloudfunction-jenkins/received_output.json
                '''
            }
        }
        stage('Verify Payload') {
            steps {
                sh '''
                    ${PYTHON_PATH} cloudfunction-jenkins/Verify_Payload.py --expected_output=cloudfunction-jenkins/expected_output.json --actual_output=cloudfunction-jenkins/received_output.json
                '''
            }
        }
        stage('Debug Environment') {
            steps {
                sh '''
                    echo "Checking Python version:"
                    ${PYTHON_PATH} --version
                    echo "Current PATH: $PATH"
                    which python3
                '''
            }
        }
    }
}

