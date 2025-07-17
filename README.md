## 🎯 Objective

Integrate the **Chapa API** to handle secure payments, allowing users to book listings and process transactions safely. This includes initiating, verifying, and updating payment status in the system.

---

## 📌 Instructions

### 🔁 1. Duplicate Project

Duplicate the project:

```bash
cp -r alx_travel_app_0x01 alx_travel_app_0x02
```

---

### 🔐 2. Set Up Chapa API Credentials

- Create a free account on [Chapa](https://developer.chapa.co/) to get your API keys.
- Store your secret key in a `.env` file:

```env
CHAPA_SECRET_KEY=your_secret_key_here
```

- Load it using `python-decouple` or `os.environ` in your `settings.py`.

---

### 🗃️ 3. Create Payment Model

In `listings/models.py`, create a `Payment` model to store:

- Booking reference
- Payment status (`Pending`, `Completed`, `Failed`)
- Amount paid
- Chapa transaction reference (`tx_ref`)
- Checkout URL

---

### 🔧 4. Create Payment API View

In `listings/views.py`:

- Create an endpoint to **initiate** a payment by making a `POST` request to Chapa:

```http
https://api.chapa.co/v1/transaction/initialize
```

- Save the returned `tx_ref` and `checkout_url` with status set to `"Pending"` in the database.

---

### ✅ 5. Verify Payment

- Create another API endpoint to **verify** the payment with Chapa.
- Use:

```http
https://api.chapa.co/v1/transaction/verify/<tx_ref>
```

- Update the `Payment` model status as `"Completed"` or `"Failed"` based on the response.

---

### 🔁 6. Implement the Payment Workflow

- When a user books a listing:
  - Automatically initiate the payment.
  - Return the Chapa **checkout URL**.
- On successful payment:
  - Update the payment status in the model.
  - Send a confirmation email (use **Celery** for background processing).
- On failure:
  - Log the issue.
  - Mark the payment as `"Failed"`.

---

### 🧪 7. Test the Integration

- Use Chapa’s **sandbox environment** to test:

  - ✅ Payment initiation
  - ✅ Payment verification
  - ✅ Status update in your `Payment` model

- Include screenshots or logs in your documentation to prove:

```text
✅ Successful initiation
✅ Verification working
✅ Final status stored
```
