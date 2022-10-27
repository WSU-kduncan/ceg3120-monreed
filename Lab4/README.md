# Part 2   ⋆    Setup Load Balancing
### (1) Chose to configure `.ssh/config` for Proxy, webserv1, & webserv2 
  - File is configured as seen below > 
  
    - Instance `Proxy` contains config file with connections for webserv1 and webserv2. 
    - Instance `webserv1` contains config file with connections for Proxy & webserv2. 
    - Instance `webserv2` contains config file with connections for Proxy & webserv1. 
  ```
  Host <Proxy, webserv1, webserv2>
      HostName <10.0.0.10, 10.0.1.10, 10.0.1.11>
      User ubuntu
      Port 22
      IdentityFile /home/ubuntu/.ssh/aws.pem
  ```
  
  ---
  
  ### (2) How to SSH ...
   - After configuring config files for each, use `ssh <Proxy, webserv1, webserv2>` to navigate between instances.
   
      - This is able to be done due to the existance of our config files. Each instance's `private IP` is associated to them within the config file and passed a `port 22` specification to let the system know we're making an `ssh` connection. 
      
 ---

### (3) Configuring HAProxy [⋆ *Reference* ⋆](https://linuxhostsupport.com/blog/how-to-install-and-configure-haproxy-on-ubuntu-20-04/)
  - While on **Proxy** instance, run ...
  
    - `sudo cp -a /etc/haproxy/haproxy.cfg{,.orig}` // to save original HAProxy configuration file in case of corruption
     
    - `sudo vim /etc/haproxy/haproxy.cfg` // to edit the HAProxy configuration file to include ...
    
```
frontend haproxy-main
    bind *:80                         // Configure frontend (Proxy), specify port 80/tcp 
    option forwardfor
    default_backend apache_webservers

backend apache_webservers
    balance roundrobin                         // Configure backend (webservers 1,2)
    server websvr1      10.0.1.10:80 check     & specify round robin load-balancing technique 
    server websvr2      10.0.1.11:80 check
```
   - `sudo systemctl restart haproxy` // to reboot Proxy after changes 
   
   - *(optional)* run `while true; do curl localhost; sleep 1; done` // to test round robin load-balancing
   
---

### (4) Configuring Webservers [⋆ *Reference* ⋆](https://linuxhint.com/how-to-install-and-configure-haproxy-load-balancer-in-linux/)
  - On instances **webserv1** and **webserv2** ...
  
    - `sudo vim /etc/hosts` & append `3.226.124.88 proxy` // to associate Proxy instance to each webserver 
    - `sudo systemctl enable apache2` // to enable apache2
    - `sudo /etc/init.d/apache2 start` //  to start apache2 when ready 
    - `sudo /etc/init.d/apache2 restart` // to restart apache2 after changes
  - On instance **webserv1** ...
    - `sudo vim /var/www/html/index.html` and append contents from [here](https://github.com/pattonsgirl/Fall2022-CEG3120/blob/main/Projects/Project4/index.srv1.html) 
  - On instance **webserv2** ...
    -  `sudo vim /var/www/html/index.html` and append contents from [here](https://github.com/pattonsgirl/Fall2022-CEG3120/blob/main/Projects/Project4/index.srv2.html) 
  - Our content files *(index.html)* are placed in `/var/www/html` because this is the home directory of our webserver. This is declared as `DocumentRoot` in your apache config file and can be set to whatever you please. 
  -  *(optional)* run `curl <instance-ip>` // to test display 

---

### (5) Connection to Proxy [⋆ *Try for Yourself* ⋆](http://3.226.124.88/) 
> ![image](https://user-images.githubusercontent.com/97551273/198383029-890937a3-3673-421a-9c97-67a986f2899f.png)
> ![image](https://user-images.githubusercontent.com/97551273/198383063-542edb51-ce9e-45fd-8e5a-a401daedef65.png)
