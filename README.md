# User Activity Logger - Django REST API
 
A robust Django backend API for tracking user activities with status workflow and Redis caching.
 
# Features
 
- **User Activity Tracking**
  - Log actions: `LOGIN`, `LOGOUT`, `UPLOAD_FILE`, etc.
  - Automatic timestamp recording
  - Optional JSON metadata storage
 
- **Workflow Management**
  - Status transitions: `PENDING` → `IN_PROGRESS` → `DONE`
  - Validation for proper status transitions
 
- **API Endpoints**
  - Create, read, filter activity logs
  - Dedicated endpoint for status transitions
  - JWT Authentication (or Token Auth)
 
- **Performance**
  - Redis caching for GET requests (1-minute TTL)
  - Automatic cache invalidation on write operations
 
- **Quality Assurance**
  - Comprehensive unit tests
  - PEP8 compliant code
  - API documentation (Swagger/Redoc)
 
## 🚀 Quick Setup
 
### Prerequisites
- Python 3.8+
- PostgreSQL
- Redis
- Virtualenv (recommended)
 
### Installation
 
1. **Clone and enter project**
   ```bash
   git clone https://github.com/yourusername/user-activity-logger.git
   cd user-activity-logger
2. **Install dependencies**
    pip install -r requirements.txt
3. **Run migrations**
    python manage.py migrate
4. **Create superuser (optional)**
    python manage.py createsuperuser
5. **Run development server**
    python manage.py runserver
==============================================================================================
 
API Documentation
 
1️.Create Activity Log
POST /api/logs/
Create a new user activity entry.
 
Headers
 
Authorization: Token <your_token>
 
Request Body
 
 
{
  "action": "LOGIN",
  "metadata": {
    "ip": "192.168.0.1",
    "device": "Chrome"
  }
}
 
 
=============================================================================================
2.Get User Activity Logs
 
GET /api/logs/<user_id>
Retrieve logs for a specific user. Supports filters for action and date range.
 
Query Parameters:
 
action=LOGIN
 
 
Sample URL
 
http://127.0.0.1:8000/api/logs/1
 
 
=============================================================================================
 
 
3.Update Activity Log Status
 
PATCH /api/logs/update/<log_id>/
Update the status of a user log (PENDING, IN_PROGRESS, DONE).
 
Request Body
 
{
  "status": "IN_PROGRESS"
}