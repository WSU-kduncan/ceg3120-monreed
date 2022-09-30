# Part 1 - Build a VPC 
- Name: **Monica Reed**

## Create a VPC (1) 
- A virtual private cloud `(VPC)` is a way to define network resources within a cloud environment.
> ![alt text](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab2/Screenshots/VPC.jpg)

## Create a Subnet (2) 
- A `subnet` is a way in which you can specify the range of IP addresses within your VPC. 
> ![alt text](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab2/Screenshots/Subnet.jpg)

## Create an Internet Gateway (3)
- An `internet gateway` allows your VPC to communicate with connections/traffic beyond your subnet (i.e. the internet). 
> ![alt text](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab2/Screenshots/internet-gateway.jpg)

## Create a Route Table + Routes (4) 
- A `route table` allows for you add rules that determine where certain traffic is sent to within your VPC. In this case, all destinations are being sent to our internet gateway. 
> ![alt text](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab2/Screenshots/route-table.jpg)

> ![alt text](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab2/Screenshots/routes.jpg)

## Create a Security Group + Inbound Rules (5) 
- A `security group` is similar to a firewall in a sense that you can set rules that filter incoming and outgoing traffic. In this case, specifiying a list of valid IP addresses that are allowed as incoming traffic.
> ![alt text](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab2/Screenshots/security-group.jpg)

> ![alt text](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab2/Screenshots/inboundrules.jpg)

# Part 2 - EC2 Instances  
## Create New Instance (1)
- `Ubuntu` AMI selected 
- Default username is `ubuntu`

## Attach Instance to VPC (2)
- Selected my VPC `REED-VPC` from dropdown when creating instance `Reed-Instance`. This attaches my instance to my VPC. 

## IPv4 Address (3)
- A public IPv4 address can be generated upon instance creation, but I `disabled` this feature so that I can manually create my own `EIP` after. I am choosing an EIP because it does not change and will not be deleted if my instance is terminated or restarted at a later date. Without an EIP I risk having to continuously update my config file to SSH into my instance. 

## Attach Volume to Instance (4) 
- Created an `8gb gp2 volume` within the `Configure Storage` step of the instance creation process, automatically attaches upon launch.

## Tag Instance (5) 
- Created tag `Name`  -   `Reed-Instance` at the beginning of the instance creation process by typing into the `Name` space provided.

## Associate Security Group (6) 
- Within the instance creation process, selected `Select existing security group` and chose `REED-sg` from the dropdown. This associated my security group with my instance. 

## Allocate EIP (7)
- I went to the `"Elastic IPs"` section within `"Network and Security"` and allocated a new Elastic IP Address. 
- I created tag `Name`   -   `Reed-EIP` 
- To associate it with my instance, I selected `"Associate Elastic IP Address"` from the `"Actions"` dropdown and selected my instance `Reed-Instance` to attach to and selected the default Private IP address provided.

## Instance Details (8) 
> ![alt text](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab2/Screenshots/instance.png)

## Change AMI Hostname (9)
- First I ran `sudo cp /etc/hostname /etc/hostname.old` to save my old hostname
- Then, I ran `sudo vim /etc/hostname` and rewrote my hostname as `REED-AMI`

## Successful SSH Connection w/ New Hostname (10)
> ![image](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab2/Screenshots/AMI-hostname.png)
