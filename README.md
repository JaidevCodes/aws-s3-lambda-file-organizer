# Serverless File Organizer using AWS S3 and Lambda

## 📌 Overview

This project demonstrates an event-driven serverless architecture using AWS.
Whenever a file is uploaded to an S3 bucket, an AWS Lambda function automatically categorizes and moves it into appropriate folders based on file type.

---

## 🚀 Features

* Automatic file organization
* Event-driven processing using S3 triggers
* Supports images, documents, videos, and others
* Prevents recursive execution (loop protection)

---

## 🏗️ Architecture

Upload File → S3 Bucket → Lambda Trigger → File Organized

---

## 🛠️ Technologies Used

* AWS S3
* AWS Lambda (Python)
* IAM Roles
* CloudWatch Logs

---

## 📂 File Categorization

| File Type  | Destination Folder |
| ---------- | ------------------ |
| .jpg, .png | images/            |
| .pdf       | documents/         |
| .mp4       | videos/            |
| others     | others/            |

---

## ⚠️ Challenges Faced

* Handling S3 folder vs file confusion
* Preventing infinite Lambda triggers
* Correct IAM permissions setup

---

## 📸 Output

Files are automatically moved into respective folders after upload.

---

## 📈 Future Improvements

* Add timestamp-based renaming
* Store metadata in DynamoDB
* Add frontend upload interface

---

## 👨‍💻 Author

Jai Dev
