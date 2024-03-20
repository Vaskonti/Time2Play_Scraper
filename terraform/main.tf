terraform {
  required_version = "~> 1.3"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

module "s3" {
  source = "./s3"
}


module "ec2" {
  source = "./ec2"
  depends_on = [module.s3]
}
