# Smart-Factories---Predicting-Future-Failure-of-Machine

This module offers the potential to optimize maintenance tasks in real time, maximizing the useful life of their equipment and avoiding disruption to operations.

Objective:
In the past few decades, a fourth industrial revolution has emerged, known as Industry 4.0. Industry 4.0 takes the emphasis on digital technology from recent decades to a whole new level with the help of interconnectivity through the Internet of Things (IoT), access to real-time data, and the introduction of cyber-physical systems.
Industry 4.0 solutions give manufacturers the ability to predict when potential problems are going to arise before they actually happen. Systems can sense when problems are arising or machinery needs to be fixed, and can empower you to solve potential issues before they become bigger problems.
This project monitors and assesses equipment while it’s in use, to prevent failures and reducing maintenance costs.

MQTT is a standard messaging protocol for the Internet of Things. It is designed as a publish/subscribe messaging transport that is ideal for connecting remote devices. Keeping this in mind I have created an API which will take real time data from IoT sensors and will call the prediction model which will internally call the machine learning API. This model API will give the result back to the IoT API stating whether the machine is running or failing. 
We can use a web service where we can make an API call with the data points and get the prediction back or we can use a web application for the same.

Responsibilities:
1. Built machine learning model which predicts machine failure.
2. Created an API which will take real time data from IoT sensors and will internally call the machine learning model.
3. Built the dashboard which accepts real time data from IoT sensors and showcase the machine status.

Technologies used:
Python, HTML, CSS, Web API and Flask
