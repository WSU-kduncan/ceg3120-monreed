# Part 2 - Setup Load Balancing
### Chose to configure `.ssh/config` for Proxy, webserv1, & webserv2
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
  
  
