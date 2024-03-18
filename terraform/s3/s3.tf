
resource "aws_s3_bucket" "example" {
  bucket = "scraper-env" // Specify your desired bucket name
  acl    = "private" // Set ACL to private, or as required

  tags = {
    Name = "scraper-env"
  }
}

resource "aws_s3_bucket_object" "example_object" {
  bucket = aws_s3_bucket.example.id // Reference the created bucket
  key    = ".env" // Specify the key/name of the file in the bucket
  source = "../.env" // Path to the file you want to upload
}