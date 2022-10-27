# Part 2 - Setup Load Balancing
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
