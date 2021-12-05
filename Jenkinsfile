pipeline {
    agent any
    stages {
        stage('install docker/compose'){
            steps{
                sh "sudo apt-get update"
                sh "sudo apt install curl -y"
                sh "curl https://get.docker.com | sudo bash"
                sh "sudo apt update"
                sh "sudo apt install curl -y jq"
                sh 'sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
                sh "sudo chmod +x /usr/local/bin/docker-compose"
                sh "sudo usermod -aG docker jenkins"
            }
        }
        stage('Build and push images') {
            environment {
                DOCKER_NAME = credentials('docker_name')
                DOCKER_PASSWORD = credentials('docker_password')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_NAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -o StrictHostKeyChecking=no -i /home/jenkins/.ssh/id_rsa docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "scp -o StrictHostKeyChecking=no -i /home/jenkins/.ssh/id_rsa nginx.conf jenkins@swarm-manager:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i config/inventory.yaml config/playbook.yaml"
            }
        }
    }
}