---

# 1️⃣ System Components

### 1. API Gateway

Receives job requests from clients. Validates request format and forwards the request to the Job Orchestrator. Acts as the single public entry point of the system.

### 2. Job Orchestrator

Responsible for creating isolated containers for each job. It manages job lifecycle including start, monitoring, and destruction.

### 3. Isolated Container (“Simulated Enclave”)

A Docker container spun up per job. Executes the fixed credit risk scoring logic. It runs in a restricted environment with no external network access.

### 4. Attestation Service (Handled by Manoj)

Generates integrity reports verifying that the correct container image and trusted code is being executed. Provides a signed attestation document to the client.

### 5. Result Storage

Temporarily stores encrypted job outputs. No plaintext data is stored.

### 6. Logging Service

Stores only metadata such as job_id, timestamp, status, execution time. No personal or sensitive input is logged.

---


# 2️⃣ Job Execution Flow

Write it exactly like this:

1. Client requests attestation for the execution environment.
2. Attestation service returns signed integrity report.
3. Client verifies the attestation report.
4. Client sends encrypted input to `/run-job`.
5. API Gateway forwards request to Job Orchestrator.
6. Orchestrator spins up a fresh Docker container.
7. Encrypted input is passed into container.
8. Container executes credit risk scoring logic.
9. Encrypted result is returned.
10. Container is destroyed immediately after execution.
11. Client retrieves encrypted result.

---


# 3️⃣ Container Isolation Plan

This is VERY important for cloud interviews.

Write:

### Isolation Rules

* One container per job
* CPU limit: 0.5 vCPU
* Memory limit: 256MB
* No outbound internet access
* Read-only filesystem
* Auto-delete container after execution
* No shared volumes between jobs



---

# 4️⃣ API Design (First Draft)

Write:

## POST `/run-job`

**Request Body:**

```
{
  "encrypted_payload": "base64_string",
  "job_id": "uuid"
}
```

**Response:**

```
{
  "job_id": "uuid",
  "status": "RUNNING"
}
```

---

## GET `/attestation/{job_id}`

Returns signed integrity report.

Response:

```
{
  "job_id": "uuid",
  "image_hash": "sha256_hash",
  "signature": "digital_signature"
}
```

---

## GET `/job-status/{job_id}`

Response:

```
{
  "job_id": "uuid",
  "status": "COMPLETED"
}
```

---

## GET `/job-result/{job_id}`

Response:

```
{
  "encrypted_result": "base64_string"
}
```

---

# 5️⃣ Deployment Target (Choose Now)

Since you're in India and AWS is more common in placements:

✅ Choose: **Amazon Web Services**

Write:

### Deployment Configuration

* Cloud Provider: AWS
* Service: EC2
* Instance Type: t3.micro (Free tier eligible)
* OS: Ubuntu 22.04 LTS
* Docker Version: 24.x
* Region: ap-south-1 (Mumbai)

---


---

# 6️⃣ Logging & Monitoring Rules

Write:

### Logging Policy

* Only metadata is logged

* No plaintext personal data

* No encryption keys stored in logs

* Logs include:

  * job_id
  * container_id
  * execution time
  * status
  * timestamp

* Logs stored securely on the host machine

* Log rotation enabled


