Can access api through a browser on any other device connected to the same wifi network as the host (this laptop)

### To run locally in test environment: 
`flask run`
- `Ctrl + C` to shut down 

### To run locally in test environment: 
1) run the gunicorn web server
    - `gunicorn -b 0.0.0.0:5001 app:app`
2) to access the api interface on any computer connected to this wifi network:
    - use this command to get your host IP address
        - `ifconfig | grep inet | grep -v inet6 | awk '{print $2}' | grep -v '127.0.0.1'`
    - enter this command: 
        - `http://[HOST_IP_HERE]:5001`


### Notes:
poseEstimationModule.findFeet(img) -> find coordinates of a person's body and face, option to draw wireframe on image 
poseEstimationModule.findFeet(img) -> locate the coordinates for the person's ankle, heel, and toes, then option to draw over them with pink dots


# FEATURES TO ADD:
    add video ability
    establish domain to access api outside of my wifi network