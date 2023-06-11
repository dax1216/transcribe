## Getting Started
Personal Transcribe app

Create "mediafiles", "staticfiles", "static" in directory.
Create .env file. "USE_S3" to true if you want to use S3 for media and file uploads.

```
AWS_ACCESS_KEY_ID=xxxx 
AWS_SECRET_ACCESS_KEY=xxxx
AWS_STORAGE_BUCKET_NAME=xxxx
AWS_REGION=us-east-1
USE_S3=TRUE
```

Requires ffmpeg, redis (for celery)