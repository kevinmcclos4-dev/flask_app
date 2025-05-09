pipeline {
  agent any
  triggers {
    githubPush()
  }
  stages {
    stage('Webhook Trigger Test') {
      steps {
        echo "Triggered by GitHub push!"
      }
    }
  }
}