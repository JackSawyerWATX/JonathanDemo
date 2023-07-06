# NewDemo - Notes on pushing to AWS

To host a static HTML site on AWS from VS Code while keeping costs to a minimum, you can leverage AWS S3 (Simple Storage Service) and AWS CloudFront. Here's a step-by-step guide:

1. **Create an S3 Bucket**: Sign in to the AWS Management Console, go to the S3 service, and create a new bucket. Give it a unique name and ensure public access is enabled during the bucket creation process.

2. **Configure Bucket for Static Website Hosting**: In the bucket properties, enable static website hosting. Set the index document to `index.html` (or the desired entry point for your site).

3. **Upload your HTML Files**: Upload your HTML files and any other static assets (CSS, JavaScript, images) to the S3 bucket using the AWS Management Console, AWS CLI, or a third-party S3 client like Cyberduck.

4. **Enable Public Access**: For each file, make sure to set the appropriate permissions to allow public access. You can do this by selecting the file in the S3 bucket, choosing "Actions," and then "Make Public."

5. **Enable Static Website Hosting**: Note down the S3 bucket's endpoint URL provided in the static website hosting settings. It will be in the format `bucket-name.s3-website-<AWS-region>.amazonaws.com`.

6. **Set Up CloudFront Distribution**: Open the AWS Management Console, go to the CloudFront service, and create a new distribution. Choose the S3 bucket as the origin and configure the distribution settings accordingly. CloudFront will act as a Content Delivery Network (CDN) for your static site, improving performance.

7. **Update DNS Settings**: Once the CloudFront distribution is created, it will provide you with a CloudFront domain name (e.g., `xyz123.cloudfront.net`). Update your DNS settings (if applicable) to point your domain or subdomain to this CloudFront domain name.

By following these steps, your static HTML site will be hosted on AWS S3 with CloudFront serving as a CDN. This setup allows for efficient content delivery and scalability, while the costs remain relatively low, especially for low-traffic sites.

Remember to monitor your AWS usage and ensure that you understand the associated costs for S3 storage, data transfer, and CloudFront distribution.
