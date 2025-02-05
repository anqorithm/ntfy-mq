---
marp: true
theme: default
paginate: true
---

# Queueing Systems in Backend  
**Better Task Handling for `Modern` Applications**

**Abdullah Alqahtani**  
 a.alqahtani059@mobily.com.sa

---

# Before Queueing Systems

- Tasks are handled `synchronously`.
- Each task must complete before the next one starts.
- Limited `scalability` and `efficiency`.

---

# What is a Queueing System?

- A way to handle tasks **asynchronously**.  
- Tasks are added to a **queue** and processed later.  

### Key Parts:
1. **Producer**: Adds tasks to the `queue`.  
2. **Queue**: Stores tasks.  
3. **Consumer**: Processes tasks.  

---

# Why Use a Queueing System?

1. **Speed**:  
   Tasks are processed in the `background`, making your app faster.  

2. **Scalable**:  
   Add more workers to handle `more` tasks.  

3. **Reliable**:  
   Tasks won't get lost, even if something fails.

---

# Common Queueing Tools

- **RabbitMQ**:  
  Reliable and widely used message broker.  

- **Apache Kafka**:  
  Great for `large-scale` event streaming.  

- **Amazon SQS**:  
  Managed queueing system for `AWS` users.  

- **Google Pub/Sub**:  
  Fully managed, real-time messaging for `GCP` environments.

- **Redis Streams**:  
  `Lightweight` and fast for `real-time` applications.  

---

# Why Google Pub/Sub?

- **Fully Managed**:  
  No infrastructure to maintain, automatic scaling.  

- **Global Scalability**:  
  Built for worldwide distributed systems.  

- **Real-time Delivery**:  
  Low-latency message delivery at any scale.  

- **GCP Integration**:  
  Native integration with Google Cloud services.  

- **Exactly-Once Delivery**:  
  Prevents duplicate processing of messages.  

---

# Why RabbitMQ?

- **Reliable**:  
  Ensures messages are delivered and processed.  

- **Flexible**:  
  Supports various messaging patterns (e.g., `Work Queues`, `Pub/Sub`).  

- **Scalable**:  
  Handles millions of tasks.  

- **Easy to Use**:  
  Simple setup and extensive documentation.

---

# How Does a Queue Work?

1. **Producer**: Sends tasks.  
2. **Queue**: Stores tasks.  
3. **Consumer**: Processes tasks.  

---

# Use Cases for Queueing Systems

1. **Image Processing**: Resize or edit images.  
2. **Email Sending**: Send emails in the background.  
3. **Data Pipelines**: Process big data in steps.  
4. **Event Handling**: Handle user actions like `clicks`.  
5. **Bulk Notifications**:  
   Send WhatsApp/SMS messages to `100,000+` users reliably.

---

# Demo Overview

Tasks are handled `asynchronously` for faster processing.

---

# Summary

- Queueing systems improve `asynchronous task handling` in backend systems.  
- `RabbitMQ` is a popular choice for reliable and `scalable` message queuing.  
- Key Benefits:
  1. `Faster` apps.
  2. `Scalable` systems.
  3. `Reliable` processing.

---

# Questions?  

**Thank You!**

**Abdullah Alqahtani**  
 a.alqahtani059@mobily.com.sa
