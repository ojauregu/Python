import boto3

s3=boto3.client("s3")

url= s3.generate_presigned_url(
	"get_object",
	Params={
		"Bucket" : "oscarini64258",
		"Key" : "package.json"
	},
	ExpiresIn=3600,
	HttpMethod="GET"
	)
	
print(url)