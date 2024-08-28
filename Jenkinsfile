pipeline {
    agent any
    environment {
        GCP_PROJECT_NAME = 'lustrous-bit-313410'
        GCS_BUCKET = 'ad-payload-bucket'
        INPUT_TOPIC = 'input_topic'
        OUTPUT_TOPIC = 'output_topic'
    }
    stages {
         stage('Install Dependencies') {
            steps {
                script {
                    // Use the full paths to python and pip from your environment
                    sh '''
                        /home/ayush_deep/myenv/bin/python3 -m venv /home/ayush_deep/myenv
                        . /home/ayush_deep/myenv/bin/activate
                        /home/ayush_deep/myenv/bin/pip install --upgrade google-cloud-pubsub google-cloud-storage google-api-core google-cloud-bigquery pybase64
                        /home/ayush_deep/myenv/bin/python --version
                        /home/ayush_deep/myenv/bin/pip --version
                    '''
                }
            }
        }
        stage('Clone Repository') {
            steps {
                deleteDir()
                git 'https://github.com/ad201125/cloudfunction-jenkins.git'
            }
        }
        stage('Fetch Payloads') {
            steps {
                sh 'python Get_Payload.py --gcp_project_name=lustrous-bit-313410 --gcs_bucket ad-payload-bucket --gcs_folder=payloads --payload_name=input.json'
                sh 'python Get_Payload.py --gcp_project_name=lustrous-bit-313410 --gcs_bucket ad-payload-bucket --gcs_folder=payloads --payload_name=expected_output.json'
            }
        }
        stage('Publish Input Payload') {
            steps {
                sh 'python cloudfunction-jenkins/PubSub_Publisher.py --input_topic=input-topic --payload=cloudfunction-jenkins/input.json'
            }
        }
        stage('Listen to Output Payload') {
            steps {
                sh 'python cloudfunction-jenkins/PubSub_Listener.py --output_topic=output-topic --output_file=cloudfunction-jenkins/received_output.json'
            }
        }
        stage('Verify Payload') {
            steps {
                sh 'python cloudfunction-jenkins/Verify_Payload.py --expected_output=my-repo/expected_output.json --actual_output=cloudfunction-jenkins/received_output.json'
            }
        }
    }
}

