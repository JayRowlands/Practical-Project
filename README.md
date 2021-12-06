# QA Practical Project

## Contents:
* [Project Brief](#Project-Brief)
* [Risk Assessment](#Risk-Assessment)
* [Project Management](#Project-Management)
* [App Design](#App-Design)
* [Known Issues](#Known-Issues)

## Project Brief

For the scope of this project, the application must feature two random generators accompanied by a third random generator that uses the other generators. Project management through a Kanban board must also be used. The application must be containerised through Docker and deployed via Jenkins with ansible through multiple cloud-based VM's.

## Risk Assessment 

Before designing and developing the application, a risk assessment was created to outline the possible complications that could occur during the development and operation of the application as well as the measures that will be put in place to reduce the risk of these complications occurring. Please see below.

![Risk Assessment](https://github.com/JayRowlands/Practical-Project/blob/main/resources/Risk-Assessment.png) 

## Project Management

To effectively manage this project, I used Jira to set up a sprint containing user stories that listed tasks detailing the requirements of the system in correlation to the design set out. 

![DOP Board1](https://github.com/JayRowlands/Practical-Project/blob/main/resources/dop-board2.png)

![DOP Board2](https://github.com/JayRowlands/Practical-Project/blob/main/resources/dop-board1.png)


Furthermore, for the version control system, Git was used with a linked Github repository for the remote. This allowed me to keep functioning versions of code which I sometimes referred back to if for any reason that function stopped working, it also acts as a backup for the project work. Jenkins was used as a CI server with a webhook to the github repo to clone changes as they are pushed and deploy the changes. 

The Jenkins pipeline is bullet pointed in detail below:

* Checkout SCM: Github repo is cloned down
* install docker/compose: Docker and Docker-Compose are installed on the swarm virtual machines and the user groups are created
* Build and push images: Containers and images are built on the logged in Dockerhub account
* Deploy: The containers are mounted to the swarm virtual machines and a docker stack is created running the application.

![Jenkins Pipeline](https://github.com/JayRowlands/Practical-Project/blob/main/resources/pipeline.png)


## App Design

To meet the requirement set by the brief, I have developed an arcade grabber which uses get requests from service 2 and 3 to get the random values and a post request to use the values in service 4. The front end then displays all values and if the player is a winner or not.

Winner!

![Winner](https://github.com/JayRowlands/Practical-Project/blob/main/resources/winner.png)


Loser! 

![Loser](https://github.com/JayRowlands/Practical-Project/blob/main/resources/loser.png)

## Known Issues

The following error prevents the application from running via docker swarm. 
* invalid port in upstream nginx proxy_pass 