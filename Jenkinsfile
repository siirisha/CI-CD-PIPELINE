pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Simulate writing build logs to a file (logs.txt)
                    sh 'echo "Build started\nTests passed\nERROR: Failed to deploy" > logs.txt'

                    // Read log file content
                    def logText = readFile('logs.txt').trim()

                    // Call the Flask AI prediction API
                    def response = sh(
                        script: """
                        curl -s -X POST http://localhost:5000/predict \
                        -H "Content-Type: application/json" \
                        -d '{"logs": "${logText.replaceAll('"', '\\"').replaceAll('\n', ' ')}"}'
                        """,
                        returnStdout: true
                    ).trim()

                    def prediction = readJSON text: response

                    if (prediction.predictions.contains(1)) {
                        error "🚨 Build Failure Predicted! Stopping pipeline..."
                    } else {
                        echo "✅ No build failure predicted."
                    }
                }
            }
        }
    }
}
