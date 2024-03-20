resource "aws_security_group" "example" {
  name        = "scraper_group"
  description = "Allow SSH traffic from my IP"

  // Inbound rule to allow SSH traffic from your IP address
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["78.90.102.146/32"] // Specify your IP address here
  }

  // Outbound rule to block all traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


#resource "aws_instance" "python_worker" {
#    depends_on = [aws_security_group.example]
#    ami = "ami-07d9b9ddc6cd8dd30"
#    instance_type = "t2.micro"
#    tags = {
#        Name = "python_scraper"
#    }
#    key_name = "PythonScraperWorker"
#    iam_instance_profile = "WebServerRole"
#    security_groups = [aws_security_group.example.name]
#    user_data = <<-EOF
#                #!/bin/bash
#                sudo apt-get update &&
#                sudo apt-get install python3-pip -y &&
#                sudo apt-get install python3-venv -y &&
#                sudo apt-get install git -y &&
#                sudo apt install ruby-full wget -y &&
#                cd /home/ubuntu &&
#                sudo wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install &&
#                sudo chmod +x ./install &&
#                sudo ./install auto &&
#                sudo service codedeploy-agent start &&
#                git clone "https://github.com/Vaskonti/Time2Play_Scraper.git" /home/ubuntu/Time2Play_Scraper &&
#                cd /home/ubuntu/Time2Play_Scraper &&
#                pip install -r requirements.txt
#                aws s3 cp s3://
#                EOF
#}

resource "aws_instance" "control-node" {
  depends_on = [aws_security_group.example]
  ami = "ami-07d9b9ddc6cd8dd30"
  instance_type = "t2.micro"
    tags = {
        Name = "control-node"
    }
    key_name = "PythonScraperWorker"
    iam_instance_profile = "WebServerRole"
    security_groups = [aws_security_group.example.name]
    user_data = <<-EOF
                #!/bin/bash
                sudo apt-get update &&
                sudo apt-get install python3-pip -y &&
                sudo apt-get install python3-venv -y &&
                sudo apt-get install git -y &&
                sudo apt install ruby-full wget -y &&
                cd /home/ubuntu &&
                git clone "https://github.com/Vaskonti/ansible_configs.git" /home/ubuntu/ansible_configs
                python3 -m pip install --user ansible
                EOF
}