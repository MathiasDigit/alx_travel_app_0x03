## 🎯 Objective

Configure **Celery** with **RabbitMQ** to handle background tasks and implement an **email notification** feature for bookings.

---

## 🛠️ Instructions

### 1. 📁 Duplicate Project

- Duplicate the project `alx_travel_app_0x02` to a new folder named `alx_travel_app_0x03`.

---

### 2. ⚙️ Configure Celery

- Set up **Celery** with **RabbitMQ** as the message broker.
- In `settings.py`, add Celery configuration.
- Create a `celery.py` file in the root of the Django project.

---

### 3. 📬 Define Email Task

- In `listings/tasks.py`, create a `@shared_task` function to send a booking confirmation email.
- Ensure the task uses Django’s email backend (configured in `settings.py`).

---

### 4. 🚀 Trigger Email Task

- In `BookingViewSet`, override `perform_create()` to call the email task using `.delay()` after saving the booking.

---

### 5. ✅ Test Background Task

- Create a new booking.
- Confirm that the email is sent **asynchronously** via the Celery worker.
