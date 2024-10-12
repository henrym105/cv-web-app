
Can access api through a browser on any other device connected to the same wifi network as the host (this laptop)

### See examples 

### To run locally in test environment: 
1) activate python environment
    - `source venv/bin/activate`
2) run the gunicorn web server
    - `gunicorn -b 0.0.0.0:5001 app:app`
3) Open a new terminal tab or window
4) To access the api interface locally:
    - use this command to get your host IP address
        - `ifconfig | grep inet | grep -v inet6 | awk '{print $2}' | grep -v '127.0.0.1'`
    - paste this into a web browser: 
        - `__HOST_IP__:5001`


### Notes:
* poseEstimationModule.findFeet(img) 
    - find coordinates of a person's body and face, option to draw wireframe on image 
* poseEstimationModule.findFeet(img) 
    - locate the coordinates for the person's ankle, heel, and toes, then option to draw over them with pink dots.


# FEATURES TO ADD:
    - add video/livestream ability
    - establish domain to access api outside of my wifi network
