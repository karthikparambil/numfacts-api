# Number Trivia api

This project provides a simple Flask-based API deployed on Vercel using serverless functions.

## 📌 How to Use the API
### ▶ Base URL
https://numfactsapi.vercel.app/number/

### GET `/number/<number>`
https://numfactsapi.vercel.app/number/1

**Response:**
```json
{
    "fact": "1 is the first non-zero positive integer.",
    "number": 1
}
```

## ⭐ Advantages
### ✔ 1. Serverless & Scalable
The API runs on Vercel serverless functions — no servers to manage.
Automatically scales with traffic.

### ✔ 2. Lightweight
Uses only Flask with minimal dependencies, ensuring fast cold starts.

### ✔ 3. Easy Testing
All endpoints can be accessed via direct URLs, perfect for:

- learning APIs
- quick experiments
- small integration tasks

## Conclusion

This API is easy to use, fast to deploy, and simple to extend. It’s a clean starting point for building and testing small Flask-based services on Vercel.
