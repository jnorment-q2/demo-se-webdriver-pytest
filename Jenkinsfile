pipeline{
    agent any
    
    environment {
    }
    
    stages{
    
        stage('source'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], 
                doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], 
                userRemoteConfigs: [[url: 'https://github.com/jnorment-q2/demo-se-webdriver-pytest']]])
            }
        }
    
        stage('setup environment'){
            steps{
                dir('test'){
                    sh returnStdout: true, script: './setup_env_cloud.sh'
                }
            }
        }
    
        stage('run unit test'){
            steps{
                dir('test'){
                    sh returnStdout: true, script: 'pipenv run python -m unittest testmod' 
                }
            }
        }
    }    
    
}
